# Functions display the data structures you want to view in the console.
# import module
from nltk.corpus import wordnet as wn


# function: given a word, display its synsets with definitions and examples
def _display_synsets(keyword):
    print()
    print("keyword:", keyword)
    synsets = wn.synsets(keyword)
    for i, synset in enumerate(synsets):
        definition = synset.definition().lower()
        examples = synset.examples()

        print(i, synset)
        print("definition:", definition)
        print("examples:", examples)
        print()


def _display_sents(sents):
    '''
    display sentences
    :param sents: sentences
    :return: None
    '''
    print()
    print("display sents of size", len(sents))
    for i, sent in enumerate(sents):
        print(i, sent.sentence)
    print()


def _display_a_list(list, name=None):
    '''
    display a list
    :param list:
    :param name:
    :return:
    '''
    print()
    if name is not None:
        print(str(name) + ":")
    for i, item in enumerate(list):
        print(i, item)
        print()