# Template 1: compose(composer, verb, music, at-time, at-loc)

from nltk.corpus import wordnet as wn

from script.task4_utils.filter_by_verb import _filter_by_verb
from script.task4_utils.pickle_if_not import _pickle_keyword_sents_if_not
# from script.task4_utils.pickle_if_not import _pickle_keyword_groves_if_not

# This is important to unpickle class Sentence.
import sys
from script import sentence
sys.modules['sentence'] = sentence

##################################
keyword = "compose"
synset_str = "compose.v.02"

##################################
# Step 1: filter sentences by verb

sents, synset = _filter_by_verb(synset_str)
print("number of filtered sentences:", len(sents))

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
subjects_all = sub._subject(synset, sents[:10])

# TEST PRINT
# for subjects in subjects_all:
#     print(subjects)

objects_all = sub._object(synset, sents[:10])

# TEST PRINT
for objects in objects_all:
    print(objects)

######################################
# Step 3: extract temporal information
# from script.templates import temporal as time
# time._extract_static_time(sents[100:110])

######################################
# Step 4: extract temporal information
