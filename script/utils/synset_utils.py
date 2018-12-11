# This script contains synset-related (or synword-related) utilities.


# function: get indices of synwords in lemmas of a sentence
# parameters: sentence as lemmas, synwords
# return: a list of indices of synwords
def _get_indices_of_synsets(lemmas, synwords):
    lemmas_inds = []
    for lemma_idx, lemma in enumerate(lemmas):
        if lemma in synwords:
            lemmas_inds.append(lemma_idx)
    return lemmas_inds
