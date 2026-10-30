# The Great Cake Escape — Final Storyboard (v1)

**Runtime:** about 24 s · **Aspect:** 4:3 · **Frame rate:** 24 fps · **Screen direction:** the cake travels screen-left.

## The structural idea: the rule of three

The hero wide is the spine of the film. We see **the same locked-off composition three
times**, with one thing changed each time:

1. **Shot 01:** the cake crosses the street. Calm, absurd, beautiful.
2. **Shot 03:** same frame, same moment, but **a police car now sits behind them**.
3. **Shot 08:** same frame again for the payoff (with the recommended ending).

This is a Tati / Roy Andersson / Wes Anderson device. Repeating a composition with one
change is funny in itself. It is also cheaper, and it is the **safest possible thing for
continuity**: Seedream holds the hero almost perfectly when the framing doesn't change.

---

## Shot list

| # | Act | Dur | Shot | Source | Status |
|---|---|---|---|---|---|
| 01 | Escape | 3.0 s | **THE CROSSING.** Locked-off wide at eye level. Four skaters push the cake slowly screen-left across the crossing. The bystander in the doorway watches, unmoved. | `d4d471f7` (hero) | KEEP |
| 02 | Escape | 2.0 s | **THE WHEELS.** Ground-level low angle. Skateboards rattle under the board and the cake towers against the blue sky. Handheld, tracking left at their speed. | `2c357194` | KEEP |
| 03 | Pursuit | 3.0 s | **THE CAR.** Back to the exact hero wide. The white police sedan with its blue beacon is now behind them. It creeps forward and the beacon turns once, silently. Nobody has noticed. Then D slowly turns his head. | `94e5c91e` | KEEP |
| 04 | Pursuit | 2.5 s | **THE LOOK.** Medium shot of D (Lookout) and C (Pusher). D stares back over his shoulder; C looks up from pushing and follows his eyeline. A beat. They push harder. Police car soft in the background. | new edit of hero | MISSING |
| 05 | Close call | 2.0 s | **THE STRAWBERRY.** Extreme close-up of the top-tier strawberries. The street blurs past. The platform hits a bump and one strawberry shivers on its rosette of frosting. | regenerate `b82b2caf` | REGENERATE |
| 06 | Close call | 3.5 s | **THE TIP.** Same hero street. Swerving away from the car, the board jolts and the whole cake tilts off one edge of the board. All four lunge. | fix `55405ae1` | REGENERATE |
| 07 | Close call | 3.0 s | **THE SILENCE.** Static. The cake holds at an impossible 20° angle, balanced on one edge. Four skaters freeze with fingertips on the frosting, not breathing. All sound drops out except one distant bird. | new edit of fixed 06 | MISSING |
| 08 | Payoff | 4.5 s | **THE PAYOFF.** See endings below. | new | MISSING |

**Total: 23.5 s.** Sound design and the payoff hold can stretch it to 25 s.

### Pacing shape

```
01 ███ calm, wide   02 ██ fast, low   03 ███ calm (dread)   04 ██▌ medium beat
05 ██ ECU fast      06 ███▌ chaos     07 ███ dead stop       08 ████▌ release
```

Cuts speed up from 03 to 06, stop dead at 07, and release at 08. Match cuts:
**02 → 03** (rattling wheels cut to the silent wide) and **05 → 06** (the strawberry shiver
cuts to the whole cake tipping: small wobble, then big wobble).

### Optional inserts (only if pacing needs them)

- **Officer, lowering sunglasses**: 1.5 s, between 04 and 05. Locks his identity before the
  ending and is required for Ending A. Recommended if we choose A.
- **Grandmother on a balcony**, shelling peas, unimpressed: 1.5 s, after 07. A good laugh
  beat, but it is one more character to keep consistent.
- **Police tyre stopping**: 1 s. Skip; the car is already established.

### Officer & car (lock before generating 04)

- **Car:** the white sedan with a single blue rotating roof beacon from `94e5c91e`. It is the
  reference for every police shot.
- **Officer** (only appears if the ending needs him): a man in his fifties with a thick dark
  moustache and aviator sunglasses, a short-sleeved pale-blue uniform shirt and a white
  peaked cap. No real-agency insignia or text.

---

## Three endings

### A — "THE ESCORT" ★ Recommended

The cake is about to fall in 07. **A fifth hand enters frame**: pale-blue sleeve, wedding
ring, one finger. It steadies the cake back upright (08a, 1.5 s insert). Cut to **the hero
wide for the third time** (08b, 3 s): the police car is now **in front** of the cake, beacon
turning, the officer's arm out of the window waving the street clear. The four skaters ride
behind in perfect, dignified formation. They were never being chased. They were being
escorted.

- *Why it works:* it completes the rule of three, reverses the premise, and stays deadpan.
  It is the most "what film is this?" ending.
- *Risk:* **low.** 08b is one edit of the hero. 08a is a simple close-up.
- *Sound:* the siren finally switches on, and it becomes the music.

### B — "THE WIPERS"

The cake falls in 07. Cut to black for one beat of silence. Then a locked shot of the police
car through its windshield: the **entire cake has landed upright on the bonnet**, its bottom
tier pressed against the glass. Inside, the officer sits motionless behind pink frosting.
The wipers switch on, *thunk… thunk*, clearing two arcs to reveal his unmoving face.

- *Why it works:* it is the most unforgettable single image, and pure physical comedy.
- *Risk:* **high.** Frosting smearing under wipers is hard for current video models. The cake
  has to keep its design after impact. Plan 2–4 attempts.
- *Sound:* total silence, then the wipers squeak.

### C — "THE WINDOW DISPLAY"

The cake is saved. In a panic they push it flush against the patisserie window ("Beerstogdoiles")
and freeze beside it in poses, like a shop display. The police car rolls slowly past. The
officer glances, nods approvingly at the cake, and drives on. Hold. D reaches up, takes one
strawberry, and eats it.

- *Why it works:* it is a quiet, Andersson-like ending with a final character beat.
- *Risk:* **medium.** It needs a new composition (the shopfront) and the car moving through frame.
- *Sound:* the engine fades away, then one wet strawberry bite.

**Recommendation:** shoot **A**, because it gives the cleanest structure at the lowest cost. If
budget allows, test **B's** single still first (one image, a few credits) before committing
to animating it. If that still is spectacular, it may be worth the risk.
