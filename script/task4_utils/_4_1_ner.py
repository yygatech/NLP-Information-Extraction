## 4.1 Named Entity Recognition (NER)

from .. import sentence
import nltk

sent = sentence(1203)
# print(sent.sentence, "\n")
# print(sent.pos, "\n")

# sample:
# sent = nltk.corpus.treebank.tagged_sents()[22]

ne_chunk = nltk.ne_chunk(sent.pos)
# print(type(chunk))
print(ne_chunk)