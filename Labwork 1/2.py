import numpy as np
import matplotlib.pyplot as plt
from scipy.fftpack import fft, ifft
import scipy
import signals


x = np.array(signals.Input_1kHz_15kHz)

# Plot signal in time domain
plt.stem(x)
plt.xlabel('Time (s)')
plt.show()

t = np.arange(0, len(x))

# Perform Fourier transform
X = fft(x)

# Extract real, imaginary, magnitude, and phase components
X_real = X.real
X_imag = X.imag
X_mag = np.abs(X)
X_phase = np.angle(X)

# Perform Inverse Fourier transform
x_recon = ifft(X)

# Plot real component
plt.plot(t, X_real)
plt.xlabel('Time (s)')
plt.ylabel('Real component')
plt.show()

# Plot imaginary component
plt.plot(t, X_imag)
plt.xlabel('Time (s)')
plt.ylabel('Imaginary component')
plt.show()

# Plot magnitude
plt.plot(t, X_mag)
plt.xlabel('Time (s)')
plt.ylabel('Magnitude')
plt.show()

# Plot phase
plt.plot(t, X_phase)
plt.xlabel('Time (s)')
plt.ylabel('Phase (radians)')
plt.show()

# Plot reconstructed signal
plt.plot(t, x, label='Original signal')
plt.plot(t, x_recon, label='Reconstructed signal')
plt.legend()
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')
plt.show()