### 4.3.3 extract subject

# function: get indices of a lemma
def _get_indices_of_synsets(idx, compose_synonyms):
    res = []
    sent = sents[idx]
    #     print(sent.lemmas)
    for lemma_idx, lemma in enumerate(sent.lemmas):
        if lemma in compose_synonyms:
            res.append(lemma_idx)
    return res


# function: extract subject
def _extract_subject(idx, lemma_idx):
    sent = sents[idx]
    print("#", idx, sent.sentence, "\n")

    verb = sent.tokens[lemma_idx]
    print("verb:", verb, "\n")

    #     pos = sent.pos
    #     print("pos:", pos, "\n")

    trees = Trees(idx)
    cp = trees.cp
    #     dp = trees.dp
    #     ne = trees.ne
    #     cp.pretty_print()
    #     print("cp:", cp)
    #     print("dp:", dp.to_conll(4))
    #     print("ne:", ne)

    ptree = nltk.tree.ParentedTree.convert(cp)
    #     print("parented tree:", ptree)

    leaf_values = ptree.leaves()
    #     print(leaf_values)

    tree_location = ptree.leaf_treeposition(lemma_idx)
    #     print("tree location:", tree_location)

    node = ptree
    for i in tree_location[:-1]:
        node = node[i]
    #     print("node:", node)
    lemma_node = node

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


##################################

selected_inds = range(20)
for selected_idx in selected_inds:
    idx = compose_inds[selected_idx]
    lemma_inds = _get_indices_of_synsets(idx, compose_synonyms)
    print("lemma_inds:", lemma_inds)

    # may have more than one lemma_idx
    for lemma_idx in lemma_inds:
        subject = _extract_subject(idx, lemma_idx)

        if subject == "":
            print("no subject found")
        else:
            print(subject)

        print()