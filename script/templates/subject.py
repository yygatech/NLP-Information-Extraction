# extract subject
import nltk

from script.task4_utils.get_tree_lemmas import _get_tree_lemmas
from script.trees import Trees


# function: get indices of a lemma
def _get_indices_of_synsets(lemmas, synwords):

    # print("synonyms:", synonyms)
    lemmas_inds = []
    for lemma_idx, lemma in enumerate(lemmas):
        if lemma in synwords:
            lemmas_inds.append(lemma_idx)
    return lemmas_inds


######################################
# function: extract subject
def _extract_subject(sent, lemma_idx):
    trees = Trees(sent)
    cp = trees.cp
    #     dp = trees.dp
    #     ne = trees.ne
    #     cp.pretty_print()
    #     print("cp:", cp)
    #     print("dp:", dp.to_conll(4))
    #     print("ne:", ne)

    ptree = nltk.tree.ParentedTree.convert(cp)
    #     print("parented tree:", ptree)

    # leaf_values = ptree.leaves()
    #     print(leaf_values)

    # get path(list of indices) to the lemma node
    tree_location = ptree.leaf_treeposition(lemma_idx)
    #     print("tree location:", tree_location)

    # walk to the lemma node
    node = ptree
    for i in tree_location[:-1]:
        node = node[i]
    #     print("node:", node)

    subject = ""
    while node.parent() is not None:
        if node.parent().label() != 'VP' and node.left_sibling() is not None and node.label() == 'VP':
            subject = node.left_sibling()
            while subject.label() != 'NP' and subject.left_sibling() is not None:
                subject = subject.left_sibling()
            break
        else:
            node = node.parent()

        # print("ascended node:", node, "\n")
        # print("subject:", subject, "\n")

    # return value
    if subject == "":
        return ""
    else:
        return subject.flatten()


# extract all subjects of sentences given a synset
def _subject(synonyms, sents):
    # synonyms = synset.lemma_names()
    # print("synonyms:", synonyms)

    subjects_all = []
    for i, sent in enumerate(sents):
        print(i, ":", sent.sentence)

        lemmas = _get_tree_lemmas(sent)
        lemma_inds = _get_indices_of_synsets(lemmas, synonyms)
        print("lemma_inds:", lemma_inds)

        # may have more than one lemma_idx
        # e.g. lemma_inds = [2, 5]

        subjects = []
        for lemma_idx in lemma_inds:
            subject = _extract_subject(sent, lemma_idx)
            sub = {}
            if subject == "":
                print("no subject found")
            else:
                subject_str = " ".join(subject.leaves())
                print("subject found:", subject_str)
                sub[subject.label()] = subject_str
                subjects.append(sub)

        subjects_all.append(subjects)
        print()
    return subjects_all


######################################
# function: extract object
def _extract_object(sent, lemma_idx):
    trees = Trees(sent)
    cp = trees.cp
    #     dp = trees.dp
    #     ne = trees.ne
    # cp.pretty_print()
    # print("cp:", cp)
    #     print("dp:", dp.to_conll(4))
    #     print("ne:", ne)

    ptree = nltk.tree.ParentedTree.convert(cp)
    # print("parented tree:", ptree)

    # leaf_values = ptree.leaves()
    #     print(leaf_values)

    # get path(list of indices) to the lemma node
    tree_location = ptree.leaf_treeposition(lemma_idx)
    #     print("tree location:", tree_location)

    # walk to the lemma node
    node = ptree
    for i in tree_location[:-1]:
        node = node[i]
        # print("node:", node)

    objects = []

    # get the first direct object
    # print("node:", node.label(), node.flatten())
    while node.parent() is not None and 'V' in node.parent().label():
        while node.right_sibling() is not None:
            node = node.right_sibling()
            # node.pretty_print()
            if node.label() == 'NP':
                break

        # break condition
        if node.label() == 'NP':
            # search in right siblings for all objects
            objects.append(node.flatten())
            while node.right_sibling() is not None and node.right_sibling() == 'NP':
                node = node.right_sibling()
                objects.append(node.flatten())
            break

        node = node.parent()
        # print("node:", node.label())

    # return value
    return objects


# extract all objects of sentences given a synset
def _object(synonyms, sents):
    # synonyms = synset.lemma_names()
    # print("synonyms:", synonyms)

    objects_all = []
    for i, sent in enumerate(sents):
        print(i, ":", sent.sentence)

        lemmas = _get_tree_lemmas(sent)
        lemma_inds = _get_indices_of_synsets(lemmas, synonyms)
        print("lemma_inds:", lemma_inds)

        # may have more than one lemma_idx
        # e.g. lemma_inds = [2, 5]

        objects_sent = []
        for lemma_idx in lemma_inds:
            objects = _extract_object(sent, lemma_idx)
            objects_instance = []
            if len(objects) == 0:
                print("no object found")
            else:
                sum = {}
                for i, object in enumerate(objects):
                    object_str = " ".join(object.leaves())
                    print("object", i, "found:", object_str)
                    sum[object.label()] = object_str

                objects_instance.append(sum)
            objects_sent.append(objects_instance)
        objects_all.append(objects_sent)
        print()

    return objects_all


######################################
def _triple(synwords, sent, subjects, objects):
    print("sentence:", sent.sentence)
    print("subjects:", subjects)
    print("objects:", objects)

    lemmas = _get_tree_lemmas(sent)
    print("lemmas:", lemmas)

    lemma_inds = _get_indices_of_synsets(lemmas, synwords)
    print("lemma_inds:", lemma_inds)

    # may have more than one lemma_idx
    # e.g. lemma_inds = [2, 5]

    e1_lemmas = []
    for i, lemma_idx in enumerate(lemma_inds):
        e1_lemmas.append(lemmas[lemma_idx])
        trees = Trees(sent)
        cp = trees.cp
        # cp.pretty_print()

        ptree = nltk.tree.ParentedTree.convert(cp)
        # print("parented tree:", ptree)

        # leaf_values = ptree.leaves()
        # print(leaf_values)

        # get path(list of indices) to the lemma node
        tree_location = ptree.leaf_treeposition(lemma_idx)
        # print("tree location:", tree_location)

        # walk to the lemma node
        node = ptree
        for i_loc in tree_location[:-1]:
            node = node[i_loc]
            # print("node:", node)

        print("node.label()", node.label())
        print("node.leaves()", node.leaves())

        if node.label() not in ('VBN', 'VBD'):
            continue

        # if lable is 'VBN' or 'VBD'
        prev_idx = lemma_idx - 1
        while prev_idx >= lemma_idx - 2:
            if lemmas[prev_idx] == "be":
                # swap subject and object
                temp = subjects[i]
                subjects[i] = objects[i]
                objects[i] = temp
                print("swapped because", prev_idx, "lemma is:", lemmas[prev_idx])
                break
            prev_idx -= 1
    return subjects, e1_lemmas, objects

######################################
# TEST
# from nltk.corpus import wordnet as wn
#
# from script.pickle_utils import _get_keyword_sents
#
# keyword = "compose"
# synset_str = "compose.v.02"
# synset = wn.synset(synset_str)
# sents = _get_keyword_sents(keyword)[50:55]
# print("finding subject:")
# subjects_all = _subject(synset, sents)
# print("finding object:")
# objects_all = _object(synset, sents)
