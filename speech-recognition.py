import speech_recognition as sr
AUDIO_FILE = ("sample.wav")
AUDIO_FILE1 = ("sample1.wav")
     
r = sr.Recognizer()

with sr.AudioFile(AUDIO_FILE) as source:
    audio = r.record(source)
    
with sr.AudioFile(AUDIO_FILE1) as source:
    audio1 = r.record(source)
    
try:
    print("audio file sample.wav contains : " + r.recognize_google(audio))
    print("audio file sample1.wav contains : " + r.recognize_google(audio1))
except sr.UnknownValueError:
    print("Google Speech Recognition could not understand audio")
except sr.RequestError:
    print("Couldn't get results from Google Speech Recognition")
