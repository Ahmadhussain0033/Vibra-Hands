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

### 📌 Vibra Hands – Components List  

#### 🛠️ Sensors & Electronics  

| **Component** | **Quantity** | **Purpose** |
|--------------|------------|-------------|
| **IMU (BNO086 or MPU6050)** | 1 per glove | Tracks hand motion, acceleration, and tilt. |
| **Force Sensitive Resistor (FSR402/FSR406)** | 6 per glove | Measures pressure on fingers and palm. |
| **Piezo Sensor (LDT0-028K)** | 1 per glove | Detects rapid impacts and vibrations. |
| **Haptic Feedback Motor (Vibration Motor)** | 2 per glove | Provides physical feedback for user actions. |
| **Microcontroller (ESP32 or Arduino Nano 33 BLE)** | 1 per glove | Processes sensor data and sends outputs. |

#### 🔌 Power & Connectivity  

| **Component** | **Quantity** | **Purpose** |
|--------------|------------|-------------|
| **Battery (LiPo 3.7V 1000mAh)** | 1 per glove | Powers the system wirelessly. |
| **Battery Charging Module (TP4056)** | 1 per glove | Enables safe battery charging. |
| **Wireless Module (ESP-NOW / Bluetooth / NRF24L01)** | 1 per glove | Sends data wirelessly to external devices. |

---

## 📌 Summary of What This Setup Can Detect  
✅ **Hand Motion (IMU):** Tracks movement, speed, and tilt.  
✅ **Soft & Hard Presses (FSR):** Detects how much force is applied.  
✅ **Rapid Hits & Vibrations (Piezo Sensor):** Measures impact intensity.  
✅ **Haptic Feedback:** Provides vibration response.  
✅ **Wireless Control:** Sends real-time data over Bluetooth/WiFi.  

---
## **Software**

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

