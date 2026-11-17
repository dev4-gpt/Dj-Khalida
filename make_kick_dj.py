"""
One-kick DJ: everything is ONE synthesized kick drum, at different speeds.
Mirrors the @thel.ab67 reel 'When does a beat become a note?'
- ~2 hits/sec      = beat / rhythm
- ~20+ hits/sec    = your brain stops counting, hears pitch
- 55-110 Hz        = bass (A1/A2)
- 3:2 ratio        = perfect fifth,  4:5:6 ratio = major chord
- 392-880 Hz       = melody
No samples, no synths other than the kick itself.
"""
import numpy as np, wave, struct, os

SR = 44100
OUT = os.path.dirname(os.path.abspath(__file__))

def kick(dur=0.28):
    """One kick: pitch drops 160 -> 48 Hz, punchy decay + a tiny click."""
    n = int(SR * dur); t = np.arange(n) / SR
    freq = 48 + (160 - 48) * np.exp(-t * 28)
    phase = np.cumsum(freq) / SR * 2 * np.pi
    body = np.sin(phase) * np.exp(-t * 11)
    click = np.exp(-t * 220) * np.sin(2 * np.pi * 900 * t) * 0.4
    return (body + click).astype(np.float64)

KICK = kick()

def add_hits(buf, start, dur, rate_hz, gain=0.5):
    """Schedule the same kick every 1/rate seconds. At low rate = rhythm,
    at high rate the onsets fuse into a pitched tone at rate_hz."""
    s = int(start * SR); e = min(len(buf), int((start + dur) * SR))
    if rate_hz <= 0 or e <= s: return
    period = max(1, int(SR / rate_hz))
    pos = s
    klen = len(KICK)
    while pos < e:
        end = min(e, pos + klen)
        buf[pos:end] += KICK[:end - pos] * gain
        pos += period

def render_demo():
    """Part 1: the reel itself - a single kick speeding up 2 -> 440 Hz."""
    secs = [(2,2.0),(3,1.5),(4,1.5),(7,1.5),(14,1.5),(21,1.5),(27,1.5),
            (34,1.5),(55,2.0),(110,2.0),(220,2.0),(440,2.5)]
    total = sum(d for _, d in secs) + 0.5
    buf = np.zeros(int(total * SR)); tcur = 0.0
    for rate, d in secs:
        add_hits(buf, tcur, d, rate, gain=0.7); tcur += d
    return buf

def render_track():
    """Part 2: a full track from that kick alone. Am - F - C - G (as in the reel).
    beat = kick at 2/sec (120 BPM), bass = kick looped at root freq,
    chords = kick looped at 3 chord tones, melody = kick looped at note freq."""
    BPM = 120; beat = 60 / BPM; bar = beat * 4
    prog = [  # (bass_root, [chord tones], [melody notes per bar, in beats])
        (55.00,  [110.00, 130.81, 164.81], [440.00, 523.25, 659.25, 523.25]),  # Am
        (43.65,  [ 87.31, 110.00, 130.81], [349.23, 440.00, 523.25, 440.00]),  # F (F1=43.65)
        (65.41,  [130.81, 164.81, 196.00], [523.25, 659.25, 783.99, 659.25]),  # C
        (49.00,  [ 98.00, 123.47, 146.83], [392.00, 493.88, 587.33, 783.99]),  # G
    ]
    bars = 8; total = bars * bar + 1.0
    buf = np.zeros(int(total * SR))
    for b in range(bars):
        root, chord, mel = prog[b % 4]; t0 = b * bar
        intro = b < 1; full = b >= 2  # bar 1: beat only, then bass, then all
        for q in range(4):  # four-on-the-floor beat
            add_hits(buf, t0 + q * beat, 0.28, 1 / beat * 0 + 9999, gain=0)  # placeholder no-op
            s = int((t0 + q * beat) * SR); e = min(len(buf), s + len(KICK))
            buf[s:e] += KICK[:e - s] * 0.85
        if b >= 1:
            add_hits(buf, t0, bar, root * 2, gain=0.20)          # bass = kick at root*2 Hz, all bar
        if full:
            for f in chord:
                add_hits(buf, t0, bar, f * 2, gain=0.055)        # chord pad = kick at tone*2 Hz
            for i, f in enumerate(mel):
                add_hits(buf, t0 + i * beat, beat * 0.9, f, gain=0.10)  # melody, 1 note/beat
    return buf

def save(buf, name):
    buf = buf / (np.max(np.abs(buf)) + 1e-9) * 0.89
    pcm = (buf * 32767).astype(np.int16)
    stereo = np.column_stack([pcm, pcm]).ravel()
    with wave.open(os.path.join(OUT, name), 'wb') as w:
        w.setnchannels(2); w.setsampwidth(2); w.setframerate(SR)
        w.writeframes(struct.pack('<%dh' % len(stereo), *stereo))
    print(name, f"{len(buf)/SR:.1f}s")

if __name__ == '__main__':
    save(render_demo(),  '01-beat-becomes-note-demo.wav')
    save(render_track(), '02-one-kick-dj-track.wav')
