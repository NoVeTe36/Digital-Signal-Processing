import numpy as np
import matplotlib.pyplot as plt
import soundfile as sf

# Load the original audio waveform from a file
audio_data, sample_rate = sf.read('audio.wav')

# Plot the original audio waveform
plt.subplot(2, 1, 1)
plt.plot(audio_data)
plt.title('Original Audio')
plt.xlabel('Sample')
plt.ylabel('Amplitude')

# Generate random noise with the same length as the audio waveform
noise = np.random.normal(0, 0.05, len(audio_data)) # add noise to everywhere
noisy_audio = audio_data + noise

# Save the noisy audio waveform to the output file
output_file = 'noisy_audio.wav'
sf.write(output_file, noisy_audio, sample_rate)

# Plot
plt.subplot(2, 1, 2)
plt.plot(noisy_audio)
plt.title('Noisy Audio')
plt.xlabel('Sample')
plt.ylabel('Amplitude')

# Adjust subplots to prevent overlap
plt.tight_layout()

# Display the plot
plt.show()

# Plot the frequency domain of the original and noisy signals
audio_data_freq = np.fft.fft(audio_data)
noisy_audio_freq = np.fft.fft(noisy_audio)

plt.subplot(2, 1, 1)
plt.plot(abs(audio_data_freq[:len(audio_data_freq) // 2]))
plt.title('Original Audio Frequency')
plt.xlabel('Frequency (Hz)')
plt.ylabel('Magnitude')

plt.subplot(2, 1, 2)
plt.plot(abs(noisy_audio_freq[:len(noisy_audio_freq) // 2]))
plt.title('Noisy Audio Frequency')
plt.xlabel('Frequency (Hz)')
plt.ylabel('Magnitude')

plt.tight_layout()
plt.show()

# Frequency response of the noise filter
