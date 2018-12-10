# Template 1: compose(composer, verb, music, at-time, at-loc)

from nltk.corpus import wordnet as wn

from script.task4_utils.filter_by_verb import _filter_by_verb
from script.task4_utils.pickle_if_not import _pickle_keyword_sents_if_not
from script.task4_utils import filter_by_verb as fs
# from script.task4_utils.pickle_if_not import _pickle_keyword_groves_if_not

# This is important to unpickle class Sentence.
import sys
from script import sentence
sys.modules['sentence'] = sentence

##################################
keyword = "compose"
synset_str = "compose.v.02"

excludes = ['write']
synwords = fs.getCandidateWords(synset_str, excludes)
print('target verbs:', synwords)

##################################
# Step 1: filter sentences by verb

sents = _filter_by_verb(synwords)
print("number of filtered sentences:", len(sents))


# filter those preceed 'of'
def _filter_of(sents):
    from script.task4_utils.get_tree_lemmas import _get_tree_lemmas
    from script.templates.subject import _get_indices_of_synsets

    synonyms = synset.lemma_names()
    # print("synonyms:", synonyms)

    filtered = []
    for sent in sents:

        # get tree lemmas
        lemmas = _get_tree_lemmas(sent)
        lemma_inds = _get_indices_of_synsets(lemmas, synonyms)
        for lemma_ind in lemma_inds:
            curr_word = lemmas[lemma_ind]
            next_word = lemmas[lemma_ind + 1]
            if next_word != "of":
                filtered.append(sent)
                break
    return filtered

# sents = _filter_of(sents)
# print("number of 2nd-round filtered sentences:", len(sents))

# pickle keyword sents if never pickled
sents_pickle = _pickle_keyword_sents_if_not(keyword, sents)
print("Create sents pickle:", sents_pickle)

# get or wrap trees if trees do not exist
# this section below doesn't work!
# error: AttributeError: Can't pickle local object 'DependencyGraph.__init__.<locals>.<lambda>'
# groves_pickle = _pickle_keyword_groves_if_not(keyword, sents)
# print("Create groves pickle:", groves_pickle)

# unpickle groves
# groves = pu._get_groves(keyword)
# print("length of groves", len(groves))

####################################
# sample
# idx = 1
# sentence = sentences[1]
# pos_tag = pos_tags[1]
#
# trees = Trees(sentence, pos_tag)
# ctree = trees.cp
# dtree = trees.dp
# netree = trees.ne
#
# print("print ctree:")
# # ctree.pretty_print()
#
# print("print dtree:")
# # print(dtree.to_conll(4))
#
# print("print ner tree:")
# # print(netree)

######################################
# Step 2: find subject and object
from script.templates import subject as sub
selected_sents = sents[50:60]
subjects_all = sub._subject(synwords, selected_sents)

# TEST PRINT
# for subjects in subjects_all:
#     print(subjects)

objects_all = sub._object(synwords, selected_sents)

# TEST PRINT
# for objects in objects_all:
#     print(objects)

# form triples: v(e1, x1, x2)
for i, sent in enumerate(selected_sents):
    subjects = subjects_all[i]
    objects = objects_all[i]

    x1, e1, x2 = sub._triple(synset, sent, subjects, objects)
    print()
    print(i, "sentence:", sent.sentence)
    print("e1:", e1)
    print("x1:", x1)
    print("x2:", x2)

#### Person and Location
# from script.templates import entity
# persons = entity.extractEnt(sents, 'PERSON')
# print('Person:', persons)
# locations = entity.extractEnt(sents, 'GPE')
# print('Location:', locations)

######################################
# Step 3: extract temporal information
# from script.templates import temporal as time
# time._extract_static_time(sents[100:110])

######################################
# Step 4:
