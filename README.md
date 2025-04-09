# Smart IoT Industrial Monitoring and Predictive Maintenance

This repository contains a project for Smart IoT Industrial Monitoring and Predictive Maintenance using an industrial arm. The system collects data from various sensors, processes it, and predicts potential failures through machine learning models. The project involves several microcontrollers and communication protocols to gather and process the data. The key components of the system are:

- **STM32**: Collects data from sensors and runs FreeRTOS.
- **ESP32**: Acts as a communication bridge between the STM32 and Raspberry Pi.
- **Raspberry Pi**: Processes the data, runs machine learning models, and visualizes data.
- **Sensors**: DHT11 (temperature and humidity), MPU6050 (accelerometer and gyroscope), Camera, and IR sensors.

## Table of Contents

- [System Architecture](#system-architecture)
- [Components Used](#components-used)
- [System Workflow](#system-workflow)
- [Communication Protocols](#communication-protocols)
- [Machine Learning Model](#machine-learning-model)
- [Visualizing Data](#visualizing-data)

## System Architecture

The system consists of multiple components working together to monitor and predict failures in the industrial arm. The architecture is distributed, with each component performing specific tasks.

1. **Data Acquisition (STM32 + Sensors)**: The STM32 microcontroller is responsible for acquiring sensor data. Sensors include:
   - **DHT11** for temperature and humidity readings.
   - **MPU6050** for abnormal vibration detection using accelerometer and gyroscope.
   - **Camera** for visual and condition inspection.
   - **IR Sensors** for proximity detection.

   The STM32 is running **FreeRTOS**, which allows it to handle multitasking and manage sensor data acquisition efficiently.

2. **Data Transmission (ESP32)**: The ESP32 microcontroller acts as a communication bridge. It receives the sensor data from the STM32 using serial communication (e.g., UART or SPI) and forwards it to the Raspberry Pi. It also allows the Raspberry Pi to send commands back to the STM32.

3. **Data Processing and ML model implementation (Raspberry Pi 4)**: The Raspberry Pi receives the data from the ESP32, processes it, and runs a machine learning model to predict potential failures. It also visualizes the data and alerts the user about any anomalies or potential issues.

4. **Visualization and Control (Raspberry Pi)**: The data and prediction results are visualized through a web interface running on the Raspberry Pi. The user can monitor sensor data, view failure predictions.

## Components Used

- **STM32 Microcontroller**:
  - Used for data acquisition from sensors.
  - Runs **FreeRTOS** for multitasking.
  
- **ESP32**:
  - Used for communication between STM32 and Raspberry Pi.
  - Supports Wi-Fi for data transmission.

- **Raspberry Pi**:
  - Used for processing and running the machine learning model.
  - Acts as the central hub for visualization and control.
  - Runs the server for displaying real-time sensor data and failure predictions.

- **DHT11 Sensor**:
  - Temperature and humidity sensor used to monitor the arm's conditions.

- **MPU6050 Sensor**:
  - Accelerometer and gyroscope used to monitor if there's any abnormal vibrations occurs on the arm's axis.

- **IR Sensor**:
  - Used for proximity detection.

- **Camera**:
  - Used for visual monitoring and defect detection on the industrial arm.

## System Workflow

### 1. **Sensor Data Collection (STM32 + FreeRTOS)**

- The STM32 microcontroller is responsible for interfacing with the sensors and collecting data.
- FreeRTOS handles multitasking, allowing the STM32 to manage different sensors concurrently.
- The data collected includes temperature, humidity, motion, and possibly visual data from the camera and IR sensors.

### 2. **Data Transmission to ESP32**

- The STM32 sends the collected sensor data to the ESP32 using serial communication (e.g., UART or SPI).
- The ESP32 transmits the data to the Raspberry Pi over a Wi-Fi network using a suitable communication protocol (e.g., MQTT, HTTP, or WebSocket).

### 3. **Data Processing and Failure Prediction (Raspberry Pi)**

- The Raspberry Pi receives the data from the ESP32 and processes it.
- A machine learning model is trained to predict potential failures based on the sensor data.
  - The model may use algorithms such as decision trees, support vector machines (SVM), or neural networks.
  - The model is trained on historical sensor data to recognize patterns that indicate failure.

### 4. **Visualization and Control (Raspberry Pi)**

- The processed data and failure predictions are displayed on a web interface, which is hosted on the Raspberry Pi.
- The user can monitor real-time data, receive alerts for potential failures, and visualize trends.

## Communication Protocols

- **Serial Communication (STM32 to ESP32)**: The STM32 communicates with the ESP32 using a serial protocol like UART or SPI. The STM32 sends sensor data in real-time, which is then forwarded by the ESP32.
  
- **Wi-Fi Communication (ESP32 to Raspberry Pi)**: The ESP32 uses Wi-Fi to transmit sensor data to the Raspberry Pi. Common communication protocols for this step include:
  - **MQTT**: A lightweight messaging protocol used for IoT devices.
  - **HTTP**: The Raspberry Pi can host a simple web server to receive data from the ESP32.
  - **WebSocket**: For real-time communication between the ESP32 and Raspberry Pi.

## Machine Learning Model

The machine learning model is implemented on the Raspberry Pi to predict failures based on sensor data. The model is trained using historical data and works by identifying patterns that precede failures in the industrial arm. 

- The training process involves:
  1. Collecting historical data from the sensors.
  2. Preprocessing the data (e.g., normalization, feature extraction).
  3. Training a machine learning model (e.g., Random Forest, SVM, Neural Network).
  4. Evaluating the model's accuracy and making adjustments.

- The trained model is then used for real-time prediction, where incoming sensor data is fed into the model, and failure predictions are generated.
<img src="Project resources/Predective maintenance.png">

## Visualizing Data

Data visualization is done on the Raspberry Pi via a web interface. The system displays:

- Real-time sensor data.
- Historical trends and data analysis.
- Failure predictions and alerts.
- Graphs and charts for better insight into sensor performance and system status.
