# This script contains Trees-related utility functions.
# import class
from script.classes.trees import Trees
from nltk.stem import WordNetLemmatizer as Lm

# import module
from nltk.corpus import wordnet as wn


# function: parse trees for one sent
# parameter: sent
# return: parsed trees
def _parse_trees(sent, cp=True, dp=False, ne=False):
    return Trees(sent, cp, dp, ne)


# function: parse trees (groves) for a list of sents
# parameter: sents
# return: parsed groves
def _parse_groves(sents, cp=True, dp=False, ne=False):
    groves = []
    for sent in sents:
        grove = _parse_trees(sent, cp, dp, ne)
        groves.append(grove)
    return groves


# function: grove to tokens
# parameter: grove
# return: tokens (words)
def _grove_to_tokens(grove):
    cp = grove.cp
    words = [word for word in cp.leaves()]
    return words


# function: grove to lemmas
# parameter: grove
# return: lemmas
def _grove_to_lemmas(grove):
    words = _grove_to_tokens(grove)
    lm = Lm()
    # TODO lemmatize according to WordNet tag
    lemmas = [lm.lemmatize(word, wn.VERB) for word in words]
    return lemmas


# function: groves to lemmas_all
# parameter: groves
# return: lemmas_all
def _groves_to_lemmas_all(groves):
    lemmas_all = []
    for grove in groves:
        lemmas = _grove_to_lemmas(grove)
        lemmas_all.append(lemmas)
    return lemmas_all
