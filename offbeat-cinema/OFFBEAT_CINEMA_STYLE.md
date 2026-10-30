# OFFBEAT CINEMA — House Style & Production System

> **Beautifully shot films about things that should not exist.**

This file is the reusable standard for every Offbeat Cinema film. Each film gets its
own folder (`NNN-film-slug/`) with a `SHOT_MANIFEST.json`, but the rules here apply to all.

---

## 1. The test

Every film must make a viewer ask: **"What movie is this from? I want to see the rest."**

Each film needs:
- one clear central idea (one sentence),
- at least one unforgettable image,
- intentional camera work (every move has a reason),
- a satisfying cinematic moment (a payoff, not a fade-out).

## 2. Tone

- Deadpan characters, impossible situations. **Nobody acknowledges the absurdity.**
- Treat the ridiculous with the urgency normally reserved for diamonds, bombs, heists.
- Physical comedy and visual storytelling over dialogue. Dialogue is the exception.
- Comedy comes from composition and timing: the locked-off wide, the held beat, the repeat.

## 3. Look

| Element | Standard |
|---|---|
| Era feel | 1970s–1990s analog cinema, European independent film, vintage fashion editorial |
| Capture | 35mm motion-picture photography; slightly faded photochemical colour |
| Light | Natural, motivated light. Warm afternoon sun and slight haze are the default |
| Texture | Organic grain, soft highlight roll-off, natural skin texture, believable motion blur |
| Lenses | Normal to slightly long (35–85mm feel). Wide only with intent |
| Movement | Mostly static or gently handheld. Tracking only when following action |
| Aspect | 4:3 master by default. Vertical versions are reframed, never blindly cropped |

**Never:** HDR look, plastic CGI, decorative lens flares, constant slow motion, random
drone/orbit moves, digital over-sharpening, modern cars/phones/signage/logos, typography in frame,
title-card clichés, captions burned into the master.

## 4. Directing rules (learned on Film 001)

1. **The hero frame is law.** Every film has one approved hero image. It outranks every
   written description. Priority: hero frame → characters & costumes → hero prop →
   environment → light direction & colour → texture.
2. **Lock screen direction.** Decide which way the action travels on screen and keep it
   (Film 001: the cake travels screen-left).
3. **Count people in every frame.** Image models duplicate characters. A frame with the
   wrong head-count is rejected, however beautiful.
4. **Edit, don't re-imagine.** Reference-based edits of the hero (same framing, one change)
   keep continuity almost perfectly. Big reframes drift. Prefer: hero → instruction edit →
   crop/zoom edit → new angle, in that order of safety.
5. **Repeat compositions for comedy.** A locked wide shown twice with one thing changed is
   cheaper to generate, safer for continuity, and funnier than a new angle.
6. **No baked motion blur in start frames.** A still that already contains motion blur
   animates badly.
7. **Few, deliberate attempts.** Draft at 720p (≈4.5 credits/s), review, and only then
   render the winner at 1080p (≈12 credits/s).

## 4b. Motion & camera grammar (learned from the references, 2026-10-30)

Rough cut v1 looked like animated photographs: locked cameras, posed start frames,
prompts that were mostly "don't". The references (`001-great-cake-escape/references/
REFERENCE_ANALYSIS.md`) and the two 720p tests settled these rules:

1. **The camera belongs to someone.** A passer-by, a paparazzo, someone on a balcony. It's
   handheld, it reacts, and it arrives a little late. Crash zooms and fast push-ins are
   allowed; random orbits are not.
2. **Something travels through every shot.** Subjects enter, cross and leave frame.
   Nobody "sways in place".
3. **Foreground life.** Put people, objects or architecture between the lens and the
   subject: a newspaper reader, a cyclist, a pillar, a shoulder.
4. **Occlusion is the cut.** A hand over the lens, a door closing or a body passing makes
   the next shot feel motivated.
5. **One event per shot, cut fast.** A cut every 0.7–2.5 s. Scale moves wide → medium →
   close, then jumps back out to a big wide.
6. **Multi-shot generations.** Seedance 2.0 reads tagged shots (`[Shot 1, handheld wide] …`)
   as separate moments and keeps the cast consistent across them. Write a whole scene
   (10–15 s, 3–5 shots) per generation, using approved stills as `image_references`.
   Use a `start_image` only when the first frame must match exactly, and then describe
   the motion boldly.
