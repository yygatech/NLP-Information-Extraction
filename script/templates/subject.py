# extract subject
from script.trees import Trees
import nltk

# function: get indices of a lemma
def _get_indices_of_synsets(sent, compose_synonyms):
    lemmas_inds = []
    for lemma_idx, lemma in enumerate(sent.lemmas):
        if lemma in compose_synonyms:
            lemmas_inds.append(lemma_idx)
    return lemmas_inds

######################################
# function: extract subject
def _extract_subject(sent, lemma_idx):
    verb = sent.tokens[lemma_idx]
    # print("verb at", lemma_idx, ":", verb)

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

    # (outdated version)
    #     while node.parent() != None:
    #         if node.parent().label() == 'S':
    #             if node.left_sibling() != None:
    #                 subject = node.left_sibling()
    #                 break
    #             else:
    #                 while node.parent() != None:
    #                     if node.parent().label() != 'NP' and node.label() == 'NP' and node.left_sibline() != None:
    #                         for child in node:
    #                             if str(lemma_node) in str(child):
    #                                 node = child
    #                                 break
    #                             if child.label() == 'NP':
    #                                 subject = child
    #                         break
    #                     else:
    #                         node = node.parent()
    #                 break
    #         else:
    #             node = node.parent()

    while node.parent() != None:
        if node.parent().label() != 'VP' and node.left_sibling() != None and node.label() == 'VP':
            subject = node.left_sibling()
            while subject.label() != 'NP' and subject.left_sibling() != None:
                subject = subject.left_sibling()
            break
        else:
            node = node.parent()

    #     print("ascended node:", node, "\n")
    #     print("subject:", subject, "\n")

    # return value
    if subject == "":
        return ""
    else:
        return subject.flatten()
    print()

# extract all subjects of sentences given a synset
def _subject(synset, sents):
    synonyms = synset.lemma_names()
    # print("synonyms:", synonyms)

    subjects_all = []
    for i, sent in enumerate(sents):
        print(i, ":", sent.sentence)

        lemma_inds = _get_indices_of_synsets(sent, synonyms)
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


# extract all objects of sentences given a synset
def _object(synset, sents):
    synonyms = synset.lemma_names()
    # print("synonyms:", synonyms)

    objects_all = []
    for i, sent in enumerate(sents):
        # print(i, ":", sent.sentence)
        objects = []

        lemma_inds = _get_indices_of_synsets(sent, synonyms)
        # print("lemma_inds:", lemma_inds)

        # may have more than one lemma_idx
        # e.g. lemma_inds = [2, 5]

        for lemma_idx in lemma_inds:
            # object = _extract_object(sent, lemma_idx)
            object = ""
            objects.append(object)

            # TEST PRINT
            # if subject == "":
            #     print("no object found")
            # else:
            #     print("object found:", object)

        objects_all.append(objects)
        # print()
    return objects_all
