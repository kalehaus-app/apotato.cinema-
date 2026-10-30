# The Great Cake Escape — Asset Audit & Continuity Review

**Source:** Higgsfield generation history, pulled through the authenticated Higgsfield
connector on 2026-10-30. All originals were downloaded at full resolution to
`images/source/` (filenames are the first 8 characters of the Higgsfield job ID).
`images/source/higgsfield_generations.json` holds the full prompts, seeds and parameters.

**Not received:** the curated moodboard, the Higgsfield moodboard, the reference videos and
the three Instagram references. Instagram requires a login and cannot be fetched from here.
The visual direction below comes from the brief and the hero frame. Drop exports into
`references/` and the direction can be checked against them.

---

## Locked hero frame

**`d4d471f7` → `hero/HERO_d4d471f7.png`** — Higgsfield Soul v2, 2048×1536 (4:3), seed 100656,
style "Elegance in Leisure".

Note: the hero's text prompt says "three-tiered", but the image shows **four tiers**. The
image wins.

### Character sheet (crops in `characters/`)

| ID | Name | Look | Hero position |
|---|---|---|---|
| A | **Stripe** | Orange-and-blue jersey with white side panels, royal-blue shorts with a white side stripe, white tube socks, white sneakers. Short dark hair, slim. | Far left, walking, hand on cake |
| B | **Tank** | White sleeveless vest, **white** shorts, white socks, **dark/black** sneakers. Tallest; longer dark wavy hair. | Left, behind A, hand on cake |
| C | **Pusher** | White tee with blue sleeve trim, blue shorts with red/white side stripes, white socks with navy/black stripes, white sneakers. Dark hair, bent forward. | Right, pushing, foot on skateboard |
| D | **Lookout** | Cream ringer tee with blue/red trim and a red-blue cherry graphic on the chest, blue shorts, white socks with blue stripes, white sneakers. Feathered brown hair. | Far right, on skateboard, looking back |

The brief lists "vintage blue athletic shorts" for everyone. In the hero, **B wears white
shorts**, and the hero takes precedence.

**Background extra:** a young man in a blue tee and dark trousers stands in the shop doorway
far left. He is part of the location. Keep him in shots that use the hero street, and never
count him as a skater.

### Hero prop: the cake (`references/REF_cake.png`)

Four tiers of blush-pink frosting with white piped swags and pearl borders. There are
strawberry clusters on the top, on tier 2 and on tier 3, and pink roses with orange/red
blooms on tiers 1 and 2. It sits on a wide, low, white board. The board rides on
skateboards (visible in `2c357194`; hidden by the angle in the hero). The cake stands about
1.5× the height of the skaters.

### Environment (`references/REF_environment_street_depth.png`)

A narrow Mediterranean or Central-European street with cream and terracotta facades, a
maroon awning, and a pastiche shop sign ("Beerstogdoiles") at left. Overhead tram/phone
wires run along the street. A **blue 1960s sedan** and a **cream 1960s sedan** are parked
mid-right. The road is grey asphalt with a faded pedestrian crossing. Sun comes from the
front-left in late afternoon with soft haze. The far end of the street recedes to the
right.

### Screen direction (locked)

The cake travels **screen-left**: pushers are on the right and the street recedes to
background-right. "Behind them" means background-right.

---

## Frame-by-frame audit

| Job | What it shows | Story use | Continuity | Physical / artifacts | Call |
|---|---|---|---|---|---|
| `d4d471f7` | Hero wide: four skaters push the cake across the street | Shot 01 | 10 — reference | Board has no visible wheels (fine at this angle). Pastiche signage is acceptable. | **KEEP (HERO)** |
| `94e5c91e` | Hero framing, blue sedan replaced by a **white police sedan with a blue roof beacon** | Shot 03 — same wide, now with police | 9.5 — identical cast, cake and street | Police car reads clearly; nothing else changed | **KEEP** |
| `7aa40a7e` | Same idea, police car is a grey/blue sedan with a light bar, closer, partly hidden | Alternate for Shot 03 | 9 | Car is half-hidden behind C and less readable as police | **OPTIONAL** (backup to `94e5c91e`) |
| `2c357194` | Low ground-level angle: same four plus the extra; the board rides on skateboards | Shot 02 | 9 — faces, outfits and cake match. Sky is cleaner and bluer than the hero. | Skateboards under the board are believable. No defects found. | **KEEP** |
| `55405ae1` | Cake tipping off the board; all of them lunge | Shot 06 | 6 — **five** people on the left (an extra jersey behind A), and D's tee lost its graphic | Strong composition and the tipping physics read well | **REGENERATE** (inpaint/edit fix) |
| `b82b2caf` | Extreme close-up of a strawberry on the frosting | Shot 05 | 8 — frosting and strawberry style match | **Spin motion blur is baked into the still**. It will animate badly and reads as spinning, not wobbling | **REGENERATE** (clean, at rest) |
| `16859572` | Side-profile wide; skaters running | — | 3 — **five** skaters, a duplicate A jersey, a new blue/red jersey, the cake moving with nobody touching it, the cake shrunk, boards abandoned | Broken story logic | **REJECT** |
| `5e2ee19d` | Soul variation: three tiers, different cast including a young woman, green shorts | — | 2 — different film | Good look | **REJECT** (archive) |
| `4b979e27` | Soul variation: different cast, red shorts, fish-eye feel | — | 2 | Stretched wheels, garbled signage | **REJECT** (archive) |
| `0172e2b5` | Soul variation: tall cake, different cast, police car in the distance | — | 2 | Beautiful framing, wrong people | **REJECT** (archive; possible style reference) |

Earlier experiments (Oct 27–28: three skaters, a white birthday cake, a 2002-American look)
belong to an earlier concept. They are left in Higgsfield and were not downloaded.

### What the audit tells us

- Seedream 5.0 Pro edits with the hero as reference **hold continuity when the framing stays
  the same** (`94e5c91e`, `7aa40a7e`: near-perfect).
- They **drift when the camera moves far** (`16859572`) and **duplicate people when the
  action gets crowded** (`55405ae1`).
- So: missing frames should be generated as edits of the hero or an approved derivative,
  with character crops as extra references. Every prompt must state the head-count, and
  every new angle should be a moderate move, not a full re-stage.

### Usable now

**3 KEEP** (01, 02, 03) · **1 OPTIONAL** backup · **2 REGENERATE** (05, 06) ·
**3 MISSING** (04, 07, 08) · **4 REJECT**.
