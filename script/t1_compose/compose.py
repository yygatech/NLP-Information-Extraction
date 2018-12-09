# Template 1: compose(composer, verb, music, at-time, at-loc)

from script.task4_utils.filter_by_verb import _filter_by_verb

# This is important to unpickle class Sentence.
import sys
from script import sentence
sys.modules['sentence'] = sentence

##################################
# Step 0: select the right synset
# from script.task3_5 import __synsets
# from nltk.corpus import wordnet as wn
#
# # synsets of 'compose'
# compose_synsets = __synsets('compose')
# for i, synset in enumerate(compose_synsets):
#     definition = synset.definition().lower()
#     examples = synset.examples()
#
#     print(synset)
#     print("definition:", definition)
#     print("examples:", examples)
#     print()
#
# # selected synset is 'compose.v.02'
# compose_synset = wn.synset('compose.v.02')
# print("selected synset:", compose_synset)
#
# compose_synonyms = compose_synset.lemma_names()
# print("synonyms:", compose_synonyms)

##################################
# Step 1: filter sentences by verb
sent_dict = _filter_by_verb('compose.v.02')
print("number of filtered sentences:", len(sent_dict))

# PRINT
# for sent_idx in sent_dict:
#     sent = sent_dict[sent_idx]
#     print(sent_idx, sent.sentence)

##################################
# Step 2: