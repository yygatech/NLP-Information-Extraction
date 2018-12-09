# task3.py
# How to install and use nltk?
# https://www.nltk.org/install.html

# How to download nltk data?
# https://www.nltk.org/data.html
# command line $ python3
# python3 >> import nltk
# python3 >> nltk.download()
# download directory: /usr/local/share/nltk_data
# download what you will need

import pickle

import task2
import task3_1
import task3_3
import task3_2
import task3_4
import task3_5

# load corpus
corpus = task2._load_corpus("../data/corpus.txt")

## 3.1
sentences, words_all = task3_1._task3_1(corpus)

with open(r'../pickle/sentences.pickle', 'wb') as output:
    pickle.dump(sentences, output)

with open(r'../pickle/words_all.pickle', 'wb') as output:
    pickle.dump(words_all, output)

# TEST
# print("sentences")
# print(sentences[1:2])

# print("words_all")
# print(words_all[1:2])

## 3.3
pos_tags_all = task3_3._pos_tag(words_all)

with open(r'../pickle/pos_tags_all.pickle', 'wb') as output:
    pickle.dump(pos_tags_all, output)

# TEST
# print("pos_tags_all")
# print(pos_tags_all[1:2])

wn_tags_all = task3_3._wn_tag(pos_tags_all)

with open(r'../pickle/wn_tags_all.pickle', 'wb') as output:
    pickle.dump(wn_tags_all, output)

# TEST
# print("wn_tags_all")
# print(wn_tags_all[1:2])

## 3.2
lemmas_all = task3_2._lemmatize(words_all, wn_tags_all)

with open(r'../pickle/lemmas_all.pickle', 'wb') as output:
    pickle.dump(lemmas_all, output)

# TEST
# print("lemmas_all")
# print(lemmas_all[1:2])

## 3.4
# dep_trees = task3_4._dependency_parse(sentences[5:7])

# TEST
# for i, dep_tree in enumerate(dep_trees):
#     print("dep_tree", i, ":")
#     print(dep_tree.to_conll(4))

# parse_trees = task3_4._parse(sentences[5:7])

# TEST
# for i, parse_tree in enumerate(parse_trees):
#     print("parse_tree", i, ":")
#     parse_tree.pretty_print()

## 3.5
# synsets = task3_5.__synsets("canis")
# synset = synsets[0]
# hypernyms = task3_5.__hypernymns(synset)
# hyponyms = task3_5.__hyponyms(synset)
# meronyms = task3_5.__meronyms(synset)
# holonyms = task3_5.__holonyms(synset)

# TEST
# print("synsets:", synsets, "\n")
# print("hypernyms:", hypernyms, "\n")
# print("hyponyms:", hyponyms, "\n")
# print("meronyms(being a member of):", meronyms, "\n")
# print("holonyms(having members of):", holonyms, "\n")