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

  

| **Component**                                                | **Quantity per Glove**        | **Brand / Model**                       | **Weight (g)**                   | **Dimensions (mm)**                     | **Purpose**                                                                                                  |
|--------------------------------------------------------------|-------------------------------|----------------------------------------|----------------------------------|-----------------------------------------|-------------------------------------------------------------------------------------------------------------|
| **IMU (BNO086)**                                              | 6                             | **Hillcrest Labs BNO086**               | ~1.2 each                        | 15x15x2                                | Tracks hand motion, acceleration, and tilt.                                                                  |
| **TCA9548A I2C Multiplexer**                                  | 1                             | **Texas Instruments TCA9548A**         | ~1.5                              | 20x15x2                                | Manages I2C communication for 6 IMUs with a single SDA/SCL pair.                                             |
| **Piezo Force Sensor (KSY Series)**                           | 6                             | **TDK KSY-15**                          | ~0.5 each                        | 10x10x0.5                              | Measures both **pressure and vibration** on fingers and palm.                                                |
| **Haptic Piezo Motor (Vibration Motor)**                      | 1                             | **Precision Microdrives 304-116**       | ~1.5                              | 8x3                                   | Provides physical feedback for user actions on the palm.                                                     |
| **Microcontroller (ESP32 WROVER)**                                   | 1                             | **ESP32 WROVER**    | ~5                                | 31x18x3                                | Processes sensor data and sends outputs.                                                                    |
| **Flexible LiPo Battery Strips (600mAh each)**                | 3 (parallel connection)       | **LG Chem JH3 Cell Strips**             | ~8 each                          | 60x20x2                                | Provides **1800mAh** total for 3–4 hours of usage.                                                          |
| **Battery Charging Module (TP4056)**                          | 1                             | **TP4056 with USB-C input**             | ~2                                | 25x17x2                                | Safe charging for LiPo strips with **overcharge protection**.                                                |
| **Protection Circuit Module (PCM)**                           | 1                             | **Generic 3.7V 1S PCM (20x8x3 mm)**    | ~1                                | 20x8x3                                 | Prevents **over-discharge, overcurrent, and short circuits** for LiPo strips.                                |

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

