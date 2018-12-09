# task3_3.py

## 3.3
# (this step should be done before 3.2)
# part-of-speech (POS) tag the words
# to extract lemmas as features
# should use word_tokenize before POS tagging

# nltk WordNet Interface:
# http://www.nltk.org/howto/wordnet.html
from nltk.corpus import wordnet as wn

def _pos_tag(words_all):
    from nltk import pos_tag as pt

    n_sent = len(words_all)
    pos_tags_all = [[] for i in range(n_sent)]

    for i, words in enumerate(words_all):
        pos_tags = pt(words)
        pos_tags_all[i] = pos_tags

    return pos_tags_all

def _tag(pos_tags_all):
    n_sent = len(pos_tags_all)
    tags_all = ["" for i in range(n_sent)]
    for i in range(n_sent):
        pos_tags = pos_tags_all[i]
        tags_all[i] = [pos_tag[1] for pos_tag in pos_tags]

    return tags_all

# Penn Treebank tags to WordNet tags
def _penn2wn(penn_tag):

    if penn_tag.startswith('J'):
        return wn.ADJ
    elif penn_tag.startswith('V'):
        return wn.VERB
    elif penn_tag.startswith('N'):
        return wn.NOUN
    elif penn_tag.startswith('R'):
        return wn.ADV
    else:
        return ''

def _wn_tag(pos_tags_all):
    # WordNet (morphy) tags
    tags_all = _tag(pos_tags_all)

    n_sent = len(pos_tags_all)
    wn_tags_all = [[] for i in range(n_sent)]

    for i, tags in enumerate(tags_all):
        wn_tags = [wn.NOUN for j in range(len(tags))]
        for j, tag in enumerate(tags):
            wn_tags[j] = _penn2wn(tag)
        wn_tags_all[i] = wn_tags

    return wn_tags_all