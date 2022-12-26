import numpy as np
import json
from rich.progress import track
from rich import print as pprint
import func
import os
import sys
import stats

try:
    first_word = sys.argv[1]
except:
    first_word = 'crate'
    
pattern_matrix = np.load('patternMatrix.npy')

wordList = []

file = open('words.txt', 'r')
for line in file:
    wordList.append(line.replace('\n',''))

ori_word_list = wordList

freq_file = open('freqs.json', 'r')
freqs = json.load(freq_file)

hit_pattern = [2,2,2,2,2]
hit_pattern_num = func.ternary_to_decimal(hit_pattern)

test_set = []

pos_words_file = open('possible_words.txt', 'r')
for line in pos_words_file:
    test_set.append(line.replace('\n', ''))


distribution = [0, 0, 0, 0, 0, 0]
scores=[]
failed={}
counter=0
#testiraj sve
for answer in test_set:
    counter += 1
    guess=''
    answer_index = ori_word_list.index(answer)
    wordList = ori_word_list
    guesses=[]
    pattern=[]
    hit = False
    pattern_num = 0
    pattern_list=[]
    step = 0
    while pattern_num != hit_pattern_num:
        step += 1
        if step > 6:
            failed[answer] = guesses
            scores.append(0)
            break
        if step==1:
            guess = first_word
        else:
            guess = stats.calculate_suggestion(wordList, ori_word_list, pattern_matrix, freqs)[0][0]
        guesses.append(guess)
        pattern_num = pattern_matrix[ori_word_list.index(guess), answer_index]
        pattern = func.decimal_to_ternary(pattern_num)
        pattern_list.append(pattern)
        if pattern_num == hit_pattern_num:
            hit = True
            scores.append(step)
            break
        wordList = func.reduce_words(guess, [int(x) for x in pattern], wordList, pattern_matrix, ori_word_list)
    if hit:
        distribution[step-1] += 1
        message = "\n".join([
            "",
            f'Odgovor: {answer}',
            f'Pokušaji: {guesses}',
            "",
            func.plist_to_emoji(pattern_list),
            "",
            f"Distribucija pokušaja: {distribution}",
            f"Prosječno: {sum(scores)/len(scores)}",
            "",
            f"Progres: {counter}/{len(test_set)}"
        ])
        if answer is not test_set[0]:
            n = len(message) + 1
            print("\r\033[0;0H")
            print(' '*n*5, end='')
            print("\r\033[0;0H")
        else:
            print("\r\033[K\n")
        pprint(message)

print(f'Fejlani: {failed}')