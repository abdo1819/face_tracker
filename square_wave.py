import numpy as np
from scipy import signal
import matplotlib.pyplot as plt
from scipy.io.wavfile import write
import os

t = np.linspace(0, 1, 44100*5, endpoint=False)
waveform =signal.square(2 * np.pi * 440 * t)
waveform_quiet = waveform * 0.3
waveform_integers = np.int16(waveform_quiet * 32767)

# plt.plot(t,waveform_integers)
# plt.ylim(-2, 2)

# plt.show()
sps = 44100
write('first_sine_wave.wav', sps, waveform_integers)

os.system("aplay first_sine_wave.wav")
