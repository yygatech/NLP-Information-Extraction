# task3_1.py

# function: sentence tokenize with filter
# argument: corpus string
# return: tokenized the corpus as sentences
def _filter_sent_tokenize(corpus):
    ### 3.1.1
    # tokenize into sentences
    from nltk.tokenize import sent_tokenize as st

    original_sentences = st(corpus)

    # filter sentences
    sentences = [sentence for sentence in original_sentences if len(sentence) > 5]

    # show sentences
    #     n_sent = len(sentences)
    #     for i in range(3):
    #         print(sentences[i])
    #     print("number of sentences:", n_sent)

    return sentences


# function: word tokenize
# argument: sentences as strings
# return: tokenized sentences as a list of lists of words
def _word_tokenize(sentences):
    ### 3.1.2
    # tokenize into words
    from nltk.tokenize import word_tokenize as wt

    # list of lists of words
    n_sent = len(sentences)
    words_all = [[] for i in range(n_sent)]
    for i, sentence in enumerate(sentences):
        words_all[i] = wt(sentence)

    # show words
    #     for i in range(3):
    #         print(words_all[i])

    return words_all


# function: sentence and word tokenize
# argument: corpus as a string
# return: (sentences, tokenized sentences)
def _task3_1(corpus):
    ## 3.1
    # tokenize the statements into sentences and words
    sentences = _filter_sent_tokenize(corpus)
    words_all = _word_tokenize(sentences)

    return sentences, words_all