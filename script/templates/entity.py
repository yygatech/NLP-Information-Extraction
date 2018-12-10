
def extractEnt(sents, key="PERSON"):
    '''
    Entity Recognition
    :param sents:
    :param key:'PERSON', 'LOCATION'
    :return:
    '''
    import nltk
    ret = []
    for i, sent in enumerate(sents):
        tree = nltk.ne_chunk(sent.pos)
        getNodes(tree, key, ret)
    return set(ret)

def getNodes(parent, key, output):
    '''
    visit all of the notes of a tree
    return the words meets the requirement
    :param parent:
    :param key:
    :param output:
    :return:output
    '''
    import nltk
    for node in parent:
        if type(node) is nltk.Tree:
            # print(node.label(), node.leaves())
            if str(node.label()) == key:
                word = node.leaves()[0][0]
                tag = node.leaves()[0][1]
                if(tag != 'JJ'):
                    output.append(word)
            getNodes(node, key, output)