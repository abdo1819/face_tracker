import numpy as np
from scipy.io.wavfile import write
from scipy import signal as sg
import os


# Samples per second
sps = 44100

# Frequency / pitch of the sine wave
freq_hz = 440.0

# Duration
duration_s = 5.0

# NumpPy magic
each_sample_number = np.arange(duration_s * sps)
# waveform = np.sin(2 * np.pi * each_sample_number * freq_hz / sps)
waveform = 100 * sg.square(2 * np.pi * freq_hz * each_sample_number / freq_hz)
waveform_quiet = waveform * 0.3
waveform_integers = np.int16(waveform_quiet * 32767)

# Write the .wav file
write('first_sine_wave.wav', sps, waveform_integers)

os.system("aplay first_sine_wave.wav")

''' other waves
# Fs = 44100  # Sampling Rate
# f = 440  # Frequency (in Hz)
# sample = 44100  # Number of samples
# x = np.arange(sample)

####### sine wave ###########
# y = 100*np.sin(2 * np.pi * f * x / Fs)

####### square wave ##########
# y = 100* sg.square(2 *np.pi * f *x / Fs )

####### square wave with Duty Cycle ##########
# y = 100* sg.square(2 *np.pi * f *x / Fs , duty = 0.8)

####### Sawtooth wave ########
# y = 100* sg.sawtooth(2 *np.pi * f *x / Fs )
'''
