# pip install scikit-learn joblib numpy pandas scipy

from joblib import load
import numpy as np
import pandas as pd
import time

# Load the model (expects 7 features)
model = load('rf_model.joblib')

# Buffers
buffer_ax1, buffer_ay1, buffer_az1 = [], [], []
buffer_ax2, buffer_ay2, buffer_az2 = [], [], []
buffer_temp = []

window_size = 100
step_size = 50

def collect_sample():
    # Read data from MPU6050 sensors (mocked with random values)
    ax1, ay1, az1 = read_mpu6050_sensor_1()
    ax2, ay2, az2 = read_mpu6050_sensor_2()
    temp = read_temperature()
    
    # Append to buffers
    buffer_ax1.append(ax1)
    buffer_ay1.append(ay1)
    buffer_az1.append(az1)
    buffer_ax2.append(ax2)
    buffer_ay2.append(ay2)
    buffer_az2.append(az2)
    buffer_temp.append(temp)

    if len(buffer_ax1) == window_size:
        # Create DataFrame for convenience
        window = pd.DataFrame({
            'ax1': buffer_ax1,
            'ay1': buffer_ay1,
            'az1': buffer_az1,
            'ax2': buffer_ax2,
            'ay2': buffer_ay2,
            'az2': buffer_az2,
            'temp': buffer_temp,
        })

        features = extract_features(window)

        # Predict using the model
        prediction = model.predict([features])[0]
        print("Prediction:", prediction)

        # Slide window
        del buffer_ax1[:step_size]
        del buffer_ay1[:step_size]
        del buffer_az1[:step_size]
        del buffer_ax2[:step_size]
        del buffer_ay2[:step_size]
        del buffer_az2[:step_size]
        del buffer_temp[:step_size]

def extract_features(window):
    # Match exactly the 7 features used during training
    features = {
        'ax1_mean': np.mean(window['ax1']),
        'ay1_mean': np.mean(window['ay1']),
        'az1_mean': np.mean(window['az1']),
        'ax2_mean': np.mean(window['ax2']),
        'ay2_mean': np.mean(window['ay2']),
        'az2_mean': np.mean(window['az2']),
        'temp_mean': np.mean(window['temp']),
    }
    return pd.Series(features)

# === Fake sensor data generators ===

def read_mpu6050_sensor_1():
    # Return random acceleration values in ±2g range
    return np.random.uniform(-2, 2), np.random.uniform(-2, 2), np.random.uniform(-2, 2)

def read_mpu6050_sensor_2():
    return np.random.uniform(-2, 2), np.random.uniform(-2, 2), np.random.uniform(-2, 2)

def read_temperature():
    # Return realistic random temperature (°C)
    return np.random.uniform(20, 40)

# === Simulate real-time loop ===
if __name__ == "__main__":
    while True:
        collect_sample()
        time.sleep(0.01)  # Simulate ~100 Hz sampling rate
