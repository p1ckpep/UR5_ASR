import speech_recognition as sr
r = sr.Recognizer() 
test = sr.AudioFile("/home/pj/pyaudio_test/speech1.wav")
with test as source:
    audio = r.record(source)
type(audio) 
c=r.recognize_sphinx(audio)     
print(c)