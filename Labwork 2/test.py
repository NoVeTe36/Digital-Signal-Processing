import numpy as np
from scipy import signal
import matplotlib.pyplot as plt
import signals
from scipy.fftpack import fft

# Specify the filter parameters
Fs = 10000  # sampling frequency
# cutoff = 100  # cutoff frequency
# filter_order = 10  # filter order

# Design the Bessel filter
b_bessel, a_bessel = signal.bessel(4, 400, btype='lowpass', fs=Fs)
# Frequency response of the filter
w_bessel, h_bessel = signal.freqz(b_bessel, a_bessel)


# Design the Butterworth filter
b_butter, a_butter = signal.butter(1, 400, btype='lowpass', fs=Fs)
# Frequency response of the filter
w_butter, h_butter = signal.freqz(b_butter, a_butter)

# Design the Chebyshev filter
b_cheby, a_cheby = signal.cheby1(12, 1, 400, btype='lowpass', fs=Fs)
# Frequency response of the filter
w_cheby, h_cheby = signal.freqz(b_cheby, a_cheby)

# Generate input signal with frequency components ranging from 1 kHz to 15 kHz
x = signals.Input_1kHz_15kHz

# Apply the filters to the input signal
x_bessel = signal.filtfilt(b_bessel, a_bessel, x)
x_butter = signal.filtfilt(b_butter, a_butter, x)
x_cheby = signal.filtfilt(b_cheby, a_cheby, x)

plt.title('Frequency domain of input signal and filtered signals')
fft_x = fft(x)
plt.plot(abs(fft_x))
fft_x_bessel = fft(x_bessel)
plt.plot(abs(fft_x_bessel))
fft_x_butter = fft(x_butter)
plt.plot(abs(fft_x_butter))
fft_x_cheby = fft(x_cheby)
plt.plot(abs(fft_x_cheby))
plt.legend(['Input signal', 'Bessel filtered signal', 'Butterworth filtered signal', 'Chebyshev filtered signal'])
plt.show()

# Plot the input and output signals for each filter
fig, axs = plt.subplots(4, 1, sharex=True, figsize=(10, 10))
axs[0].plot(x)
axs[0].set_title('Input Signal')
axs[1].plot(x_bessel)
axs[1].set_title('Bessel Filter Output')   
axs[2].plot(x_butter)
axs[2].set_title('Butterworth Filter Output')
axs[3].plot(x_cheby)
axs[3].set_title('Chebyshev Filter Output')
plt.tight_layout()
plt.show()


# Plot the frequency response of each filter
fig, axs = plt.subplots(3, 1, sharex=True, figsize=(10, 10))
axs[0].plot(w_bessel, 20 * np.log10(abs(h_bessel)))
axs[0].set_title('Bessel Filter Frequency Response')
axs[0].set_ylabel('Magnitude [dB]')

axs[1].plot(w_butter, 20 * np.log10(abs(h_butter)))
axs[1].set_title('Butterworth Filter Frequency Response')
axs[1].set_ylabel('Magnitude [dB]')

axs[2].plot(w_cheby, 20 * np.log10(abs(h_cheby)))
axs[2].set_title('Chebyshev Filter Frequency Response')
axs[2].set_ylabel('Magnitude [dB]')
axs[2].set_xlabel('Frequency [rad/sample]')
plt.tight_layout()
plt.show()