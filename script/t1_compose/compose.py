## 4.3 compose
### 4.3.1 extract sentences that have a 'compose' theme
##################################
# count number of sentences
n_sent = len(sentences)
print("numer of sentences:", l, "\n")

# get all sentence objects
sents = []
for i in range(n_sent):
    sent = Sentence(i)
    sents.append(sent)

##################################
# find out the right synset
# synsets of 'compose'
compose_synsets = __synsets('compose')
for i, synset in enumerate(compose_synsets):
#     print(synset)
    definition = synset.definition().lower()
    examples = synset.examples()
#     print("definition:", definition)
#     print("examples:", examples)
#     print()
# our synset is 'compose.v.02'
compose_synset = wn.synset('compose.v.02')
# print(compose_synset)

compose_synonyms = compose_synset.lemma_names()
print(compose_synonyms, "\n")

##################################
# extract sentences that have a 'compose' theme
compose_inds = []
for i, sent in enumerate(sents):
    for compose in compose_synonyms:
        if compose in sent.lemmas:
            compose_inds.append(i)
            break
print("number of sentences containing 'compose'", len(compose_inds))

for i, compose_idx in enumerate(compose_inds):
    sent = sents[compose_idx]
    print(i, sent.sentence)
    print()