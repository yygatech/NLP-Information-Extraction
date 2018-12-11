
# import module
from script.utils import filters as fr
from script.utils import tree_utils as tu
from script.utils import pickle_utils as pu
from script.templates import sub_object as sub
from script.templates import entity, temporal
from script.templates.information import _gather_info_batch
from script.utils import display as dp

# This is important to unpickle class Sentence.
import sys
from script.classes import sentence
sys.modules['sentence'] = sentence

# templates 4: invent/create(verb, inventor, invention, at-time, at-loc)
####################################################################
# Step 0: preparation
keyword = "invent"
synset_str = "invent.v.01"

synwords = fr.getCandidateWords(synset_str)
print('target verbs:', synwords)

####################################################################
# Step 1: filter sentences
# filter by verb (keyword)
sents = fr.getCandidateSentences(synwords, keyword, synset_str)
print("number of selected sentences:", len(sents))

# TEST: select samples for testing
sample = 20
if sample > len(sents):
    sample = len(sents)

sents = sents[:sample]
print("sample size:", len(sents))

# parse into groves
groves = tu._parse_groves(sents, cp=True, ne=True)
# lemmas_all = tu._grove_to_lemmas(groves)

# pickle keyword sents if never pickled
if_pickled = pu._pickle_keyword_sents_if_not(keyword, sents)
print("create sents pickle:", if_pickled)

# TEST: display before pickled keyword sents and unpickled keyword sents
# print()
# print("before pickled sents:")
# dp._display_sents(sents)
# unpickled_sents = pu._get_keyword_sents(keyword)
# print("unpickled sents:")
# dp._display_sents(unpickled_sents)

# this section below doesn't work!
# pickle keyword groves if never pickled
# error: AttributeError: Can't pickle local object 'DependencyGraph.__init__.<locals>.<lambda>'
# if_groves_pickled = pu._pickle_keyword_groves_if_not(keyword, groves)
# print("create groves pickle:", if_groves_pickled)
# TEST: unpickle groves
# unpickled_groves = pu._get_groves(keyword)
# print("size of groves:", len(unpickled_groves))


####################################################################
# Step 2: extract subject and object (or actor and receiver)
subjects_all = sub._subject_batch(synwords, groves)

# TEST PRINT
# for i, subjects in enumerate(subjects_all):
#     print("subject", i, ":", subjects)

objects_all = sub._object_batch(synwords, groves)

# TEST PRINT
# for i, objects in enumerate(objects_all):
#     print("object", i, ":", objects)

# order subject and object(s)
sub._triple_batch(synwords, groves, subjects_all, objects_all)

# TEST
# print()
# for i, subjects in enumerate(subjects_all):
#     print("sentence", i, ":", sents[i].sentence)
#     print("subject", i, ":", subjects)
#     print("object", i, ":", objects_all[i])
#     print()


####################################################################
# Step 3: extract person, location and time information

# location
from script.templates import geo
locations = geo._getLocation(sents, groves, synwords)
# dp._display_a_list(locations, "location info")


# time
times = temporal._extract_time_batch(sents, groves)

# TEST PRINT
# print()
# print("time info:")
# for i, time in enumerate(times):
#     print(i, sents[i].sentence)
#     print(i, time)
#     print()


####################################################################
# Step 4: gather extracted info
info_batch = _gather_info_batch(keyword, sents, subjects_all, objects_all, times, locations)

# TEST PRINT
print()
print("Filled Template:")
for i, info in enumerate(info_batch):
    print(i)
    for j, key in enumerate(info):
        print(key, "-", info[key])
    print()
