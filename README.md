# Smart IoT Industrial Monitoring Predictive Maintenance
An embedded system for real-time monitoring of industrial equipment, integrating predictive maintenance through anomaly detection.

## Description du Projet
Ce projet vise à concevoir un système IoT industriel simplifié pour la surveillance en temps réel d'équipements industriels, en intégrant un **RTOS (Real-Time Operating System)** pour la gestion des capteurs et un modèle de **Machine Learning (ML)** entraîné dans MATLAB pour la détection d'anomalies. Le système est conçu pour être **évolutif, économe en énergie** et adapté à un environnement académique, avec des ressources matérielles et logicielles limitées.

## Objectifs
1. **Acquisition de données en temps réel** : Lire et synchroniser les données de capteurs hétérogènes (température, vibrations) sur un STM32.
2. **Détection d'anomalies** : Déployer un modèle ML léger pour identifier les signes précoces de défaillance.
3. **Communication IoT** : Transmettre les données et alertes vers un dashboard cloud via un ESP32.
4. **Optimisation énergétique** : Prolonger l'autonomie du système grâce à des stratégies de gestion de l'énergie.

## Architecture du Système

### Composants Matériels
- **Capteurs** :
  - **DHT11** : Capteur de température et humidité (bas coût, basse fréquence).
  - **MPU6050** : Capteur de vibrations et accélération (haute fréquence).
  - **Caméra** : Capteur visuel pour observations de phénomènes.
- **Microcontrôleurs** :
  - **STM32** : Pour l'acquisition des données et l'exécution du modèle ML.
  - **ESP32** : Pour la communication Wi-Fi et l'envoi des données vers le cloud.

### Composants Logiciels
- **RTOS** : FreeRTOS pour la gestion des tâches sur STM32.
- **Machine Learning** : MATLAB pour l'entraînement et la génération de code C du modèle ML.
- **Communication** : MQTT/HTTP pour l'envoi des données vers un dashboard cloud (ex. ThingSpeak).
- **Visualisation** : Dashboard cloud pour le suivi en temps réel des données et des alertes.

## Fonctionnalités Clés

### 1. Gestion des Tâches avec FreeRTOS
- **Tâche haute priorité** : Lecture des vibrations (MPU6050 à 100 Hz).
- **Tâche moyenne priorité** : Lecture de la température (DHT11 à 1 Hz).
- **Tâche basse priorité** : Prétraitement des données (ex. calcul de la moyenne, FFT pour vibrations).

### 2. Modèle de Machine Learning avec MATLAB
- **Entraînement** :
  - Génération d'un dataset synthétique dans MATLAB (températures normales/surchauffe, vibrations normales/défaillance).
  - Utilisation d'un **arbre de décision** ou d'une **régression logique** pour un modèle léger et efficace.
- **Déploiement** :
  - Conversion du modèle en code C avec **MATLAB Coder**.
  - Intégration du modèle dans le firmware STM32 pour une détection d'anomalies embarquée.

### 3. Communication IoT via ESP32
- **Workflow** :
  1. Le STM32 envoie les données prétraitées à l'ESP32 via UART/SPI.
  2. L'ESP32 transmet les données et les prédictions du modèle ML à un dashboard cloud via MQTT (Message Queuing Telemetry Transport).
  3. Alertes en temps réel via LED ou notification cloud.

### 4. Optimisation Énergétique
- **Stratégies** :
  - Mise en veille du STM32 entre les lectures de capteurs.
  - Désactivation du Wi-Fi (ESP32) entre les envois de données.

 ## Références
- [Documentation FreeRTOS](https://www.freertos.org/)
- [MATLAB Coder](https://www.mathworks.com/products/matlab-coder.html)
- [ThingSpeak](https://thingspeak.com/)
- [Arduino ESP32](https://www.arduino.cc/en/Guide/ESP32)



