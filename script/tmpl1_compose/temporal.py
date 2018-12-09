### 4.3.2 extract static temporal information

# function: extract static time information
def _extract_static_time(idx):
    print("#", idx, sents[idx].sentence, "\n")

    trees = Trees(idx)
    #     print(type(trees.cp))
    # print(type(trees.dp))
    #     print(type(trees.ne))

    #     print(trees.cp)
    # print(trees.dp.to_conll(4))
    #     print(trees.ne)

    tree = trees.cp
    tree_list = []
    rate_list = []

    #     print(tree)

    def _traverse(tree):
        for subtree in tree:
            if type(subtree) == nltk.tree.Tree:
                #                 print(subtree, "\n")
                _traverse(subtree)

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

    _traverse(tree)

    highest_rate = 0
    selected_tree = tree
    for i, cand in enumerate(tree_list):
        if rate_list[i] > highest_rate:
            highest_rate = rate_list[i]
            selected_tree = cand
    #             print(rate_list[i], tree)
    #             print(tree.flatten())
    #             print()

    # return value
    if selected_tree == tree:
        #         print("no temporal information")
        return ""
    else:
        #         print("%", highest_rate, selected_tree)
        return selected_tree.flatten()

#     print("\n")

##################################

from nltk.parse.corenlp import CoreNLPDependencyParser as DP
from nltk.parse.corenlp import CoreNLPParser as CP

import re

selected_inds = range(10)

for selected_idx in selected_inds:
    idx = compose_inds[selected_idx]
    static_time = _extract_static_time(idx)
    if static_time == "":
        print("no temporal information")
    else:
        print(static_time)

    print()