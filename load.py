from contextlib import redirect_stdout
import func
import sys
import numpy as np
import traceback
from rich.progress import track

object_dict = {}
#pattern_id : best 10 words

wordList = []

file = open('wordsHR.txt', 'r', encoding='utf-8')
for line in file:
    wordList.append(line.replace('\n',''))

pattern_matrixHR = np.zeros((len(wordList), len(wordList)), dtype=np.uint8)

for index1, word in track(enumerate(wordList), description='Radim...', total=len(wordList)):
    for index2, wordP in enumerate(wordList):
        try:
            pattern = func.getPattern(word, wordP)
            pattern_matrixHR[index1, index2] = func.ternary_to_decimal(pattern)
        except Exception:
            print(f'prva: {word} druga: {wordP}')
        except KeyError as e:
            print(f'prva: {word} druga: {wordP}')
            print(func.word_to_num(word))
            print(func.word_to_num(wordP))
            print(traceback.format_exc())
            print(e)
            sys.exit("exit")


print('radim dump')
np.save('patternMatrixHR.npy', pattern_matrixHR)
print('dump gotov')

# dict = {}
# file = open('freqs.txt', 'r')
# for line in file:
#     try:
#         linija = line.replace('\n', '').split(' ')
#         frekv = [float(x) for x in linija[1:]]
#         dict[linija[0]] = (sum(frekv)/len(frekv))
#     except ZeroDivisionError:
#         dict[linija[0]] = 0

# frekv_lista = [value for value in dict.values()]
# suma = sum(frekv_lista)

# for zapis in dict.keys():
#     dict[zapis] = (dict[zapis] / suma)

# file = open('freqs.json', 'w')
# json.dump(dict, file)
