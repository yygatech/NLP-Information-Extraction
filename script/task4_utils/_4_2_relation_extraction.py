## 4.2 Relation Extraction
import re
import nltk

# sent = Sentence(1203)
# print(sent.sentence, "\n")
# print(sent.pos, "\n")

# sample:
IN = re.compile(r'.*\bin\b(?!\b.+ing)')
for doc in nltk.corpus.ieer.parsed_docs('NYT_19980315'):
    for rel in nltk.sem.extract_rels(
            'ORG', 'LOC', doc,
            corpus='ieer', pattern=IN):
        print(nltk.sem.rtuple(rel))
print()

# for r in nltk.sem.extract_rels('ORG', 'LOC', [chunk]):
#     print(nltk.sem.clause(r))