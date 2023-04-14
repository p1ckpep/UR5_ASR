import speech_recognition as sr

def rec(rate=16000):
    r = sr.Recognizer()
    with sr.Microphone(sample_rate=rate) as source:
        print('正在获取声音中...')
        audio = r.listen(source)

    with open("record1.wav", "wb") as f:
        f.write(audio.get_wav_data())
        print('声音获取完成.')

    return 1

if __name__ == '__main__':
    rec()