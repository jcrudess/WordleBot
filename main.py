from ast import pattern
from rich import print
from const import YELLOW, GREY, GREEN
import func
import json
import stats
import numpy as np

first_word = 'crane'

pattern_matrix = np.load('patternMatrix.npy')

wordList = []

file = open('words.txt', 'r')
for line in file:
    wordList.append(line.replace('\n',''))

ori_word_list = wordList

freq_file = open('freqs.json', 'r')
freqs = json.load(freq_file)

while len(wordList) > 1:
    #čitaj riječ
    word = input("unesite riječ: ")
    pattern = str(input("unesite dobiveni pattern (oblik - 00120, 0-crno 1-žuto 2-zeleno): "))
    wordList = func.reduce_words(word, [i for i in pattern], wordList, pattern_matrix, ori_word_list)    
    #vrati listu
    if len(wordList) == 1:
        print(f'Pobjeda! Odgovor: {wordList}')
    elif len(wordList) == 0:
        print('Greška!')
    else:
        print(stats.calculate_suggestion(wordList, ori_word_list, pattern_matrix, freqs))






