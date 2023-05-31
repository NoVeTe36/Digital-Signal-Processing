import numpy as np
import matplotlib.pyplot as plt
import signals
from scipy.fftpack import fft
from scipy import signal
from scipy.signal import freqz

def blackman_filter(signal, num_of_taps):
    # Generate the Blackman window
    window = np.blackman(num_of_taps)

    # Normalize the window
    window /= np.sum(window)

    # Apply the filter using convolution
    filtered_signal = np.convolve(signal, window, mode='same')

    return filtered_signal

def hamming_filter(signal, num_of_taps):
    # Generate the Hamming window
    window = np.hamming(num_of_taps)

    # Normalize the window
    window /= np.sum(window)

    # Apply the filter using convolution
    filtered_signal = np.convolve(signal, window, mode='same')

    return filtered_signal

def bartlett_filter(signal, num_of_taps):
    # Generate the Bartlett window
    window = np.bartlett(num_of_taps)

    # Normalize the window
    window /= np.sum(window)

    # Apply the filter using convolution
    filtered_signal = np.convolve(signal, window, mode='same')

    return filtered_signal

# Generate an example input signal
input_signal = signals.Input_1kHz_15kHz

# Apply the Blackman filter
num_of_black = 51
black_filtered_signal = blackman_filter(input_signal, num_of_black)

# Apply the Hamming filter
num_of_ham = 39
ham_filtered_signal = hamming_filter(input_signal, num_of_ham)

# Apply the Bartlett filter
num_of_bart = 39
bar_filtered_signal = bartlett_filter(input_signal, num_of_bart)

# Plot the frequency response of the filters
w_black, h_black = freqz(np.blackman(num_of_black)/np.sum(np.blackman(num_of_black)), worN=8000)
w_ham, h_ham = freqz(np.hamming(num_of_ham)/np.sum(np.hamming(num_of_ham)), worN=8000)
w_bart, h_bart = freqz(np.bartlett(num_of_bart)/np.sum(np.bartlett(num_of_bart)), worN=8000)

nyq = 0.5 * 10000

plt.figure()
plt.plot(w_black/np.pi*nyq, abs(h_black), label='Blackman')
plt.plot(w_ham/np.pi*nyq, abs(h_ham), label='Hamming')
plt.plot(w_bart/np.pi*nyq, abs(h_bart), label='Bartlett')
plt.legend(loc='upper right')
plt.title('Frequency Response of Filters')
plt.xlabel('Frequency [Hz]')
plt.ylabel('Magnitude [dB]')
plt.grid()
plt.show()

# Plot the input signal and the filtered signals
plt.figure()
plt.plot(input_signal, label='Input Signal')
plt.plot(black_filtered_signal, label='Blackman Filtered Signal')
plt.plot(ham_filtered_signal, label='Hamming Filtered Signal')
plt.plot(bar_filtered_signal, label='Bartlett Filtered Signal')
plt.legend(loc='upper right')
plt.title('Input Signal and Filtered Signals')
plt.xlabel('n')
plt.ylabel('Amplitude')
plt.grid()
plt.show()


fft_x = fft(input_signal)
fft_black = fft(black_filtered_signal)
fft_ham = fft(ham_filtered_signal)
fft_bar = fft(bar_filtered_signal)

plt.figure()
plt.plot(abs(fft_x), label='Input Signal')
plt.plot(abs(fft_black), label='Blackman Filtered Signal')
plt.plot(abs(fft_ham), label='Hamming Filtered Signal')
plt.plot(abs(fft_bar), label='Bartlett Filtered Signal')
plt.legend(loc='upper right')
plt.title('FFT of Input Signal and Filtered Signals')
plt.xlabel('n')
plt.ylabel('Amplitude')
plt.grid()
plt.show()

# Plot the filtered coefficients
plt.figure()
# plt.stem(np.blackman(num_of_black)/np.sum(np.blackman(num_of_black)), label='Blackman')
# plt.stem(np.hamming(num_of_ham)/np.sum(np.hamming(num_of_ham)), label='Hamming')
plt.stem(np.bartlett(num_of_bart)/np.sum(np.bartlett(num_of_bart)), label='Bartlett')
plt.legend(loc='upper right')
plt.title('Filter Coefficients')
plt.xlabel('n')
plt.ylabel('Amplitude')
plt.grid()
plt.show()
