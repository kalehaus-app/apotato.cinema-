# 001 — The Great Cake Escape

Four young skateboarders transport an absurdly enormous wedding cake through a sleepy
European town while being pursued by the police.

House rules: [`../OFFBEAT_CINEMA_STYLE.md`](../OFFBEAT_CINEMA_STYLE.md) · Source of truth: [`SHOT_MANIFEST.json`](SHOT_MANIFEST.json)

## Status — rough cut v1 (2026-10-30)

| Deliverable | File |
|---|---|
| Rough cut, **Ending A "The Escort"** (24.1 s) | `exports/GreatCakeEscape_roughcut_v1_endingA.mp4` |
| Rough cut, **Ending B "The Wipers"** (24.3 s) | `exports/GreatCakeEscape_roughcut_v1_endingB.mp4` |
| Asset audit & continuity review | `storyboard/ASSET_AUDIT.md` |
| Storyboard + 3 endings | `storyboard/STORYBOARD.md` |
| Copy-paste prompts | `prompts/IMAGE_PROMPTS.md`, `prompts/ANIMATION_PROMPTS.md` |
| Stills animatic (pre-production) | `edits/animatic_v1_endingA.mp4` |

Both cuts: 4:3, 1440×1080, 24 fps, H.264, with a grain/vignette finish and **temp** sound.

### Shots

| # | Shot | Still | Clip | Used | Score |
|---|---|---|---|---|---|
| 01 | The Crossing | hero `d4d471f7` | `videos/01_2620d149.mp4` | 0.5–3.5 s | 9 |
| 02 | The Wheels | `2c357194` | `videos/02_9feb94d4.mp4` | 0.5–2.5 s | 9 |
| 03 | The Car | `94e5c91e` | `videos/03_7677fbde.mp4` | 0–2.6 s | 7 ⚠ |
| 04 | The Look | take 41 | `videos/04_1b9e26a5.mp4` | 0.5–3.5 s | 8.5 |
| 05 | The Strawberry | take 51 | `videos/05_abaa7a18.mp4` | 1.5–3.5 s | 9 |
| 06 | The Tip | take 63 | `videos/06_6b9bcc3f.mp4` | 0–3.5 s | 8.5 |
| 07 | The Silence | take 71 | `videos/07_0b8f1474.mp4` | 0.5–3.5 s | 9 |
| 08A1 | The Finger | take 81 | `videos/08A1_af81a3e9.mp4` | 0–2 s | 8 |
| 08A2 | The Escort | take 82 | `videos/08A2_336363ee.mp4` | 0.5–3.5 s | 8 |
| 08B | The Wipers | take 84 | `videos/08B_97a57346.mp4` | 0–4.5 s | 9 |

⚠ **03** is trimmed hard: after ~2.6 s the camera starts tracking and the police car's
livery changes. A re-take with a stronger "tripod, camera does not move" instruction
costs about 60 credits.

### Spend

12 Seedream 5.0 Pro stills (~30 credits) + 10 Seedance 2.0 1080p clips (~540 credits)
= **570 credits**. Balance went from 2,169 to 1,599.

## Not done yet / needs a decision

1. **Choose the ending:** A (escort, the third repeat of the hero wide) or B (cake on the
   bonnet, wipers). Ending C was not produced.
2. **Sound is temp.** `audio/mix_ending*.wav` is procedural: ambience, wheel rattle,
   impacts, a plucked caper bassline, the silence in 07, a two-tone siren (A) and wiper
   squeaks (B). It sets rhythm only. For the master, use designed foley plus licensed or
   original music. Higgsfield's music and SFX models are listed as "game pipeline only",
   so they weren't used.
3. **References not reviewed:** the moodboards, reference videos and Instagram creators
   were not available to this session. Add exports to `references/` to check the grade
   and pacing against them.
4. **9:16 social version:** not started. Shots 01/03/06/07/08A2 are wide and need
   per-shot reframing or outpainting, not a centre crop.
5. Optional insert: officer lowering his sunglasses (sets him up before the ending).

## Rebuild

```bash
python3 offbeat-cinema/tools/render_prompts.py offbeat-cinema/001-great-cake-escape
python3 offbeat-cinema/tools/temp_sound.py offbeat-cinema/001-great-cake-escape --ending A
python3 offbeat-cinema/tools/assemble.py offbeat-cinema/001-great-cake-escape --ending A --out exports/cut.mp4
```

## Folder map

```
hero/        locked hero frame          characters/  per-skater crops (A–D)
references/  cake + street crops        images/source/ original Higgsfield frames (untouched)
images/takes/ new Seedream takes        videos/      Seedance clips (untrimmed)
audio/       temp mixes                 edits/       animatics
exports/     rough cuts                 prompts/     generated prompt sheets
storyboard/  audit + storyboard
```
