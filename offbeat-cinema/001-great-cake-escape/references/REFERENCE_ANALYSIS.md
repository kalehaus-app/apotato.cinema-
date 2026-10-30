# Reference analysis — why rough cut v1 looks unnatural

Five reference videos were uploaded on 2026-10-30 (`references/uploads_2026-10-30/`):

| File | What it is | Length | Cuts |
|---|---|---|---|
| `5c299890` | LA sidewalk walk-through: knights eating lunch, a burning skater, a gator with cucumber eyes, a nuke (watermark not identified) | 28.7 s | a continuous moving shot with gag-by-gag reveals |
| `9da0fd82` | "Mona Lisa" paparazzi / Florence (R watermark) | 13.9 s | ~18 cuts (one every ~0.8 s) |
| `b26d6edb` | Egyptian mummy proposal and sports day (R watermark) | 18.7 s | ~10 cuts |
| `8afdf7a6` | "Genghis Khan by TAPEWARP": modern-life montage | 27.8 s | ~12 cuts |
| `8aad87c0` | Seedance prompting tutorial ("stacked prompting") | 24.6 s | tutorial |

## What the references do that v1 does not

| | References | Rough cut v1 |
|---|---|---|
| **Camera** | Operated by a "person": crash zooms, rack focus, pans that arrive a little late, handheld POV, phone/paparazzi cameras | Locked-off tripod in 6 of 10 shots, because I asked for it |
| **Foreground** | Things cross the lens: photographers, bodyguards, passers-by, a fountain edge | Nothing between camera and subject |
| **Motion** | Subjects travel: walk out of doors, get into cars, run, fall, are shoved | Subjects sway in place; the cake barely moves |
| **Cut rhythm** | One gag per shot, a cut every 0.6–2 s | Shots of 2–3.5 s, held on near-still frames |
| **Sound** | Native, synced, real-world audio | Silent clips + synthetic temp mix |
| **Staging** | Candid: characters ignore the camera | Posed: start frames are a fashion-editorial tableau |

## The tutorial's three rules (`8aad87c0`)

1. **Open with the vibe:** the mood, the lighting, the environment.
2. **Direct, don't just mention:** say *what happens*, the *movement* and the *camera*
   ("a dolly zoom when you want unease", "a tracking shot when you're following motion").
3. **Separate your shots and tag each one.** Seedance reads each tag as its own moment,
   so one generation can hold a multi-shot sequence with natural cuts.

## Root causes in our process

1. **Image-to-video from a posed still** fixes frame one, and Seedance preserves the
   pose. Starting frames should be the moment *before* action, with bodies already in
   motion, or the still should be a reference only, so the model can stage the action itself.
2. **Prompts weighted toward "don't"**: half of each v1 prompt was a list of preservation
   constraints, which the model reads as "move as little as possible".
3. **"One shot per generation" was the wrong rule for Seedance 2.0.** Multi-shot tagged
   prompts give the model the cut rhythm and keep the cast consistent across those cuts.
4. **Native audio was turned off.**
5. **Post-processing** (added grain and vignette) made it look more "filtered", not more filmic.

## Revised rules (to fold into OFFBEAT_CINEMA_STYLE.md once the test confirms them)

- The camera is a character: give every shot an operator behaviour.
- Something must travel through every shot.
- Put foreground life between the camera and the subject.
- Stack the prompt: mood → environment → characters → tagged shots → sound.
- At most one line of continuity constraints. Let reference images carry identity.
- Native audio on; replace or augment it in the edit, never with synthetic placeholders.
- No added vignette.
