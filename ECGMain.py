import numpy as np
import matplotlib.pyplot as plt

# Function to generate a synthetic ECG signal
def generate_ecg(signal_length=1000, sampling_rate=250):
    # Time in seconds
    t = np.linspace(0, signal_length / sampling_rate, signal_length)

    # ECG signal parameters
    heart_rate = 75  # Beats per minute
    freq = heart_rate / 60  # Frequency in Hz
    # Generate a synthetic ECG signal
    ecg_signal = (
        0.6 * np.sin(2 * np.pi * freq * t) +   # Main sinusoidal wave
        0.3 * np.sin(4 * np.pi * freq * t) +   # Second harmonic
        0.1 * np.random.normal(size=signal_length)  # Random noise
    )

    return t, ecg_signal

# Function to visualize the ECG signal
def plot_ecg(t, ecg_signal):
    plt.figure(figsize=(12, 6))
    plt.plot(t, ecg_signal, color='blue')
    plt.title('ECG Simulation')
    plt.xlabel('Time (s)')
    plt.ylabel('Amplitude')
    plt.grid()
    plt.axhline(0, color='black', lw=0.5, ls='--')
    plt.ylim(-1, 1)  # Limits for the y-axis
    plt.xlim(0, max(t))  # Limits for the x-axis
    plt.show()

# Parameters
signal_length = 1000  # Length of the signal
sampling_rate = 250    # Sampling frequency in Hz

# Generate and visualize the ECG signal
t, ecg_signal = generate_ecg(signal_length, sampling_rate)
plot_ecg(t, ecg_signal)
