import json
import func
import time
import numpy as np

# print('load matrix')
# pattern_matrix = json.load('patternMatrix.json')

def get_information(word, word_list, original_word_list, pattern_matrix, indices):
    probabilty=0
    entropy=0
    information=0
    word_list_length = len(word_list)
    #formula: sum(p(x)*E(x))=sum(p(x)*(-log2(p(x))))
    word_patterns = np.take(pattern_matrix[original_word_list.index(word)], indices=indices)
    unique, counts = np.unique(word_patterns, return_counts=True)
    information = sum([(num/word_list_length)*-func.safe_log2(num/word_list_length) for num in counts])
    return information

def calculate_suggestion(words_possible, original_word_list, pattern_matrix, freqs):
    information = 0
    score = 0
    quant = []
    result = []
    indices = [index for index, elem in enumerate(original_word_list) if elem in words_possible]
    pattern_matrix
    for word in words_possible:
        t1 = time.time()
        information = get_information(word, words_possible, original_word_list, pattern_matrix, indices)
        #dodaj frekvenciju riječi
        score = information * freqs[word]
        quant = [word, information, freqs[word], score]
        result.append(quant)
        t2 = time.time()
    return sorted(result, key=lambda x : x[3], reverse=True)[:10]
