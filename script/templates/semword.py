'''
Disambiguate the sense of word.

'''

import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import wordnet as wn
from nltk.corpus import stopwords


def simplified_lesk(target, sentence):
    maximum = 0
    maxsense = ""
    stop_words = stopwords.words('english')
    s_list = [token.lower() for token in word_tokenize(sentence)]

    sets = wn.synsets(target)
    # print(len(sets))
    max_n = 0
    for i in range(len(sets)):  # first ten senses
        # print('0. Word sense '+str(i))
        overlap = []

        # print('1. Obtain gloss and examples')
        # item = target + '.v.' + str(i)
        bank = sets[i]
        # gloss
        gloss = word_tokenize(bank.definition())
        # examples
        examples = []
        es = [word_tokenize(example) for example in bank.examples()]
        for word_list in es:
            for word in word_list:
                examples.append(word.lower())

        # print('2. Overlap')
        for token in s_list:
            if token in examples:
                overlap.append(token)
            if token in gloss:
                overlap.append(token)

        # print('3. check stopwords and tareget in Overlap')
        for word in overlap:
            if word in stop_words:
                while word in overlap:
                    overlap.remove(word)

        if target in overlap:
            while target in overlap:
                overlap.remove(target)
        # print('4. maximum')
        if len(overlap) > maximum:
            max_n = i
            maximum = len(overlap)
            maxsense = gloss
        # print('Overlap for sense', i, 'is', overlap)

    chosen_sense = " ".join(maxsense)
    # print()
    # print('The final chosen sense:', max_n, '\n', chosen_sense)
    return sets[max_n]
