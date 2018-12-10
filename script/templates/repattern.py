### extract subject
#
from script.trees import Trees
import nltk

# function: get indices of a lemma
def _get_indices_of_synsets(sent, compose_synonyms):
    lemmas_inds = []
    for lemma_idx, lemma in enumerate(sent.lemmas):
        if lemma in compose_synonyms:
            lemmas_inds.append(lemma_idx)
    return lemmas_inds


# function: extract subject
def _extract_subject(sent, lemma_idx):
    verb = sent.tokens[lemma_idx]
    # print("verb at", lemma_idx, ":", verb)

    pos = sent.pos
    # print("pos:", pos)

    trees = Trees(sent.sentence, pos)
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

# display subjects of sentences given a synset
def _subject(synset, sents):
    synonyms = synset.lemma_names()
    # print("synonyms:", synonyms)
    ret = []
    for i, sent in enumerate(sents):
        # print(i, ":", sent.sentence)

        lemma_inds = _get_indices_of_synsets(sent, synonyms)
        # print("lemma_inds:", lemma_inds)

        # may have more than one lemma_idx
        # e.g. lemma_inds = [2, 5]

        for lemma_idx in lemma_inds:
            subject = _extract_subject(sent, lemma_idx)
            sub = {}
            if subject == "":
                print("no subject found")
            else:
                sub[subject.label()] = ' '.join(subject.leaves())
                ret.append(sub)
    return ret

def getPPs(sents):
    grammar = r"""
              NP: {<DT|JJ|NN.*>+}          # Chunk sequences of DT, JJ, NN
              NPCNP: {<NP><CC><NP>}
              PP: {<IN|TO|RP><NP|NPCNP>} 
              """
    # VP: {<VB.*><NP|PP>+$} # Chunk verbs and their arguments
    # VP: {<VB.*><VBD|IN.*>+}
    cp = nltk.RegexpParser(grammar)
    ret = []
    for sent in sents:
        tree = cp.parse(sent.pos)
        for subtree in tree.subtrees():
            # print(subtree)
            if subtree.label() == 'PP':
                # print(subtree.leaves())
                phase = [node[0] for node in subtree.leaves()]
                phase = " ".join(phase)
                ret.append(phase)
    return ret

def getVNNs(sents):
    grammar = r"""
              NP: {<DT|JJ|NN.*>+}          # Chunk sequences of DT, JJ, NN
              VNN: {<V.*><NP>} 
              """
    cp = nltk.RegexpParser(grammar)
    ret = []
    for sent in sents:
        tree = cp.parse(sent.pos)
        for subtree in tree.subtrees():
            # print(subtree)
            if subtree.label() == 'VNN':
                # print(subtree.leaves())
                phase = []
                for node in subtree.leaves():
                    word = getWordLemma(node[0],node[1])
                    phase.append(word)
                phase = " ".join(phase)
                ret.append(phase)
    return ret


def extractRelation(sents):
    # cp = nltk.RegexpParser('CHUNK: {<V.*> <TO> <V.*>}')

    grammar = r"""
      PP: {<IN><NP>} 
      # NP: {<DT|JJ|NN.*>+}          # Chunk sequences of DT, JJ, NN
      # VP: {<VB.*><NP|PP|CLAUSE>+$} # Chunk verbs and their arguments
      """
    cp = nltk.RegexpParser(grammar)

    # for sent in brown.tagged_sents():
    for sent in sents:
        tree = cp.parse(sent.pos)
        for subtree in tree.subtrees():
            # if subtree.label() == 'NP':
            #     print(subtree)
            if subtree.label() == 'PP':
                print(subtree)

def getWordLemma(word, tag):
    from nltk.stem import WordNetLemmatizer as LM
    lm = LM()
    if(tag != ""):
        lemma = lm.lemmatize(word, tag)
    else:
        lemma = lm.lemmatize(word)
    return lemma

def penn2wn(penn_tag):
    from nltk.corpus import wordnet as wn
    if penn_tag.startswith('J'):
        return wn.ADJ
    elif penn_tag.startswith('V'):
        return wn.VERB
    elif penn_tag.startswith('N'):
        return wn.NOUN
    elif penn_tag.startswith('R'):
        return wn.ADV
    else:
        return ''

def getWordLemma(word, tag):
    from nltk.stem import WordNetLemmatizer as LM
    lm = LM()
    tag = penn2wn(tag)
    if(tag != ""):
        lemma = lm.lemmatize(word, tag)
    else:
        lemma = lm.lemmatize(word)
    return lemma

def penn2wn(penn_tag):
    from nltk.corpus import wordnet as wn
    if penn_tag.startswith('J'):
        return wn.ADJ
    elif penn_tag.startswith('V'):
        return wn.VERB
    elif penn_tag.startswith('N'):
        return wn.NOUN
    elif penn_tag.startswith('R'):
        return wn.ADV
    else:
        return ''