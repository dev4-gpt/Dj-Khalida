# One Kick DJ

**When does a beat become a note?**

One synthesized kick drum, repeated at different speeds, becomes a beat, a bassline, a chord, and a melody. No samples, no other instruments. Built from an [@thel.ab67](https://www.instagram.com/reel/DeJ2WMajlAk/) reel ("When does a beat become a note?").

## Live dashboard

Open `index.html` in any browser (or serve this folder, see below). The dashboard runs itself: a looping 72-second, 7-chapter show with no input needed.

1. The kick as a plain 2 Hz beat
2. Speeding up through the ~20 Hz blur where rhythm becomes pitch
3. Landing on A1, A2, A3, A4 (55, 110, 220, 440 Hz)
4. A 3:2 perfect fifth
5. A 4:5:6 major chord
6. A full Am - F - C - G track at 120 BPM: beat, bass, chords, melody, all from that one kick
7. Loop

Live instruments around the stage: oscilloscope, spectrum analyzer, a log frequency ruler with the pitch threshold marked, per-voice cards (Hz, note, period, ratio), a live math panel (T = 1/f, semitones from A4, tempo = f x 60), and a piano strip (A1-A5).

Note: browsers block audio until the first tap or click anywhere on the page. Visuals run immediately; sound joins on that first tap. That is a browser rule, not a dashboard control.

```sh
# serve locally
python3 -m http.server 8000
# then open http://localhost:8000
```

On GitHub Pages: enable Pages for this repo (Settings > Pages > deploy from branch, root folder) and `index.html` is the site.

## The math in one screen

- Repetition rate and pitch are the same number: `f = 1 / T`. A kick every 0.5 s is 2 Hz (a 120 BPM beat). A kick every 1/440 s is 440 Hz (the note A4).
- Below ~20 hits/sec your auditory system resolves each hit separately, so you hear rhythm. Above it, hits arrive faster than that resolution and the brain measures period instead: pitch.
- Pitch is logarithmic: `semitones = 12 * log2(f2 / f1)`. Doubling the rate is +12 semitones, one octave (55 -> 110 -> 220 -> 440 is A1 -> A2 -> A3 -> A4).
- Ratios survive speed changes. Speed every voice up by the same factor and every frequency multiplies by that factor, so a 3:2 rhythm becomes a 3:2 frequency ratio: a perfect fifth. 4:5:6 becomes a major triad.
- A repeated kick is not a pure tone. By Fourier, a periodic waveform is its fundamental plus harmonics at 2f, 3f, 4f... The kick supplies the harmonic spectrum; the repetition rate chooses the fundamental. Pitch is set by the spacing between harmonics (residue pitch), which is why the 440 Hz layer can have its loudest peak at 882 Hz and still sound like 440 Hz.

Full write-up: [EXPLAINER.md](EXPLAINER.md)

## Regenerate the audio files

The dashboard synthesizes everything live in the browser. The Python version renders the same idea to WAV files:

```sh
pip install numpy
python3 make_kick_dj.py
```

Outputs:

- `01-beat-becomes-note-demo.wav` (21.5 s): one kick speeding up 2 -> 440 hits/sec
- `02-one-kick-dj-track.wav` (17 s): an 8-bar, 120 BPM Am - F - C - G track, one kick only

The kick itself: a sine whose pitch dives 160 -> 48 Hz with an exponential amplitude decay, plus a short click transient. In `make_kick_dj.py`, `add_hits()` schedules that same kick at any rate; at low rates you hear rhythm, at high rates the onsets fuse into a pitched tone at that rate.

## Build on it

Ideas that follow naturally:

- Change key, tempo, or progression in `make_kick_dj.py` (one-line changes in `render_track()`), or in the dashboard's chapter data in `index.html`
- Swap the kick recipe (different pitch dive or decay) and hear how the tone color of every layer changes at once
- Add a second one-shot (a hat or a clap) and apply the same rhythm-to-pitch treatment
- Record the dashboard and cut it as a reel

## Credit

Concept inspired by The Lab (@thel.ab67), "When does a beat become a note?" (Oct 6, 2026). Code and dashboard are original.
