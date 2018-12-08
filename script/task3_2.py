# tesk3_2.py

def _lemmatize(words_all, wn_tags_all):
    ## 3.2
    # lemmatize the words to extract lemmas as features
    from nltk.stem import WordNetLemmatizer as LM

    lm = LM()
    n_sent = len(words_all)
    lemmas_all = [[] for i in range(n_sent)]
    for i, words in enumerate(words_all):
        lemmas = ["" for j in range(len(words))]
        for j, word in enumerate(words):
            wn_tag = wn_tags_all[i][j]
            if wn_tag == '':
                lemma = lm.lemmatize(word)
            else:
                lemma = lm.lemmatize(word, wn_tag)
            lemmas[j] = lemma
        lemmas_all[i] = lemmas

    return lemmas_all