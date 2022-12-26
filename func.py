from math import log2
from const import YELLOW, GREEN, GREY, SPEC_SLOVA
import numpy as np
from rich import print

def safe_log2(x):
    return log2(x) if x > 0 else 0

def dekodiraj(word):
    return word.replace('lj', SPEC_SLOVA['lj']).replace('nj', SPEC_SLOVA['nj']).replace('dž', SPEC_SLOVA['dž'])

def word_to_num(word):
    w_num = []
    for index, i in enumerate(dekodiraj(word)):
        w_num.append(ord(i))
    return w_num


def getPattern(word, targetWord):
    result = [0, 0, 0, 0, 0]
    w_num = word_to_num(word)
    tw_num = word_to_num(targetWord)
    w2 = np.asarray(tw_num, dtype=np.uint16)
    unique, counts = np.unique(w2, return_counts=True)
    if word == 'anđeo' and targetWord == 'anđeo':
        print(unique)
        print(counts)
    freq = dict(zip(unique, counts))
    #prvo riješi zelene i sive
    for index, elem in enumerate(w_num):
        if elem not in tw_num:
            continue
        elif tw_num[index] == elem:
            result[index] = 2
            freq[elem] -= 1
        else:
            None
    #još jedna petlja za žute
    for index, elem in enumerate(w_num):
        if elem in tw_num and freq[elem] > 0 and result[index] == 0:
            result[index] = 1
            freq[elem] -= 1
    return result

def getEmojiPattern(pattern):
    result = ''
    for i in pattern:
        if i == 0:
            result += GREY
        elif i == 2:
            result += GREEN
        else:
            result += YELLOW
    return result

def plist_to_emoji(pattern_list):
    result = ''
    for i in pattern_list:
        result += getEmojiPattern(i)+'\n'
    result += (6 - len(pattern_list))*'\n'
    return result

def ternary_to_decimal(number):
    #lista u obliku [0, 0, 1, 2, 0], konvertiraj u decimalni broj
    result=0
    if not number:
        return 0
    for num, elem in enumerate(number):
        result+=int(elem)*3**(4 - num)
    return result

def decimal_to_ternary(number):
    #broj pretvoriti u listu znamenaka human readable
    if number==0:
        return [0, 0, 0, 0, 0]
    nums = []
    while number:
        number, rem = divmod(number, 3)
        nums.append(rem)
    if len(nums) < 5:
        nums+=[0]*(5-len(nums))
    return list(reversed(nums))

def reduce_words(word, pattern, list, pm, owl, print_list=0):
    # w_num = word_to_num(word)
    # for index, letter in enumerate(w_num):
    #     pattern_value = pattern[index]
    #     if pattern_value == 0:
    #         list = [wordL for wordL in list if letter not in word_to_num(wordL)]
    #     elif pattern_value == 1:
    #         list = [wordL for wordL in list if letter in word_to_num(wordL) and letter != word_to_num(wordL)[index]]
    #     else:
    #         list = [wordL for wordL in list if letter == word_to_num(wordL)[index]]
    #     if print_list == 1:
    #         print(list)
    oword_arr = np.array(owl)
    word_arr = np.array(list)
    word_index = np.where(oword_arr == word)[0][0]
    pattern_num = ternary_to_decimal(pattern)
    pattern_row = pm[word_index]
    index_list = np.where(pattern_row == pattern_num)[0].tolist()
    result_arr = oword_arr[index_list]
    return result_arr[np.in1d(result_arr, word_arr)]
    



    if print_list == 1:
        print(list)
    return list


