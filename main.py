import cv2
from deepface import DeepFace
import pywhatkit
import time
import random

# Emotion-to-song mapping with varied choices
EMOTION_SONGS = {
    "happy": [
        "upbeat pop songs playlist", 
        "happy hits 2024", 
        "feel good mood music"
    ],
    "sad": [
        "sad emotional songs playlist", 
        "melancholy piano music", 
        "heartbreak pop songs"
    ],
    "angry": [
        "intense rock songs playlist", 
        "heavy metal workout", 
        "angry rap songs"
    ],
    "neutral": [
        "chill lofi beats playlist", 
        "ambient study music", 
        "coffee shop acoustic vibes"
    ],
    "surprise": [
        "epic surprise movie soundtracks", 
        "mind blowing plot twist music"
    ],
    "fear": [
        "calming relaxation music", 
        "nature sounds for anxiety", 
        "peaceful meditation music"
    ],
}

def main():
    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        print("Error: Could not open webcam.")
        return

    last_played_time = 0 
    cooldown_seconds = 60  
    frame_count = 0 

    # Variables to store the state for our on-screen graphics
    current_emotion = "Detecting..."
    current_song = "None"
    face_region = None

    while True:
        ret, frame = cap.read()
        if not ret:
            print("Error: Failed to grab frame.")
            break

        frame_count += 1
        current_time = time.time()
        
        # Calculate how much time has passed to manage our cooldown
        time_since_last_play = current_time - last_played_time
        is_cooldown = time_since_last_play < cooldown_seconds

        # 1. Analyze emotion every 30 frames
        if frame_count % 30 == 0:
            try:
                result = DeepFace.analyze(
                    frame,
                    enforce_detection=False,
                    actions=['emotion']
                )

                if isinstance(result, list):
                    result = result[0]

                # Save the face coordinates for the bounding box
                if 'region' in result:
                    face_region = result['region']

                dominant_emotion = result.get("dominant_emotion", None)

                if dominant_emotion:
                    current_emotion = dominant_emotion

                    # Only trigger a new song if the cooldown is over
                    if not is_cooldown and dominant_emotion in EMOTION_SONGS:
                        current_song = random.choice(EMOTION_SONGS[dominant_emotion])
                        print(f"Playing random choice: {current_song}")
                        
                        pywhatkit.playonyt(current_song)
                        last_played_time = time.time()

            except Exception as e:
                pass 

        # --- DRAWING ON THE VIDEO FEED ---
        
        # 2. Draw the Bounding Box around the face
        if face_region:
            x, y, w, h = face_region['x'], face_region['y'], face_region['w'], face_region['h']
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

        # 3. Draw the HUD (Heads Up Display) Text
        # Create a black background box so the text is always readable
        cv2.rectangle(frame, (10, 10), (600, 90), (0, 0, 0), -1)

        # Display current emotion
        cv2.putText(frame, f"Emotion: {current_emotion.capitalize()}", (20, 40),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 255, 255), 2)

        # Display current song and cooldown status
        if is_cooldown:
            remaining = int(cooldown_seconds - time_since_last_play)
            status_text = f"Playing: {current_song} (Wait: {remaining}s)"
            color = (0, 255, 255) # Yellow text during cooldown
        else:
            status_text = "Ready to detect new mood!"
            color = (0, 255, 0)   # Green text when ready

        cv2.putText(frame, status_text, (20, 75),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.6, color, 2)

        # Show the final frame
        cv2.imshow("Emotion Player", frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()