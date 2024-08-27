import speech_recognition as sr
from pydub import AudioSegment
import os

# Function to convert MP3 to WAV
def convert_mp3_to_wav(file_path):
    sound = AudioSegment.from_mp3(file_path)
    file_path = file_path.split(".")[0] + ".wav"
    sound.export(file_path, format="wav")
    return file_path

recognizer = sr.Recognizer()

# MP3 file path
mp3_file_path = r"C:\Users\ishaa\Desktop\speech_to_text\sample_audio\long_audio.mp3"
# Convert MP3 to WAV
wav_file_path = convert_mp3_to_wav(mp3_file_path)

''' recording the sound '''

with sr.AudioFile(wav_file_path) as source:
    recorded_audio = recognizer.listen(source)
    print("Done recording")

''' Recognizing the Audio '''
try:
    print("Recognizing the text")
    text = recognizer.recognize_google(
            recorded_audio, 
            language="en-US"
        )
    print("Decoded Text : {}".format(text))

except Exception as ex:
    print(ex)

# Clean up the temporary WAV file
os.remove(wav_file_path)
