# 🎵 RFID-MusicPlayer
**A physical jukebox interface using Raspberry Pi 3B and RFID technology.**

This project bridges the gap between physical media and digital streaming. By using an **MFRC522 RFID Scanner**, you can trigger specific Spotify tracks, albums, or playlists just by tapping a card or key fob. It is optimized for the Raspberry Pi 3B running Legacy Bookworm OS.

## 🚀 Features
* **Physical Control:** Play music via RFID tag scans.
* **Spotify Integration:** Full access to the Spotify library via the Web API.
* **Headless Operation:** Designed to run on a Raspberry Pi 3B without a monitor.
* **Legacy OS Optimized:** Tailored for **Raspberry Pi OS (Legacy Bookworm)** to ensure compatibility with hardware drivers along with needed libraries.

## 🛠️ Hardware Requirements
* **Raspberry Pi 3 Model B**
* **MFRC522 RFID Reader**
* **RFID Tags/Cards** (Mifare 1k)
* **Speaker Output:** (used for the project Jabra Speak 410 or 3.5mm jack)
* **Jumper Wires** (Female-to-Female)

## 💻 Tech Stack
* **Language:** Python version: 3.x
* **Libraries:** * `spotipy` (Spotify Web API wrapper)
    * `mfrc522` (RFID hardware interface)
    * `RPi.GPIO` (GPIO pin management)
* **Music Engine:** Raspotify (librespot)

## 🔧 Setup & Installation

### 1. Spotify Developer Setup
1.  Create an app in the [Spotify Developer Dashboard](https://developer.spotify.com/dashboard/).
2.  Add `http://127.0.0.1:8080` to your **Redirect URIs**. (Note: `localhost` is deprecated as of 2026).
3.  Note your **Client ID** and **Client Secret**.

### 2. Hardware Wiring (MFRC522 to Pi 3B)
| MFRC522 Pin | Pi Pin (Physical) |
| :--- | :--- |
| SDA | 24 |
| SCK | 23 |
| MOSI | 19 |
| MISO | 21 |
| IRQ | None |
| GND | 6, 9, 14, 20, or 25 |
| RST | 22 |
| 3.3V | 1 |

### 3. Installation
```bash
# Clone the repo
git clone [https://github.com/YOUR_USERNAME/RFID-MusicPlayer.git](https://github.com/YOUR_USERNAME/RFID-MusicPlayer.git)
cd RFID-MusicPlayer

# Install dependencies
pip install spotipy mfrc522 RPi.GPIO
