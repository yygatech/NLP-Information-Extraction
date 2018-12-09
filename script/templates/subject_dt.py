from script import task3_4


def extractSubDT(sentence, keywords):
    '''
    Get dependecy, then extract nsubj and nsubjpass as candidates
    :param sentence:
    :return:
    '''

    ret = []
    dep_treess = task3_4._dependency_parse([sentence])
    import numpy as np
    for tree in dep_treess:
        print(sentence)
        for governor, dep, dependent in tree.triples():
            print(governor, dep, dependent)
            if (dep.startswith("nsubj")):
                print('yes')

        conll4 = tree.to_conll(4)
        conll4 = np.array(conll4.split()).reshape(-1, 4)

        for candidate in conll4:
            if (candidate[3].startswith("nsubj")):
                ret.append(candidate)
    return ret
