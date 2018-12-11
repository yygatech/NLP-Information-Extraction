# extract subject
# import class
from nltk.tree import ParentedTree as Pt
from script.classes.trees import Trees

# import function
from script.utils.tree_utils import _grove_to_lemmas
from script.utils.synset_utils import _get_indices_of_synsets


# function: get a node in a parented tree
# parameter: parented tree, lemma index
# return: parented tree node
def _get_node(ptree, idx):
    # get path (list of indices) to the lemma node
    tree_location = ptree.leaf_treeposition(idx)
    # print("tree location:", tree_location)

    # walk to the lemma node
    node = ptree
    for i in tree_location[:-1]:
        node = node[i]
    #     print("lemma node:", node)
    return node


######################################
# function: extract subject
# parameters: grove, lemma index
# return: flattened tree rooted at lemma
def _extract_subject(trees, lemma_idx):
    cp = trees.cp
    # cp.pretty_print()
    # print("cp:", cp)

    ptree = Pt.convert(cp)
    # print("parented tree:", ptree)

    # leaf_values = ptree.leaves()
    # print("leaf_values:", leaf_values)

    # get lemma node
    node = _get_node(ptree, lemma_idx)

    # start searching for the subject
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
    # print()
    # print(trees.sent.sentence)

    if subject == "":
        return ""
    else:
        # print(subject.flatten())
        return subject.flatten()


# function: extract subject(s) of one sentence
# parameter: synword, grove
# return: a list of subject(s)
def _subject(synwords, grove):
    lemmas = _grove_to_lemmas(grove)
    lemma_inds = _get_indices_of_synsets(lemmas, synwords)

    # lemma_inds may have more than one lemma_idx
    # e.g. lemma_inds = [2, 5]

    subjects = []
    for lemma_idx in lemma_inds:
        # print("lemma", lemmas[lemma_idx], "at index:", lemma_idx)
        subject = _extract_subject(grove, lemma_idx)
        if subject == "":
            subjects.append(subject)
            # print("no subject found")
        else:
            pair = {}
            subject_str = " ".join(subject.leaves())
            # print("subject found:", subject_str)

            subjects.append(subject_str)
            # alternative
            # pair[subject.label()] = subject_str
            # subjects.append(pair)

    return subjects


# function: in batch, extract subject(s) of each sentence
# parameters: synwords, groves
# return: subject(s) of each sentence in batch
def _subject_batch(synwords, groves):
    subjects_batch = []
    for grove in groves:
        subjects = _subject(synwords, grove)

        subjects_batch.append(subjects)
    return subjects_batch


######################################
# function: extract subject
# parameters: grove, lemma index
# return: flattened tree rooted at lemma
def _extract_object(trees, lemma_idx):
    cp = trees.cp
    # cp.pretty_print()
    # print("cp:", cp)

    ptree = Pt.convert(cp)
    # print("parented tree:", ptree)

    # leaf_values = ptree.leaves()
    # print(leaf_values)

    # get lemma node
    node = _get_node(ptree, lemma_idx)

    # start searching for the object(s)
    # may be one or more objects for one verb,
    # so we use a list to collect it/them
    object_list = []

    # get the first direct object
    while node.parent() is not None and 'V' in node.parent().label():
        while node.label() != 'NP' and node.right_sibling() is not None:
            node = node.right_sibling()

        # break condition
        if node.label() == 'NP':
            # search in right siblings for all objects
            object_list.append(node.flatten())
            while node.right_sibling() is not None and node.right_sibling() == 'NP':
                node = node.right_sibling()
                object_list.append(node.flatten())
            break

        # if not break
        node = node.parent()
        # print("node:", node.label())

    # return value
    # print("object_list:", object_list)
    return object_list


# function: extract object(s) of one sentence
# parameter: synword, grove
# return: lists of objects(s)
def _object(synwords, grove):
    lemmas = _grove_to_lemmas(grove)
    lemma_inds = _get_indices_of_synsets(lemmas, synwords)

    # lemma_inds may have more than one lemma_idx
    # e.g. lemma_inds = [2, 5]

    objects = []
    for lemma_idx in lemma_inds:
        # print("lemma", lemmas[lemma_idx], "at index:", lemma_idx)
        object_list = _extract_object(grove, lemma_idx)
        objects_instance = []
        if len(object_list) == 0:
            # print("no object found")
            objects_instance.append(object_list)
        else:

            for i, object in enumerate(object_list):
                pair = {}
                object_str = " ".join(object.leaves())
                # print("object", i, "found:", object_str)

                objects_instance.append(object_str)
                # alternative
                # pair[object.label()] = object_str
                # objects_instance.append(pair)
        objects.append(objects_instance)
    return objects


# function: in batch, extract object(s) of each sentence
# parameters: synwords, groves
# return: object(s) of each sentence in batch
def _object_batch(synwords, groves):
    objects_batch = []
    for grove in groves:
        objects = _object(synwords, grove)
        objects_batch.append(objects)
    return objects_batch


######################################
# function: swap subject and object if passive
# parameters: grove, verb lemma, verb_idx, subject, object_list
# return: (A, B), in which A do B
def _triple_instance(trees, lemmas, lemma_idx, subject, object_list):
    cp = trees.cp
    # cp.pretty_print()

    ptree = Pt.convert(cp)
    # print("parented tree:", ptree)

    # get lemma node
    node = _get_node(ptree, lemma_idx)

    # if label is 'VBN' or 'VBD', look for linking verb 'be' in the previous two lemmas
    if node.label() in ('VBN', 'VBD'):
        for i in range(lemma_idx - 1, lemma_idx - 3, -1):
            if lemmas[i] == "be":
                # print("swapped because", i, "lemma is:", lemmas[i])
                return object_list, subject

    # not possible passive sentence; no swap
    return subject, object_list


# function: check triples in each grove
# parameters: synwords, grove, subjects, objects
def _triple(synwords, grove, subjects, objects):
    # print("subjects:", subjects)
    # print("objects:", objects)
    lemmas = _grove_to_lemmas(grove)
    lemma_inds = _get_indices_of_synsets(lemmas, synwords)

    # may have more than one lemma_idx
    # e.g. lemma_inds = [2, 5]

    # process each triple instance
    for i, lemma_idx in enumerate(lemma_inds):
        # print("lemma", i, ":")
        subjects[i], objects[i] = _triple_instance(grove, lemmas, lemma_idx, subjects[i], objects[i])


# function: check triples for a list of groves
# parameters: synwords, groves, subjects batch, objects batch
def _triple_batch(synwords, groves, subjects_all, objects_all):
    for i, grove in enumerate(groves):
        # print("sentence", i)
        _triple(synwords, grove, subjects_all[i], objects_all[i])
        # print()
