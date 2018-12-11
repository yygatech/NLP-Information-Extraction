
def extractEnt(sent, grove, key):
    '''
    entity recognition
    :param sent:
    :param grove
    :param key:'PERSON', 'LOCATION'
    :return:
    '''
    ret = []
    tree = grove.ne
    getNodes(tree, key, ret)
    return list(set(ret))


def _extract_entity_batch(sents, groves, key):
    '''
    batch entity recognition
    :param sents:
    :param groves
    :param key:
    :return: entity batch
    '''
    entity_batch = []
    for i, sent in enumerate(sents):
        entity = extractEnt(sent, groves[i], key)
        entity_batch.append(entity)
    return entity_batch


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
            if str(node.label()) in key:
                word = node.leaves()[0][0]
                tag = node.leaves()[0][1]
                # if(tag != 'JJ'):
                output.append(word)
            getNodes(node, key, output)


def getAllPRP():
    return ['I','me', 'we', 'us', 'you', 'she', 'her', 'he', 'him', 'they', 'them']