from script.trees import Trees
from nltk.stem import WordNetLemmatizer as LM
from nltk.corpus import wordnet as wn


# function: get tree lemmas of a sentence
def _get_tree_lemmas(sent):
    trees = Trees(sent)
    cp = trees.cp
    words = [word for word in cp.leaves()]
    lm = LM()
    lemmas = [lm.lemmatize(word, wn.VERB) for word in words]
    return lemmas
