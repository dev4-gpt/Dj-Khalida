# Explainer: math, structure, audio, frequency correlation

## 1. Math

A sound repeated every T seconds has frequency f = 1 / T.

| Rate | Period T | What you hear |
|---|---|---|
| 2 hits/sec | 500 ms | A beat (120 BPM) |
| 10 hits/sec | 100 ms | Fast rhythm, flutter |
| 20 hits/sec | 50 ms | The blur: counting fails |
| 55 Hz | 18.2 ms | A1, a bass note |
| 110 Hz | 9.1 ms | A2 |
| 220 Hz | 4.5 ms | A3 |
| 440 Hz | 2.3 ms | A4, the tuning standard |

Pitch is logarithmic. The distance between two frequencies in semitones is
`12 * log2(f2 / f1)`, and note frequency in equal temperament is
`f = 440 * 2^((m - 69) / 12)` for MIDI note m.

- x2 rate = +12 semitones = one octave
- x3/2 rate = +7 semitones (just intonation) = perfect fifth
- x5/4 rate = +4 semitones (just intonation) = major third

## 2. Frequency correlation

Speeding a pattern up by a factor k multiplies every rate by k. Ratios between
voices are unchanged, so rhythmic ratios become harmonic ratios:

- 2 voices at 2 and 3 hits/sec (a 3:2 polyrhythm), sped up x55: 110 and 165 Hz,
  a perfect fifth, the rock power chord
- 3 voices at 4:5:6, sped up: 110 + 137.5 + 165 Hz, a major triad

A rhythm ratio and a chord are the same ratio at different speeds.

## 3. Audio

A kick drum is a short pitched transient: pitch dives roughly 160 to 48 Hz,
amplitude decays exponentially, with a broadband click at the attack.

Repeat any short sound periodically and, by Fourier's theorem, the result is a
harmonic series: energy only at f, 2f, 3f, 4f..., where f is the repetition
rate. The repeated sound shapes the level of each harmonic (the tone color);
the rate sets the fundamental (the pitch).

Perception detail: pitch follows the spacing between harmonics, not the
loudest harmonic. In our Python render, the 440 Hz layer's loudest spectral
peak measured 882 Hz (the 2nd harmonic) and it still sounds like A4. This is
residue pitch, the same effect that lets small speakers imply bass they cannot
physically produce.

Overlap matters too: the kick lasts about 0.28 s, so above roughly 4 hits/sec
successive kicks overlap before decaying. The waveform stops being separate
events with silence between them and becomes a continuous periodic wave, which
is the physical side of the rhythm-to-pitch flip.

## 4. Structure

The track and the dashboard use four layers of the same kick, separated only
by repetition rate:

| Layer | Rate zone | Role |
|---|---|---|
| Beat | ~2 Hz | Four on the floor, 120 BPM |
| Bass | 44-131 Hz | Kick looped at the chord root (x2 in the render for weight) |
| Chords | 87-392 Hz | Kick looped at three chord tones at once |
| Melody | 349-880 Hz | Kick looped at one note per beat |

Progression: Am - F - C - G, one bar each, 8 bars.

Dashboard chapters: (1) beat, (2) the sweep through the threshold, (3) octaves
A1-A4, (4) 3:2 fifth, (5) 4:5:6 chord, (6) the full track, (7) loop.
