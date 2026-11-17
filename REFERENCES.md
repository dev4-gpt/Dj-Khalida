# Reference: the original reel

This project is a rebuild of one specific reel. Watch it first, everything in
this repo follows from it.

## The reel

- **Watch:** https://www.instagram.com/reel/DeJ2WMajlAk/
- **Creator:** The Lab (@thel.ab67), "Physics and Maths sims"
- **Title / hook:** "When does a beat become a note?"
- **Posted:** October 6, 2026
- **Length:** about 64 seconds
- **At time of checking (Nov 16, 2026):** 272,873 likes, 1,554 comments, 173K followers

## What happens in it

1. A single kick drum starts at 2.0 hits per second, shown as a slow rotating
   dot. The speed climbs: 3, 4, 7, 14, 21, 27, 34 hits per second.
2. Past about 20 hits per second the individual beats blur and a tone appears:
   55 Hz (A1), then 110, 220, and 440 Hz (A4, the note orchestras tune to).
3. Two drums in a 3:2 polyrhythm, sped up, become a perfect fifth
   (110 Hz + 165 Hz), described in the reel as the power chord from every
   rock song.
4. Three drums in a 4:5:6 ratio, sped up, become a major chord
   (110 + 138 + 165 Hz), the "happy chord".
5. Finale: a whole song from the one kick sample at different speeds.
   Beat at 10-15 hits/sec (Am), bass at 44-65 Hz (F), chords at 175-392 Hz (C),
   melody at 392-880 Hz (G). Closing idea: same kick, different speed.

Caption gist: speed a kick drum past ~20 hits per second and your brain stops
counting and hears a pitch; the reel asks viewers when they heard it turn
into a note. Hashtags include #musictheory #physics #producer #sounddesign
#math #asmr.

## How this repo maps to it

| Reel moment | In this repo |
|---|---|
| Kick speeding 2 to 440 hits/sec | `make_kick_dj.py` demo render; dashboard chapters 1-3 |
| 3:2 becomes a perfect fifth | Dashboard chapter 4; EXPLAINER.md section 2 |
| 4:5:6 becomes a major chord | Dashboard chapter 5; EXPLAINER.md section 2 |
| Full song from one kick (Am-F-C-G) | `make_kick_dj.py` track render; dashboard chapter 6 |

## Note on the video itself

The reel video is the creator's work, so this repo links to it on Instagram
rather than hosting a copy. If the link ever goes down, the breakdown above
and EXPLAINER.md preserve everything the build depends on.
