# extract static temporal information

import nltk
import re

from script.trees import Trees

def _traverse(tree, tree_list, rate_list):
    for subtree in tree:
        if type(subtree) == nltk.tree.Tree:
            # print(subtree, "\n")
            _traverse(subtree, tree_list, rate_list)

            subtree_str = str(subtree);
            rate = 0
            if "TMP" in str(subtree.label()):
                rate += 100
            if subtree.label() == "PP":
                rate += 10
            if "PP" in subtree_str[3:]:
                rate -= 20
            if "VP" in subtree_str:
                rate -= 100
            if "for" in subtree_str:
                rate -= 30
            if re.match(r'.*\b\d{4}\b.*', subtree_str) != None:
                rate += 20
            if re.match(r'.*\b\d{4}\b\ *((B.C\.)|(BC)|(A\.D\.)|(AD)).*', subtree_str) != None:
                rate += 100
            if "CD" not in subtree_str:
                rate -= 10
            if "NNS" not in subtree_str:
                rate -= 10

            if rate > 0:
                tree_list.append(subtree)
                rate_list.append(rate)


# function: extract static time information
def _extract_static_time_single_sentence(sent):
    trees = Trees(sent)
    tree = trees.cp
    # print("tree:\n", tree)
    tree_list = []
    rate_list = []

    _traverse(tree, tree_list, rate_list)

    highest_rate = 0
    selected_tree = tree
    for i, cand in enumerate(tree_list):
        if rate_list[i] > highest_rate:
            highest_rate = rate_list[i]
            selected_tree = cand
            # print(rate_list[i], tree)
            # print(tree.flatten())
            # print()

    # return value
    if selected_tree == tree:
        # print("no temporal information")
        return ""
    else:
        # print("%", highest_rate, selected_tree)
        return selected_tree.flatten()


def _extract_static_time(sents):
    for i, sent in enumerate(sents):
        print(i, ":", sent.sentence)
        static_time = _extract_static_time_single_sentence(sent)

        if static_time == "":
            print("no static time information")
        else:
            print("static time:", static_time)
        print()

def getTimeInf(sents):
    _extract_static_time(sents)
