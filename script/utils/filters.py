# This script contains filtering functions.
# import function
from script.utils import pickle_utils

# import module
from nltk.corpus import wordnet as wn


# function: get candidate keywords (synwords)
def getCandidateWords(synset_str, excludes):
    '''
    We don't want to keep all words in synset.
    So, remove 'excludes' from the synset
    :param word:
    :param excludes:
    :return:
    '''
    synset = wn.synset(synset_str)
    synset_synonyms = synset.lemma_names()
    ret = [word for word in synset_synonyms if word not in excludes]
    return ret


# function: filter sents by synset verb (keyword)
# parameter: keyword synonyms
# return: filtered sents
def _filter_by_keyword(synset_synonyms):
    # extract sentences that contain the 'synset' verb (keyword)
    sents = pickle_utils._get_sents()
    filtered_sents = []
    for sent in sents:
        for synset_synonym in synset_synonyms:
            if synset_synonym in sent.lemmas:
                filtered_sents.append(sent)
                break
    return filtered_sents


#######################################################################
# template 1
# filter those with 'compose' preceding 'of'
def _filter_of(synwords, sents, groves):
    from script.utils.tree_utils import _grove_to_lemmas
    from script.templates.sub_object import _get_indices_of_synsets

    filtered_sents = []
    filtered_groves = []
    for i, sent in enumerate(sents):
        # get tree lemmas
        lemmas = _grove_to_lemmas(groves[i])
        lemma_inds = _get_indices_of_synsets(lemmas, synwords)
        for lemma_ind in lemma_inds:
            curr_word = lemmas[lemma_ind]
            next_word = lemmas[lemma_ind + 1]
            if next_word != "of":
                filtered_sents.append(sent)
                filtered_groves.append(groves[i])
                break
    return filtered_sents, filtered_groves
