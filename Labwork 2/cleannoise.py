import numpy as np
import matplotlib.pyplot as plt
import soundfile as sf
from scipy.signal import lfilter, freqz, butter, filtfilt

# Load the original audio file
original_audio, sample_rate = sf.read('audio.wav')

# Load the noisy audio file and create noise
noisy_audio, sample_rate = sf.read('noisy_audio.wav')
filter_order = 12
cutoff_frequency = 1200.0
normalized_cutoff_frequency = 2 * cutoff_frequency / sample_rate
b, a = butter(filter_order, normalized_cutoff_frequency, btype='low')

# Apply the filter to the noisy audio data
filtered_audio = filtfilt(b, a, noisy_audio)

output_file = 'filtered_audio.wav'
sf.write(output_file, filtered_audio, sample_rate)

plt.subplot(2, 1, 1)
plt.plot(noisy_audio)
plt.title('Noisy Audio')
plt.xlabel('Sample')
plt.ylabel('Amplitude')

plt.subplot(2, 1, 2)
plt.plot(filtered_audio)
plt.title('Filtered Audio')
plt.xlabel('Sample')
plt.ylabel('Amplitude')

# Adjust subplots to prevent overlap
plt.tight_layout()
plt.show()


# Plot the frequency response for the noise filter 
w, h = freqz(b, a)
plt.plot(w * sample_rate / (2 * np.pi), 20 * np.log10(abs(h)))
plt.xlim(0, 0.5 * sample_rate)
plt.title('Frequency Response')
plt.xlabel('Frequency (Hz)')
plt.ylabel('Gain (dB)')
plt.show()



# Plot the frequency domain of the noisy and filtered signals and the original signal
noisy_audio_freq = np.fft.fft(noisy_audio)
filtered_audio_freq = np.fft.fft(filtered_audio)
original_audio_freq = np.fft.fft(original_audio)
frequencies = np.abs(np.fft.fftfreq(noisy_audio.size, 1.0 / sample_rate))

plt.plot(frequencies, 20 * np.log10(noisy_audio_freq), color='blue', label='Noisy')
plt.title('Noisy Audio')
plt.xlabel('Frequency (Hz)')

plt.plot(frequencies, 20 * np.log10(original_audio_freq), color='red', label='Original')
plt.title('Original Audio')
plt.xlabel('Frequency (Hz)')

plt.plot(frequencies, 20 * np.log10(filtered_audio_freq), color='green' , label='Filtered')
plt.title('Filtered Audio')
plt.xlabel('Frequency (Hz)')

plt.legend()
plt.tight_layout()
plt.show()


