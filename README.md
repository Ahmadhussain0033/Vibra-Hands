# Vibra Hands

## Overview

Vibra Hands is an innovative gesture-based musical interface that allows users to create and manipulate sound using intuitive hand movements and gestures. This glove-based system enables expressive musical performance without the need for traditional instruments, making it ideal for musicians, producers, and experimental artists.

## Features

- **Hand Movement Control** – Move your hands freely to adjust parameters like volume, pitch, and modulation.
- **Gesture-Based Notes** – Specific hand gestures trigger musical notes or chords.
- **Surface Interaction** – Tapping different surfaces influences sound dynamics, such as drum intensity or reverb.
- **Combined Gestures** – Unique gesture combinations unlock advanced sound modulation.
- **Instrument Switching** – Clapping changes between different instruments on the fly.
- **Custom Instrument Controls** – Each instrument type has its own specialized gestures:
  - **Drums:** Taps determine intensity, gestures adjust drum type and sound properties.
  - **Flute:** Hand height controls breath intensity, gestures control hole positions for note selection.

## Implementation Plan

---

### 🔧 Components Used  

| Component | Purpose |
|-----------|---------|
| **IMU (MPU6050 / MPU9250 / BNO055)** | Tracks hand movement, tilt, and speed. |
| **Flex Sensors** | Detects finger bending for gesture recognition. |
| **Force Sensors (FSR402 / Tekscan FlexiForce)** | Measures impact force when the glove hits an object. |
| **Time-of-Flight (VL53L0X) / Ultrasonic Sensor (HC-SR04)** | Tracks height and distance from the starting point (0,0,0). |
| **ESP32 (Microcontroller + Bluetooth/WiFi)** | Processes sensor data and wirelessly transmits it. |
| **Haptic Feedback (DRV2605L + Vibration Motors)** | Provides vibration response for interactions. |
| **Rechargeable Battery (Li-Po / Li-Ion)** | Powers the glove for wireless operation. |

---

## 📡 How It Works  
- The **IMU** continuously tracks the hand's **tilt, rotation, and movement**.  
- The **flex sensors** detect **finger bending** to recognize gestures.  
- The **ToF sensor** helps measure **height** to ensure precise tracking.  
- The **force sensors** detect **impact force** for physical interactions.  
- The **ESP32 microcontroller** processes all sensor data and **transmits it wirelessly**.  
- The **haptic feedback system** provides **vibrations** for responses.  


---

### **Software**

- **Machine Learning Gesture Recognition**
  - Train an AI model to recognize hand movements and gestures.
- **Sound Synthesis Engine**
  - Map gestures to real-time MIDI signals and digital sound processing.
- **Bluetooth/Wireless Connectivity**
  - Enable seamless connection to computers or mobile devices.
- **Customizable Sound Mapping**
  - Allow users to assign gestures to different sounds and effects.

## Future Enhancements

- **Multi-User Collaboration** – Jam with other Vibra Hands users in real time.
- **AI-Assisted Performance** – Smart musical accompaniment based on user gestures.
- Add a mike and other stuff so you can control the volume of mike, pitch, reverb and others with hands and use hands to use voice changer effects and AI voices
- add type of shoes to this as well tho idk how that will work
  
## Contribution & Development

Vibra Hands is an open-source project, and contributions are welcome! If you're interested in helping develop the hardware, software, or gesture-mapping algorithms, feel free to open an issue or submit a pull request.

Stay tuned for updates and releases!

