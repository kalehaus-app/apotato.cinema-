#!/usr/bin/env python3
"""Procedural TEMP sound design for a rough cut, timed from SHOT_MANIFEST.json.

Not final audio. It gives the edit a rhythm to judge against: ambience, wheel rattle,
impacts, a plucked caper bassline (Karplus-Strong), the drop to silence and a
two-tone siren. Replace with designed foley and licensed/original music for the master.

Each shot may carry a "sound" list in the manifest; known cues:
  ambience, wheels, wheels_loud, bump, thud_scrape, silence, bird, creak, siren, wipers, music, music_stop

Usage: python3 offbeat-cinema/tools/temp_sound.py offbeat-cinema/001-great-cake-escape --ending A
Writes audio/mix_ending<X>.wav (48 kHz stereo) and copies it to audio/mix.wav.
"""
import argparse
import json
import shutil
import wave
from pathlib import Path

import numpy as np

SR = 48000
rng = np.random.default_rng(7)


def lowpass(x, a):
    """One-pole low-pass; a in (0,1), smaller = darker."""
    y = np.empty_like(x)
    acc = 0.0
    for i, v in enumerate(x):
        acc += a * (v - acc)
        y[i] = acc
    return y


def env(n, attack=0.005, release=0.2):
    e = np.ones(n)
    a, r = int(attack * SR), int(release * SR)
    if a:
        e[:a] = np.linspace(0, 1, a)
    if r and r < n:
        e[-r:] *= np.linspace(1, 0, r)
    return e


def pluck(freq, dur, decay=0.996):
    n = int(dur * SR)
    p = max(2, int(SR / freq))
    buf = rng.uniform(-1, 1, p)
    out = np.empty(n)
    for i in range(n):
        out[i] = buf[i % p]
        buf[i % p] = decay * 0.5 * (buf[i % p] + buf[(i + 1) % p])
    return out * env(n, 0.001, 0.05)


def ambience(n):
    brown = np.cumsum(rng.normal(0, 1, n))
    brown -= lowpass(brown, 0.0005)  # remove drift
    return brown / (np.abs(brown).max() + 1e-9) * 0.05


def wheels(n, loud=False):
    noise = rng.normal(0, 1, n)
    t = np.arange(n) / SR
    clack = (np.sin(2 * np.pi * 7.3 * t) > 0.92).astype(float)  # pavement joints
    rumble = lowpass(noise, 0.05) * (0.6 + 0.4 * np.sin(2 * np.pi * 13 * t))
    x = rumble * 0.5 + lowpass(noise * clack, 0.3) * 1.5
    return x / (np.abs(x).max() + 1e-9) * (0.32 if loud else 0.18)


def thud(dur=0.5, freq=55):
    n = int(dur * SR)
    t = np.arange(n) / SR
    return np.sin(2 * np.pi * freq * t * (1 - 0.4 * t)) * np.exp(-t * 9) * 0.7


def scrape(dur=1.2):
    n = int(dur * SR)
    x = lowpass(rng.normal(0, 1, n), 0.15) * env(n, 0.05, 0.6)
    return x / (np.abs(x).max() + 1e-9) * 0.25


def bird():
    n = int(0.18 * SR)
    t = np.arange(n) / SR
    f = 3800 + 1400 * np.sin(2 * np.pi * 9 * t)
    return np.sin(2 * np.pi * np.cumsum(f) / SR) * env(n, 0.01, 0.08) * 0.05


def creak(dur=0.8):
    n = int(dur * SR)
    t = np.arange(n) / SR
    f = 180 + 60 * t
    x = np.sign(np.sin(2 * np.pi * np.cumsum(f) / SR)) * (rng.uniform(0.6, 1, n))
    return lowpass(x, 0.08) * env(n, 0.1, 0.3) * 0.08


def siren(dur):
    """European two-tone (hi-lo) siren."""
    n = int(dur * SR)
    t = np.arange(n) / SR
    f = np.where((t % 1.1) < 0.55, 466.0, 622.0)
    x = np.sin(2 * np.pi * np.cumsum(f) / SR)
    x = np.tanh(2.5 * x)  # horn-like
    return lowpass(x, 0.25) * env(n, 0.3, 0.4) * 0.16


