from speechbrain.pretrained import EncoderDecoderASR
import torch
import torchaudio

def voice_into_word(string):
    # asr_model = EncoderDecoderASR.from_hparams(source="speechbrain/asr-transformer-aishell",
    #                                            savedir="pretrained_models/asr-transformer-aishell")
    asr_model = EncoderDecoderASR.from_hparams(source="speechbrain/asr-wav2vec2-commonvoice-en",
                                               savedir="pretrained_models/asr-wav2vec2-commonvoice-en")

    # audio_1 = r"speech1.wav"
    # ddd = torchaudio.list_audio_backends()
    # print('start...')
    # snt_1, fs = torchaudio.load(audio_1)
    # wav_lens = torch.tensor([1.0])
    # res = asr_model.transcribe_batch(snt_1, wav_lens)
    # # word = res[0][0].replace(' ', '')
    # word = res[0][0]
    # print(word)
    
    print('start...')
    word=asr_model.transcribe_file(string)
    print(word)
    return word

if __name__ == '__main__':
    voice_into_word("speech1.wav")