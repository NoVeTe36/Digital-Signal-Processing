import signals
import numpy as np
import matplotlib.pyplot as plt
import scipy
from scipy.fft import fft, ifft, fftshift, rfft, irfft


#signal in the time domain
x = np.array(signals.Input_1kHz_15kHz)
plt.stem(x)
plt.xlabel('n')
plt.ylabel('Amplitude')
plt.show()


#signal in the frequency domain
X = rfft(x[0:48])
plt.title('Frequency domain signal (real)')
plt.plot(X)
plt.xlabel('Frequency (Hz)')
plt.show()



# Extract real, imaginary, magnitude, and phase components
X_real = X.real
X_imag = X.imag
X_mag = np.abs(X)
X_phase = np.angle(X)


# Plot real component
plt.plot(X_real)
plt.xlabel('Time (s)')
plt.ylabel('Real component')
plt.title('Real component')
plt.show()


# Plot imaginary component
plt.plot(X_imag)
plt.xlabel('Time (s)')
plt.ylabel('Imaginary component')
plt.title('Imaginary component')
plt.show()


# Plot magnitude
plt.plot(X_mag)
plt.xlabel('Time (s)')
plt.ylabel('Magnitude')
plt.title('Magnitude')
plt.show()


# Plot phase
plt.plot(X_phase)
plt.xlabel('Time (s)')
plt.ylabel('Phase (radians)')
plt.title('Phase')
plt.show()


# Plot reconstructed signal
x_recon = irfft(X)
plt.stem(x, label='Original signal')
plt.stem(x_recon, label='Reconstructed signal')
plt.legend()
plt.xlabel('n')
plt.ylabel('Amplitude')
plt.show()


h = np.array(signals.Impulse_response)
plt.stem(h)
plt.xlabel('n')
plt.ylabel('Amplitude')
plt.title('Impulse response')
plt.show()


#signal in the frequency domain
H = rfft(h[0:48])
plt.title('Frequency domain signal (real)')
plt.plot(H)
plt.xlabel('Frequency (Hz)')
plt.show()



# Extract real, imaginary, magnitude, and phase components
H_real = H.real
H_imag = H.imag
H_mag = np.abs(H)
H_phase = np.angle(H)


# Plot real component
plt.plot(H_real)
plt.xlabel('Time (s)')
plt.ylabel('Real component')
plt.title('Real component')
plt.show()


# Plot imaginary component
plt.plot(H_imag)
plt.xlabel('Time (s)')
plt.ylabel('Imaginary component')
plt.title('Imaginary component')
plt.show()


# Plot magnitude
plt.plot(H_mag)
plt.xlabel('Time (s)')
plt.ylabel('Magnitude')
plt.title('Magnitude')
plt.show()


# Plot phase
plt.plot(H_phase)
plt.xlabel('Time (s)')
plt.ylabel('Phase (radians)')
plt.title('Phase')
plt.show()


# calculate convolution
y = np.convolve(x, h)
plt.stem(y)
plt.show()

#signal in the frequency domain
Y = rfft(y)
plt.title('Frequency domain signal (real)')
plt.plot(Y)
plt.xlabel('Frequency (Hz)')
plt.show()



# Extract real, imaginary, magnitude, and phase components
Y_real = Y.real
Y_imag = Y.imag
Y_mag = np.abs(Y)
Y_phase = np.angle(Y)


# Plot real component
plt.plot(Y_real)
plt.xlabel('Time (s)')
plt.ylabel('Real component')
plt.title('Real component')
plt.show()


# Plot imaginary component
plt.plot(Y_imag)
plt.xlabel('Time (s)')
plt.ylabel('Imaginary component')
plt.title('Imaginary component')
plt.show()


# Plot magnitude
plt.plot(Y_mag)
plt.xlabel('Time (s)')
plt.ylabel('Magnitude')
plt.title('Magnitude')
plt.show()


# Plot phase
plt.plot(Y_phase)
plt.xlabel('Time (s)')
plt.ylabel('Phase (radians)')
plt.title('Phase')
plt.show()


# Y_multi = np.multiply(X, np.pad(H, (0, len(X) - len(H)), 'constant'))
# Y_multi_mag = np.abs(Y_multi)
# plt.plot(Y_multi_mag)
# plt.show()


# #calculate the inverse of the Y_multi

# y_multi = irfft(Y_multi)

# plt.stem(y_multi)   

# plt.show()


    