def wiper():
    n = int(0.9 * SR)
    t = np.arange(n) / SR
    squeak = np.sin(2 * np.pi * (900 + 500 * t) * t) * np.exp(-((t - 0.45) ** 2) / 0.02) * 0.06
    return squeak + np.concatenate([thud(0.25, 90) * 0.5, np.zeros(n - int(0.25 * SR))])


def bassline(dur, bpm=132):
    """Walking minor caper line: more urgent than the situation deserves."""
    notes = [73.4, 87.3, 98.0, 110.0, 116.5, 110.0, 98.0, 87.3,  # D F G A Bb A G F
             73.4, 87.3, 98.0, 103.8, 110.0, 103.8, 98.0, 82.4]  # D F G Ab A Ab G E
    beat = 60 / bpm
    n = int(dur * SR)
    out = np.zeros(n)
    i = 0
    while i * beat < dur:
        s = int(i * beat * SR)
        p = pluck(notes[i % len(notes)] * 2, beat * 0.95, 0.994)
        e = min(n, s + len(p))
        out[s:e] += p[: e - s] * 0.35
        if i % 2 == 1:  # brushed snare on 2 and 4
            h = lowpass(rng.normal(0, 1, int(0.08 * SR)), 0.6) * env(int(0.08 * SR), 0.001, 0.07) * 0.06
            out[s:min(n, s + len(h))] += h[: min(n, s + len(h)) - s]
        i += 1
    return out


def place(track, clip, at):
    s = int(at * SR)
    e = min(len(track), s + len(clip))
    if s < len(track):
        track[s:e] += clip[: e - s]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("project")
    ap.add_argument("--ending", default=None)
    a = ap.parse_args()
    root = Path(a.project).resolve()
    m = json.loads((root / "SHOT_MANIFEST.json").read_text())
    ending = a.ending or m["project"].get("selected_ending") or "A"
    shots = [s for s in m["shots"] if s.get("ending") in (None, ending)]
    total = sum(s["duration_s"] for s in shots)
    n = int(total * SR) + SR
    fx = np.zeros(n)
    mus = np.zeros(n)
    music_on = None

    t = 0.0
    for s in shots:
        d = s["duration_s"]
        ns = int(d * SR)
        cues = s.get("sound", [])
        if "silence" not in cues:
            place(fx, ambience(ns), t)
        for c in cues:
            if c == "wheels":
                place(fx, wheels(ns), t)
            elif c == "wheels_loud":
                place(fx, wheels(ns, loud=True), t)
            elif c == "bump":
                place(fx, thud(0.4, 70), t + 0.4)
            elif c == "thud_scrape":
                place(fx, thud(0.6, 50), t + 0.1)
                place(fx, scrape(min(1.5, d)), t + 0.2)
            elif c == "bird":
                place(fx, bird(), t + d * 0.55)
            elif c == "creak":
                place(fx, creak(min(1.0, d)), t + 0.2)
            elif c == "siren":
                place(fx, siren(d + 0.5), t + 0.2)
            elif c == "wipers":
                place(fx, wiper(), t + d * 0.45)
                place(fx, wiper(), t + d * 0.75)
            elif c == "music" and music_on is None:
                music_on = t
            elif c == "music_stop" and music_on is not None:
                place(mus, bassline(t - music_on) * env(int((t - music_on) * SR), 0.01, 0.03), music_on)
                music_on = None
        t += d
    if music_on is not None:
        place(mus, bassline(t - music_on) * env(int((t - music_on) * SR), 0.01, 1.2), music_on)

    mix = fx + mus
    mix = mix[: int(total * SR)]
    mix /= max(1.0, np.abs(mix).max() / 0.9)
    stereo = np.stack([mix, np.roll(mix, 12)], axis=1)  # tiny width
    out = root / "audio" / f"mix_ending{ending}.wav"
    out.parent.mkdir(exist_ok=True)
    with wave.open(str(out), "wb") as w:
        w.setnchannels(2)
        w.setsampwidth(2)
        w.setframerate(SR)
        w.writeframes((stereo * 32767).astype(np.int16).tobytes())
    shutil.copy(out, root / "audio" / "mix.wav")
    print(f"-> {out} ({total:.1f}s)")


if __name__ == "__main__":
    main()
