# task2.py

# function: load corpus
# arguments: corpus path
# return: corpus loaded as a string
def _load_corpus(corpus_path):
    # 2 create a corpus
    # import corpus
    #     corpus_path = "corpus.txt"
    corpus = ""
    with open(corpus_path, 'r') as f:
        for line in f:
            corpus += line.replace('\n', ' ')
    # print(corpus)

    return corpus

# TEST
# corpus = _load_corpus("../data/corpus.txt")
# print("corpus:\n", corpus)