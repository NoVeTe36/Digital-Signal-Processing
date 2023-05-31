import numpy as np
from scipy import signal
import matplotlib.pyplot as plt
import signals
from scipy.fftpack import fft

x = signals.Input_1kHz_15kHz
Fs = 10000

# Part 2 - Highpass Filter Design
b_high, a_high = signal.butter(4, 1000, btype='highpass', fs=Fs)
w_high, h_high = signal.freqz(b_high, a_high)
x_high = signal.filtfilt(b_high, a_high, x)

plt.title('Frequency domain of input signal and filtered signals')
fft_x = fft(x)
plt.plot(abs(fft_x))
fft_x_high = fft(x_high)
plt.plot(abs(fft_x_high))
plt.legend(['Input signal', 'Highpass filtered signal'])
plt.show()

fig, axs = plt.subplots(2, 1, sharex=True, figsize=(10, 10))
axs[0].plot(x)
axs[0].set_title('Input Signal')
axs[1].plot(x_high)
axs[1].set_title('Highpass Filter Output')
plt.tight_layout()
plt.show()

fig, axs = plt.subplots(1, 1, sharex=True, figsize=(10, 10))
axs.plot(w_high, 20 * np.log10(abs(h_high)))
axs.set_title('Highpass Filter Frequency Response')
axs.set_ylabel('Magnitude [dB]')
axs.set_xlabel('Frequency [rad/sample]')
plt.tight_layout()
plt.show()