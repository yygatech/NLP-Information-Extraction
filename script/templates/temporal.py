# extract static temporal information
# import class
from script.classes.trees import Trees

# import module
import nltk
import re


# function: rate trees (subtrees)
def _traverse(tree, tree_list, rate_list):
    for subtree in tree:
        if type(subtree) == nltk.tree.Tree:
            # print(subtree, "\n")
            _traverse(subtree, tree_list, rate_list)

            subtree_str = str(subtree)
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
def _extract_static_time_single_sentence(trees):
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


def _getPatternTime(sent):
    '''
    Return time(string)
    :param sent:
    :return:
    '''
    from script.templates import repattern as rp
    pps = rp.getPPs([sent])
    ret = []
    for pp in pps:
        pp_list = pp.split(" ")
        prep = pp_list[0]
        rest = " ".join(pp_list[1:])
        # print(pp_list, prep, rest)

        import re
        if re.match(r'[0-9]+', str(rest)) != None:
            ret.append(" ".join(pp_list))
        if(isMatch(prep, rest, getkeyTimeWords(), getkeyTimePrep())):
            ret.append(" ".join(pp_list))

    keyphases = rp.getkeyPhases([sent], getkeyTimePrep())
    for phases in keyphases:
        for phase in phases:
            if (isPhaseMatch(phase, getkeyTimeWords())):
                ret.append(phase)

    return ret


def isPhaseMatch(phase, timewords):

    for t in timewords:
        if phase.lower().__contains__(t):
            return True
    else:
        return False


def isMatch(prep, time, timewords, prepwords):
    for p in prepwords:
        if(prep.lower() == "during"):
            return True
    for t in timewords:
        if time.lower().__contains__(t):
            return True
    return False


def _extract_time(sent, grove):
    '''
    extract time information for one sentence
    :param sent: a sentence
    :return: a list of time information
    '''
    timeInfs = []

    # static time
    static_time = _extract_static_time_single_sentence(grove)
    static_tag = ""
    if static_time != "":
        static_tag = static_time.label()
        # print(static_tag, 'static time', static_time.leaves())
        timeInf1 = " ".join(static_time.leaves())
        timeInfs.append(timeInf1)
    else:
        timeInf1 = ""

    if (static_tag.__contains__('TMP') != True):
        # getTime by Pattern match
        timeInf2 = _getPatternTime(sent)

        for timeInf in timeInf2:
            if (len(timeInf1.split(" ")) > 1 and len(timeInf.split(" ")) > 1):
                s_word1 = timeInf1.split(" ")[0:2]
                s_word2 = timeInf.split(" ")[0:2]
                if (s_word1 != s_word2):
                    timeInfs.append(timeInf)
            else:
                timeInfs.append(timeInf)
    # ?
    # if (len(timeInfs) == 0):
    #     timeInfs.append("")

    # print("time info:", timeInfs)
    return timeInfs

def _extract_time_batch(sents, groves):
    '''
    in batch, extract time information
    :param sents:
    :return: a batch of time information
    '''
    time_batch = []
    for i, sent in enumerate(sents):
        # print("sentence", i, ":", sent.sentence)
        time = _extract_time(sent, groves[i])
        time_batch.append(time)
    return time_batch


def getkeyTimeWords():
    return ["month","years", "ages", "times", "centuries", "century", "later than"]


def getkeyTimePrep():
    return [ "during", "later", "within"]
