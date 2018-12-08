# task3_5.py

## 3.5
# using WordNet,
# extract hypernymns, hyponyms, meronyms, and holonyms
# as features
# Reference:
# http://www.nltk.org/_modules/nltk/corpus/reader/wordnet.html

# nltk WordNet Interface:
# http://www.nltk.org/howto/wordnet.html
from nltk.corpus import wordnet as wn

# function: get synsets of a word
# argument: a word string
# return: a list of synsets
def __synsets(word):
    return wn.synsets(word)

# function: get hypernymns of a synset
# argument: a synset
# return: a list of synsets
def __hypernymns(synset):
    return synset.hypernyms()

# function: get hyponyms of a synset
# argument: a synset
# return: a list of synsets
def __hyponyms(synset):
    return synset.hyponyms()

# function: get meronyms of a synset
# argument: a synset
# return: a list of synsets
def __meronyms(synset): #part
    return synset.member_holonyms()

# TODO?
# function: get holonyms of a synset
# argument: a synset
# return: a list of synsets
def __holonyms(synset): #whole
    return synset.member_meronyms()

    # TEST
    # for synset in wn.synsets('rice'):
    #     for hypernym in synset.part_holonyms():
    #         print(hypernym)
    # return synset.part_holonyms()

# TEST
# synsets = __synsets('rice')
# synset = synsets[0]
# print("synsets:", synsets, "\n")
#
# hypernyms = __hypernymns(synset)
# print("hypernyms:", hypernyms, "\n")
#
# hyponyms = __hyponyms(synset)
# print("hyponyms:", hyponyms, "\n")
#
# meronyms = __meronyms(synset)
# print("meronyms(being a member of):", meronyms, "\n")
#
# holonyms = __holonyms(synset)
# print("holonyms(having members of):", holonyms, "\n")