7. **Stacked prompt order:** mood/lighting → environment → characters → tagged shots
   (each one: framing + camera behaviour + what happens) → sound. Keep continuity
   constraints to one line; the reference images carry identity.
8. **Native audio on.** Design and replace sound in the edit later, but never ship silent
   clips with synthetic placeholders.
9. **No added vignette.** Grain only if the clip lacks it.

## 5. Prompt templates

### Image (still) prompt — every field required

```
[FRAME]      A cinematic 35mm film still from the same fictional film as the reference image.
[SUBJECT]    Exactly who/what is in frame, with head-count ("exactly four young men…").
[ACTION]     The single moment being captured.
[CAMERA]     Position, height, lens feel, framing (wide/medium/close), angle.
[RELATION]   Where the subjects are relative to camera and to each other; screen direction.
[BACKGROUND] Specific environment details carried over from the hero.
[LIGHT]      Direction, time of day, quality (must match hero).
[TEXTURE]    35mm, faded photochemical colour, grain, soft roll-off.
[KEEP]       What must stay identical (faces, costumes, prop geometry, street).
[NEVER]      Unwanted changes: extra people, new outfits, modern objects, text, motion blur.
             Aspect ratio.
```

### Animation (image-to-video) prompt — every field required

```
[START]      "Use the supplied image as the exact opening frame."
[MOVES]      Who/what moves, direction (screen-left/right/toward camera), speed.
[CAMERA]     Static / handheld / track — and why.
[ENVIRONMENT] Ambient motion (haze, a curtain, distant traffic).
[PHYSICS]    Contact points and weight (feet on boards, hands on cake, wobble).
[EMOTION]    How the performance reads (deadpan, urgent, frozen).
[KEEP]       Identities, costumes, prop geometry, location, lighting unchanged.
[NEVER]      No cuts, no slow motion, no new characters, no morphing, no camera move
             without purpose.
[DURATION]   Generated length → used length.
[SOUND]      Native audio off unless testing; sound is designed in the edit.
```

## 6. Pipeline

```
1. Hero frame approved           → hero/
2. Asset audit (KEEP / REGENERATE / OPTIONAL / REJECT)
3. Continuity library            → characters/, references/
4. Storyboard + endings          → storyboard/
5. Missing stills (edits of hero first)          → images/
6. Review & approve stills       (manifest: approval_status)
7. Image-to-video, one shot each → videos/
8. Review clips (faces, limbs, feet, prop size, head-count, background)
9. Rough cut (FFmpeg/Remotion)   → edits/
10. Sound design + music         → audio/
11. Master 4:3 24fps + 9:16 social → exports/
```

Each film's `SHOT_MANIFEST.json` is the source of truth for every shot: prompt, inputs,
model, parameters, outputs, status, continuity score and approval.

### Status vocabulary

- `classification`: `KEEP` · `REGENERATE` · `OPTIONAL` · `REJECT` · `MISSING`
- `generation_status`: `not_started` · `queued` · `generated` · `failed`
- `approval_status`: `pending` · `approved` · `rejected`
- `continuity_score`: 1–10 against the hero frame (8+ = usable, 6–7 = fix, ≤5 = reject)

### Clip review checklist

- [ ] Same faces, hair and outfit assignments as the character sheet
- [ ] Head-count correct for the whole clip
- [ ] Hero prop keeps size, tier count and decoration
- [ ] No sliding feet, melting wheels, extra limbs or floating objects
- [ ] Shadows consistent with the hero light direction
- [ ] Background does not swap mid-shot
- [ ] Screen direction respected
- [ ] Camera movement has a narrative reason

## 7. Sound

Sound makes the absurd feel real. Build each film from: specific foley (wheels, shoes,
props) → location ambience → one restrained period-appropriate musical idea → **silence used as
a punchline**. Music should be more urgent and dramatic than the situation deserves. Only
original or properly licensed music.

## 8. Delivery

- **Master:** 4:3, 1440×1080, 24 fps, H.264 (high bitrate) or ProRes 422.
- **Social:** 9:16, 1080×1920, reframed shot by shot (or outpainted), no burned-in captions.
- Review every vertical shot for lost action before export.

## 9. Credentials & cost

- Never commit API keys or tokens.
- Never spend generation credits without explicit approval for that batch.
- Record every generation (model, params, seed, cost) in the manifest.
