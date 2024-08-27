import os
import wave
import speech_recognition as sr

# Define the path to the audio file
audio_file = 'C:\Users\ishaa\Desktop\speech_to_text\sample_audio'

# Check if the file exists
if not os.path.exists(audio_file):
    print(f"File {audio_file} not found.")
    exit()

# Use "with" statement to ensure that the file is properly closed
with sr.AudioFile(audio_file) as source:
    # Recognize speech using Google Speech Recognition
    recognizer = sr.Recognizer()
    audio_data = recognizer.record(source)
    text = recognizer.recognize_google(audio_data)
    print("Text:", text)
