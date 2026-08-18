import numpy as np
import pandas as pd

# Set random seed for reproducibility
np.random.seed(42)

# Parameters
n_samples = 2000
sampling_rate = 100  # Hz
duration = n_samples / sampling_rate  # in seconds
timestamps = np.linspace(0, duration, n_samples)

# Helper function to generate acceleration with drift and noise
def generate_sensor_data(base_signal, noise_level=0.2, drift_factor=0.001, failure=False):
    noise = np.random.normal(0, noise_level, size=base_signal.shape)
    drift = np.cumsum(np.random.normal(0, drift_factor, size=base_signal.shape)) if failure else 0
    return base_signal + noise + drift

# Generate base sine/cosine wave signals for normal operation
t = timestamps
base_ax = np.sin(2 * np.pi * 0.5 * t)
base_ay = np.cos(2 * np.pi * 0.5 * t)
base_az = 0.5 * np.sin(2 * np.pi * 0.2 * t)

# Allocate data arrays
data = []

# Simulate 50% normal and 50% failure data
for i in range(n_samples):
    is_failure = 1 if i > n_samples // 2 else 0

    ax1 = generate_sensor_data(np.array([base_ax[i]]), failure=is_failure)[0]
    ay1 = generate_sensor_data(np.array([base_ay[i]]), failure=is_failure)[0]
    az1 = generate_sensor_data(np.array([base_az[i]]), failure=is_failure)[0]

    ax2 = generate_sensor_data(np.array([base_ax[i] * 0.8]), failure=is_failure)[0]
    ay2 = generate_sensor_data(np.array([base_ay[i] * 0.8]), failure=is_failure)[0]
    az2 = generate_sensor_data(np.array([base_az[i] * 0.8]), failure=is_failure)[0]

    temp = 25 + (np.random.normal(0, 0.3)) + (2 if is_failure else 0)  # slight increase in failure

    data.append([t[i], ax1, ay1, az1, ax2, ay2, az2, temp, is_failure])

# Create DataFrame
df = pd.DataFrame(data, columns=[
    "timestamp", "ax1", "ay1", "az1", "ax2", "ay2", "az2", "temperature", "label"
])

# Save to CSV
csv_path = "/mnt/data/robot_arm_mpu6050_dataset_realistic.csv"
df.to_csv(csv_path, index=False)

csv_path
