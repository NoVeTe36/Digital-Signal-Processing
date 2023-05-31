import signals
import numpy as np
import matplotlib.pyplot as plt
import scipy
from scipy.fft import fft, ifft, fftshift, rfft, irfft


class Signals:
    def plot(self, signal):
        #signal in the time domain
        x = np.array(signal)
        plt.stem(x)
        plt.xlabel('n')
        plt.ylabel('Amplitude')
        plt.show()

    def frequency_domain(self, signal_time_domain):
        try:
            #signal in the frequency domain
            X = rfft(signal_time_domain[0:48])
            # add title to the frequency domain
            plt.title('Frequency domain signal (real)')
            plt.plot(X)
            plt.xlabel('Frequency (Hz)')
            plt.show()
        except:
            print("\n******Please plot the signal in the time domain first.******")
            self.plot()

    def real_component(self, X):
        try:
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

        except:
            print("\nPlease plot the signal in the frequency domain first.")
            self.frequency_domain()

class Systems(Signals):
    def __init__(self):
        pass
    def plot(self, signal):
        super().plot(signal)
    def frequency_domain(self, signal_time_domain):
        super().frequency_domain(signal_time_domain)
    def real_component(self, X):
        super().real_component(X)


class Main:
    def main(self):
        print("\nChoose one of the following options:")
        print("1. Plotting")
        print("2. Plot signal in frequency domain")
        print("3. Plot real component, imaginary component, magnitude, and phase")
        print("4. Plot reconstructed signal")
        print("9. Exit")
        choice = int(input("\nEnter your choice: "))
        if choice == 1:
            print("\nChoose one of the following signals:")
            print("1. Input_1kHz_15kHz")
            print("2. Impulse_response")

            signal_choice = int(input("\nEnter your choice: "))
            if signal_choice == 1:
                Signals.plot(signals.Input_1kHz_15kHz)
            elif signal_choice == 2:
                Systems.plot(signals.Impulse_response)
        elif choice == 2:
            signal_choice = int(input("\nEnter your choice: "))
            if signal_choice == 1:
                Signals.frequency_domain(signals.Input_1kHz_15kHz)
            elif signal_choice == 2:
                Systems.frequency_domain(signals.Impulse_response)
        elif choice == 3:
            signal_choice = int(input("\nEnter your choice: "))
            if signal_choice == 1:
                Signals.real_component(signals.Input_1kHz_15kHz)
            elif signal_choice == 2:
                Systems.real_component(signals.Impulse_response)
        elif choice == 4:
            signal_choice = int(input("\nEnter your choice: "))
            if signal_choice == 1:
                Signals.real_component(signals.Input_1kHz_15kHz)
            elif signal_choice == 2:
                Systems.real_component(signals.Impulse_response)
        elif choice == 9:
            exit()
        else:
            print("\nInvalid choice. Please try again.")
            self.main()

while True:
    display = Main()
    display.main()