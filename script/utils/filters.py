# This script contains filtering functions.
# import function
from script.utils import pickle_utils

# import module
from nltk.corpus import wordnet as wn

# import from previous task
from script import task3_1
from script import task3_3

# function: get candidate keywords (synwords)
def getCandidateWords(synset_str, excludes=[]):
    '''
    1. get all words in synset.
    2. get possible words in definition
    3. we may remove 'excludes' from the synset
    :param word:
    :param excludes:
    :return:
    '''

    synset = wn.synset(synset_str)
    print(synset_str, ' ', synset.definition())

    #1. synonyms
    candidates = synset.lemma_names()

    #2. from definition
    # sentences = ["to " + synset.definition()]
    #
    # all_words = task3_1._word_tokenize(sentences)
    # taged_definition = task3_3._pos_tag(all_words)[0]
    # for i in range(1, len(taged_definition)):
    #     word = taged_definition[i][0]
    #     tag = taged_definition[i][1]
    #     if tag.startswith('V'):
    #         candidates.append(word)
    # candidates = list(set(candidates))

    #3. final candidates
    ret = [word for word in candidates if word not in excludes]
    return ret

def getCandidateSentences(synset_synonyms,keyword, label):
    from script.templates import semword
    prekeyword = keyword+".v"  # for key words we only choose verb
    ret = []
    for word in synset_synonyms:
        sents = _filter_by_keyword([word])
        # print('sents:', len(sents))
        for sent in sents:
            sentence = sent.sentence
            meaning = semword.simplified_lesk(word, sentence)

            # print()
            # print(sentence)
            if(word == keyword):
                if str(meaning).__contains__(prekeyword):
                    # print(word, meaning, meaning.definition())
                    ret.append(sent)
            elif str(meaning).__contains__(label):
                print(word, meaning, meaning.definition())
                ret.append(sent)
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
