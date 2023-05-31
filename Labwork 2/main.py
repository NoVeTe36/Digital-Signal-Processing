import numpy as np
import matplotlib.pyplot as plt
import signals
from scipy.signal import freqz, lfilter, firwin, butter, cheby1, bessel

# Load input signal
input_signal = signals.Input_1kHz_15kHz
signal_size = len(input_signal)

# Define filter parameters
fs = 44100  # Sampling frequency
nyq = 0.5 * fs  # Nyquist frequency
fc_low = 5000  # Cutoff frequency for lowpass filter
fc_high = 10000  # Cutoff frequency for highpass filter
order = 100  # Filter order

# Design FIR filters (Bartlett, Hamming, Blackman)
fir_bartlett = firwin(order+1, fc_low/nyq, window='bartlett')
fir_hamming = firwin(order+1, fc_low/nyq, window='hamming')
fir_blackman = firwin(order+1, fc_low/nyq, window='blackman')

# Design IIR filters (Chebyshev, Butterworth, Bessel)
b_cheby1, a_cheby1 = cheby1(order, 1, fc_low/nyq, btype='low')
b_butter, a_butter = butter(order, fc_low/nyq, btype='low')
b_bessel, a_bessel = bessel(order, fc_low/nyq, btype='low')

# Apply FIR filters to input signal
fir_output_bartlett = lfilter(fir_bartlett, 1, input_signal)
fir_output_hamming = lfilter(fir_hamming, 1, input_signal)
fir_output_blackman = lfilter(fir_blackman, 1, input_signal)

# Apply IIR filters to input signal
iir_output_cheby1 = lfilter(b_cheby1, a_cheby1, input_signal)
iir_output_butter = lfilter(b_butter, a_butter, input_signal)
iir_output_bessel = lfilter(b_bessel, a_bessel, input_signal)

# Plot frequency response of filters
w_bartlett, h_bartlett = freqz(fir_bartlett)
w_hamming, h_hamming = freqz(fir_hamming)
w_blackman, h_blackman = freqz(fir_blackman)
w_cheby1, h_cheby1 = freqz(b_cheby1, a_cheby1)
w_butter, h_butter = freqz(b_butter, a_butter)
w_bessel, h_bessel = freqz(b_bessel, a_bessel)

plt.figure()
plt.plot(w_bartlett/np.pi*nyq, abs(h_bartlett), label='Bartlett FIR')
plt.plot(w_hamming/np.pi*nyq, abs(h_hamming), label='Hamming FIR')
plt.plot(w_blackman/np.pi*nyq, abs(h_blackman), label='Blackman FIR')
plt.plot(w_cheby1/np.pi*nyq, abs(h_cheby1), label='Chebyshev IIR')
plt.plot(w_butter/np.pi*nyq, abs(h_butter), label='Butterworth IIR')
plt.plot(w_bessel/np.pi*nyq, abs(h_bessel), label='Bessel IIR')
plt.xlabel('Frequency (Hz)')
plt.ylabel('Magnitude')
plt.title('Frequency response of filters')
plt.legend()
plt.show()
