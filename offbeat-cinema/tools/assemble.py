#!/usr/bin/env python3
"""Assemble an animatic or rough cut from a film's SHOT_MANIFEST.json with FFmpeg.

For each shot in manifest order (only the chosen ending's payoff shots):
  - an approved video          -> trimmed to video.use_range_s
  - otherwise an existing still -> held with a slow push-in for duration_s
  - otherwise                   -> a grey slate naming the missing shot
Then concatenates to a 4:3 master and muxes audio/mix.wav if present.

Usage:
  python3 offbeat-cinema/tools/assemble.py offbeat-cinema/001-great-cake-escape --ending A
  [--out edits/animatic_v1.mp4] [--use-pending-video]
"""
import argparse
import json
import subprocess
import tempfile
from pathlib import Path

FONT = "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf"


def run(cmd):
    subprocess.run(cmd, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.PIPE)


def still_for(shot):
    img = shot["image"]
    return img.get("path") or img.get("previous")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("project")
    ap.add_argument("--ending", default=None, help="A, B or C (defaults to project.selected_ending, else A)")
    ap.add_argument("--out", default=None)
    ap.add_argument("--use-pending-video", action="store_true", help="include generated clips not yet approved")
    a = ap.parse_args()

    root = Path(a.project).resolve()
    m = json.loads((root / "SHOT_MANIFEST.json").read_text())
    w, h = m["project"]["master_resolution"]
    fps = m["project"]["fps"]
    ending = a.ending or m["project"].get("selected_ending") or "A"
    shots = [s for s in m["shots"] if s.get("ending") in (None, ending)]
    norm = f"scale={w}:{h}:force_original_aspect_ratio=increase,crop={w}:{h},fps={fps},format=yuv420p,setsar=1"

    with tempfile.TemporaryDirectory() as tmp:
        parts = []
        for n, s in enumerate(shots):
            part = Path(tmp) / f"{n:02d}.mp4"
            dur = s["duration_s"]
            v = s["video"]
            ok = v.get("approval_status") == "approved" or (a.use_pending_video and v.get("generation_status") == "generated")
            still = still_for(s)
            if v.get("path") and ok and (root / v["path"]).exists():
                t0, t1 = v["use_range_s"]
                run(["ffmpeg", "-y", "-ss", str(t0), "-t", str(t1 - t0), "-i", str(root / v["path"]),
                     "-vf", norm, "-an", "-c:v", "libx264", "-crf", "16", str(part)])
                src = "video"
            elif still and (root / still).exists():
                frames = int(round(dur * fps))
                zoom = f"zoompan=z='1+0.03*on/{frames}':x='iw/2-(iw/zoom/2)':y='ih/2-(ih/zoom/2)':d={frames}:s={w}x{h}:fps={fps}"
                run(["ffmpeg", "-y", "-loop", "1", "-i", str(root / still), "-vf",
                     f"scale={w * 2}:{h * 2}:force_original_aspect_ratio=increase,crop={w * 2}:{h * 2},{zoom},format=yuv420p,setsar=1",
                     "-frames:v", str(frames), "-c:v", "libx264", "-crf", "16", str(part)])
                src = "still"
            else:
                label = f"{s['id']}  {s['name']}  ({s['classification']})".replace(":", "\\:").replace("'", "")
                run(["ffmpeg", "-y", "-f", "lavfi", "-i", f"color=c=0x3a3632:s={w}x{h}:r={fps}:d={dur}", "-vf",
                     f"drawtext=fontfile={FONT}:text='{label}':fontcolor=0xe8dccb:fontsize=44:x=(w-tw)/2:y=(h-th)/2,format=yuv420p",
                     "-c:v", "libx264", "-crf", "16", str(part)])
                src = "slate"
            print(f"{s['id']:>5}  {dur:>4}s  {src}")
            parts.append(part)

        lst = Path(tmp) / "list.txt"
        lst.write_text("".join(f"file '{p}'\n" for p in parts))
        out = root / (a.out or f"edits/rough_cut_ending{ending}.mp4")
        out.parent.mkdir(parents=True, exist_ok=True)
        cmd = ["ffmpeg", "-y", "-f", "concat", "-safe", "0", "-i", str(lst)]
        mix = root / "audio" / "mix.wav"
        if mix.exists():
            cmd += ["-i", str(mix), "-map", "0:v", "-map", "1:a", "-c:a", "aac", "-b:a", "256k", "-shortest"]
        cmd += ["-c:v", "libx264", "-crf", "16", "-preset", "slow", "-pix_fmt", "yuv420p", "-movflags", "+faststart", str(out)]
        run(cmd)
        print(f"-> {out}")


if __name__ == "__main__":
    main()
