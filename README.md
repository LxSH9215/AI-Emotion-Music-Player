# 🎵 Emotion-Based Music Player

A real-time Computer Vision application that detects your facial emotion through a webcam and automatically plays a corresponding YouTube song or playlist to match your mood.

Built with **OpenCV** and **DeepFace**, the system analyzes your expression every 30 frames, maps the dominant emotion (e.g., *Happy*, *Sad*, *Angry*) to a curated set of YouTube search queries, and opens a relevant result in your browser — all hands-free.

---

## 📸 How It Works

```
Webcam Feed ──▶ Face Detection ──▶ Emotion Analysis ──▶ Mood Mapping ──▶ YouTube Playback
                 (OpenCV)           (DeepFace)           (Dictionary)     (pywhatkit)
```

1. The webcam captures live video frames.
2. Every **30 frames**, DeepFace analyzes the frame for the dominant emotion.
3. The detected emotion is mapped to a list of YouTube search queries (e.g., `happy` → *"upbeat pop songs playlist"*).
4. A **random** query is selected and played via `pywhatkit.playonyt()`.
5. A **60-second cooldown** prevents repeated browser tabs from opening.

---

## ✨ Key Features

| Feature | Description |
|---|---|
| **Real-Time Emotion Detection** | Analyzes facial expressions every 30 frames using DeepFace's pre-trained models. |
| **6 Supported Emotions** | Happy, Sad, Angry, Neutral, Surprise, and Fear — each mapped to curated playlists. |
| **Random Song Selection** | Picks a random search query from each emotion's list for variety on every trigger. |
| **60-Second Cooldown Timer** | Prevents multiple browser tabs from opening in quick succession. |
| **On-Screen HUD** | Displays the current emotion, now-playing song, and a live cooldown countdown directly on the video feed. |
| **Face Bounding Box** | Draws a green rectangle around the detected face in real time. |

---

## 🛠️ Tech Stack

| Technology | Role |
|---|---|
| [Python 3.9+](https://www.python.org/) | Core programming language |
| [OpenCV](https://opencv.org/) | Webcam capture, frame processing, and on-screen rendering |
| [DeepFace](https://github.com/serengil/deepface) | Facial emotion analysis (wraps TensorFlow/Keras models) |
| [TensorFlow / tf-keras](https://www.tensorflow.org/) | Backend for DeepFace's deep learning models |
| [pywhatkit](https://github.com/Ankit404butFound/PyWhatKit) | Opens YouTube search results in the default browser |

---

## 📋 Prerequisites

Before you begin, ensure you have the following:

- **Python 3.9 or higher** — [Download here](https://www.python.org/downloads/)
- **A working webcam** (built-in or external USB)
- **An active internet connection** (required for YouTube playback and first-run model downloads)
- **pip** (included with Python 3.9+)

---

## 🚀 Installation

Follow these steps to set up the project on your local machine.

### 1. Clone the Repository

```bash
git clone https://github.com/<your-username>/emotion-music-player.git
cd emotion-music-player
```

### 2. Create a Virtual Environment

```bash
python -m venv .venv
```

### 3. Activate the Virtual Environment

**Windows (PowerShell):**
```powershell
.venv\Scripts\Activate.ps1
```

**Windows (Command Prompt):**
```cmd
.venv\Scripts\activate.bat
```

**macOS / Linux:**
```bash
source .venv/bin/activate
```

### 4. Install Dependencies

```bash
pip install opencv-python deepface tf-keras pywhatkit
```

> **Note:** On the first run, DeepFace will automatically download the required emotion detection model (~10 MB). This is a one-time download.

---

## ▶️ Execution

### Run the Application

```bash
python main.py
```

### What to Expect

1. Your webcam feed will open in a window titled **"Emotion Player"**.
2. A **black HUD bar** at the top displays your detected emotion and playback status.
3. A **green bounding box** will appear around your face.
4. Once an emotion is detected, a YouTube song matching your mood will open in your default browser.
5. The HUD will show a **yellow countdown timer** during the 60-second cooldown period.
6. After the cooldown, the system is ready to detect a new mood and play another song.

### Exit the Application

Press the **`q`** key while the OpenCV window is focused to quit.

---

## 🎭 Emotion-to-Music Mapping

| Emotion | Example YouTube Searches |
|---|---|
| 😄 **Happy** | *"upbeat pop songs playlist"*, *"happy hits 2024"*, *"feel good mood music"* |
| 😢 **Sad** | *"sad emotional songs playlist"*, *"melancholy piano music"*, *"heartbreak pop songs"* |
| 😠 **Angry** | *"intense rock songs playlist"*, *"heavy metal workout"*, *"angry rap songs"* |
| 😐 **Neutral** | *"chill lofi beats playlist"*, *"ambient study music"*, *"coffee shop acoustic vibes"* |
| 😲 **Surprise** | *"epic surprise movie soundtracks"*, *"mind blowing plot twist music"* |
| 😨 **Fear** | *"calming relaxation music"*, *"nature sounds for anxiety"*, *"peaceful meditation music"* |

---

## 📁 Project Structure

```
emotion-music-player/
├── .venv/                # Virtual environment (not committed)
├── main.py               # Main application entry point
├── test_run.py           # Standalone test script for DeepFace analysis
├── requirements.txt      # Python dependencies
└── README.md             # Project documentation
```

---

## ⚙️ Configuration

You can easily customize the application by editing `main.py`:

| Parameter | Default | Description |
|---|---|---|
| `cooldown_seconds` | `60` | Time (in seconds) between consecutive song triggers |
| `frame_count % 30` | `30` | Number of frames between each emotion analysis |
| `EMOTION_SONGS` | See mapping above | Dictionary of emotions → YouTube search queries |

---

## 🐛 Troubleshooting

| Issue | Solution |
|---|---|
| `Could not open webcam` | Ensure your webcam is connected and not in use by another application. |
| Model download fails | Check your internet connection. DeepFace downloads models on first use. |
| Multiple browser tabs opening | This is prevented by the 60-second cooldown. If it persists, increase `cooldown_seconds`. |
| `ModuleNotFoundError` | Ensure the virtual environment is activated and all dependencies are installed. |

---

## 📄 License

This project is for educational and demonstration purposes.
