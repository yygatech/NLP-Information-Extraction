### pattern match

import nltk

def getPPs(sents):
    grammar = r"""
              NP: {<DT|JJ|NN.*>+}          # Chunk sequences of DT, JJ, NN
              NPCNP: {<NP><CC><NP>}
              PP: {<IN|TO|RP><CD|NP|NPCNP>} 
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

def getkeyPhases(sents, words):
    delim = ','
    ret = []
    for sent in sents:
        ret_s = []
        for word in words:
            sentence_list = sent.sentence.split(delim)
            for phase in sentence_list:
                idx = phase.lower().find(word.lower())
                if(idx > -1):
                    ret_s.append(phase)
        ret.append(ret_s)
    return ret


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