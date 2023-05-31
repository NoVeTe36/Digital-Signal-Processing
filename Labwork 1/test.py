from scipy.signal import butter, filtfilt
import signals
import numpy as np
import matplotlib.pyplot as plt
import scipy
from scipy.fft import fft, ifft, fftshift, rfft, irfft

ecg = np.array(signals.ECG)

# Define filter parameters
cutoff_freq = 100  # Hz
filter_order = 4
fs = 1000  # Hz

# Create high-pass Butterworth filter
b, a = butter(filter_order, cutoff_freq, btype='highpass', fs=fs)

# Apply filter to ECG signal
filtered_ecg = filtfilt(b, a, ecg)


plt.plot(filtered_ecg)
plt.plot(ecg, 'r-')

# fft_ecg = fft(ecg)
# fft_filtered_ecg = fft(filtered_ecg)

# plt.plot(fft_ecg, 'r-')
# plt.plot(fft_filtered_ecg, 'b')



plt.show()

