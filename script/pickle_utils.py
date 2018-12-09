import pickle
# import dill
import sys

pickle_dir = sys.path[1] + "/pickle/"

# sentences setter and getter
def _set_sentences(sentences):
    with open(pickle_dir + "sentences.pickle", 'wb') as output:
        pickle.dump(sentences, output)

def _get_sentences():
    with open(pickle_dir + "sentences.pickle", 'rb') as input:
        sentences = pickle.load(input)
    return sentences

# words_all setter and getter
def _set_words_all(words_all):
    with open(pickle_dir + "words_all.pickle", 'wb') as output:
        pickle.dump(words_all, output)

def _get_words_all():
    with open(pickle_dir + "words_all.pickle", 'rb') as input:
        words_all = pickle.load(input)
    return words_all

# pos_tags_all setter and getter
def _set_pos_tags_all(pos_tags_all):
    with open(pickle_dir + "pos_tags_all.pickle", 'wb') as output:
        pickle.dump(pos_tags_all, output)

def _get_pos_tags_all():
    with open(pickle_dir + "pos_tags_all.pickle", 'rb') as input:
        pos_tags_all = pickle.load(input)
    return pos_tags_all

# tags_all setter and getter
def _set_tags_all(tags_all):
    with open(pickle_dir + "tags_all.pickle", 'wb') as output:
        pickle.dump(tags_all, output)

def _get_tags_all():
    with open(pickle_dir + "tags_all.pickle", 'rb') as input:
        tags_all = pickle.load(input)
    return tags_all

# wn_tags_all setter and getter
def _set_wn_tags_all(wn_tags_all):
    with open(pickle_dir + "wn_tags_all.pickle", 'wb') as output:
        pickle.dump(wn_tags_all, output)

def _get_wn_tags_all():
    with open(pickle_dir + "wn_tags_all.pickle", 'rb') as input:
        wn_tags_all = pickle.load(input)
    return wn_tags_all

# lemmas_all setter and getter
def _set_lemmas_all(lemmas_all):
    with open(pickle_dir + "lemmas_all.pickle", 'wb') as output:
        pickle.dump(lemmas_all, output)

def _get_lemmas_all():
    with open(pickle_dir + "lemmas_all.pickle", 'rb') as input:
        lemmas_all = pickle.load(input)
    return lemmas_all

# sents (of custom class) setter and getter
def _set_sents(sents):
    with open(pickle_dir + "sents.pickle", 'wb') as output:
        pickle.dump(sents, output)

def _get_sents():
    with open(pickle_dir + "sents.pickle", 'rb') as input:
        sents = pickle.load(input)
    return sents

# groves setter and getter for a specific keyword
def _set_groves(keyword, groves):
    with open(pickle_dir + keyword + "_groves.pickle", 'wb') as output:
        pickle.dump(groves, output)

def _get_groves(keyword):
    with open(pickle_dir + keyword + "_groves.pickle", 'rb') as input:
        groves = pickle.load(input)
    return groves
