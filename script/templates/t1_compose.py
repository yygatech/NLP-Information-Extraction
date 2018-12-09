# Template 1: compose(composer, verb, music, at-time, at-loc)

from nltk.corpus import wordnet as wn

from script.task4_utils.filter_by_verb import _filter_by_verb

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

# get a list of filtered sentences
sentences = []
pos_tags = []
for i, sent in enumerate(sents):
    sentences.append(sent.sentence)
    pos_tags.append(sent.pos)
    # print(i, ":", sent.sentence)
    # print("pos tag:", sent.pos)

##################################
# Step 2: get or wrap trees if trees not exist

from script.trees import Trees

##################
# this section doesn't work!
# error: AttributeError: Can't pickle local object 'DependencyGraph.__init__.<locals>.<lambda>'
# from pathlib import Path
# from script import pickle_utils as pu
# pickled = Path("pickle/" + keyword + "_groves.pickle")
# if pickled.is_file():
#     print("file exists")
# else:
#     print("file not exists")
#
#     # pickle groves
#     # groves = []
#     # for i, sentence in enumerate(sentences[:10]):
#     #     print("start parsing sentence:", i)
#     #     trees = Trees(sentence, pos_tags[i])
#     #     groves.append(trees)
#     #     print("finish parsing sentence:", i)
#     # pu._set_groves(keyword, groves)
#     # print("finish pickling")
#
# # unpickle groves
# groves = pu._get_groves(keyword)
# print("length of groves", len(groves))
##################

# sample
idx = 1
sentence = sentences[1]
pos_tag = pos_tags[1]

trees = Trees(sentence, pos_tag)
ctree = trees.cp
dtree = trees.dp
netree = trees.ne

print("print ctree:")
# ctree.pretty_print()

print("print dtree:")
# print(dtree.to_conll(4))

print("print ner tree:")
# print(netree)


# find subject
from script.templates import subject as sub
subjects1 = sub._subject(synset, sents[:2])

print('subjects:', subjects1)

# print('key:', synset)
# candidates = subject_dt.extractSubDT(sents, keywords)
# print(candidates)

