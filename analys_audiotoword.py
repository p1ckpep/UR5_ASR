from audio_to_word import voice_into_word
import re
import ennumber_to_num as etn

def analys_command(string):
    word = voice_into_word(string)
    split_word = re.split('\W',word)
    num=etn.spoken_word_to_number(split_word[-1])
    # print(split_word)
    if 'UPWARD'or'UP' in split_word:
        direc_of_robot = 'z'
    elif  'DOWN' in split_word:
        direc_of_robot = 'z'
        num = -num
    elif 'LEFT' in split_word:
        direc_of_robot = 'y'
        num = -num
    elif 'RIGHT' in split_word:
        direc_of_robot = 'y'
    elif 'FORWARD' in split_word:
        direc_of_robot = 'x'
    elif 'BACK' in split_word:
        direc_of_robot = 'x'
        num = -num
    file = open('command.txt', 'w')
    print(direc_of_robot+' '+str(num),  file=file)
    file.close()

if __name__ == '__main__':
    analys_command('record1.wav')