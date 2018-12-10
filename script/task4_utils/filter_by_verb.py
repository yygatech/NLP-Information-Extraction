from nltk.corpus import wordnet as wn

from script import pickle_utils

def getCandidateWords(word, excludes):
    '''
    We don't want to keep all words in synset.
    So, remove 'excludes' from the synset
    :param word:
    :param excludes:
    :return:
    '''
    synset = wn.synset(word)
    synset_synonyms = synset.lemma_names()
    ret = [word for word in synset_synonyms if word not in excludes]

    return ret

# This is important to unpickle class Sentence.
# import sys
# from script import sentence
# sys.modules['sentence'] = sentence

# function: filter sentences by verb snyset
# parameter: verb synset as a string
# return: a dictionary each entry of which contains an index (key) and a sent class (value)
def _filter_by_verb(synset_synonyms):

    # extract sentences that contain the 'synset' verb
    sents = pickle_utils._get_sents()
    filtered_sents = []
    for i, sent in enumerate(sents):
        for synset_synonym in synset_synonyms:
            if synset_synonym in sent.lemmas:
                filtered_sents.append(sent)
                break
    # print("number of sentences containing", synset, ":", len(sent_inds))
    return filtered_sents

# TEST
# synset = 'compose.v.02'
# filtered_inds = _filter_by_verb(synset)
# print(filtered_inds)
