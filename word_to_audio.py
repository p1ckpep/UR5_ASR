import pyttsx3
import time

string="turn up,  20"

engine = pyttsx3.init()

voices = engine.getProperty('voices') 
# print(f'语音声音详细信息：{voices}')

engine.setProperty('voice', 'en') 
# engine.setProperty('voice', voices[2].id)

rate = engine.getProperty('rate')
engine.setProperty('rate', rate-100)

engine.setProperty('volume', 0.7)

# engine.say(string)
engine.save_to_file(string, 'speech1.wav')
time.sleep(1)
engine.runAndWait()
