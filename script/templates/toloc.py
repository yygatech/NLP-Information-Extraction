from script.templates import repattern as rp
from script.templates import entity

def _toLocation(sents, verbs):
    ret = []
    for sen in sents:
        print()
        print(sen.sentence)
        pps = rp.getPPs([sen])
        locations = entity.extractEnt(sents, ['GPE', 'GSP','GPE', 'ORGANIZATION'])
        prp = entity.getAllPRP()
        nextwords = _getNextWord(sen, verbs)
        # print('nextwords:', nextwords)
        # print(pps)
        # print(locations)

        location = []

        for word, tag in nextwords:
            #first priority
            if(tag == 'TO'):
                for pp in pps:
                    pp_list = pp.split(" ")
                    loc = pp[(len(pp_list[0]) + 1):]
                    if(pp_list[0].upper() == tag):
                        if isPartof(loc, locations):
                            location.append(loc)
                        # second priority
                        elif(len(location)==0):
                            location.append(loc)
            if (len(location) == 0):
                for pp in pps:
                    pp_list = pp.split(" ")
                    loc = pp[(len(pp_list[0]) + 1):]
                    if isPartof(loc, locations):
                        location.append(loc)
            if (word not in prp) and (len(location) == 0):
                    location.append(word)
        # print('location:', location)
        ret.append(list(set(location)))


        # print(pps)
        # for loc in locations:
        #     print(loc)
        #     if loc in str(pps):
        #         print(pps)
        nextwords = _getNextWord(sen, verbs)
        # print(nextwords)
    return ret

def isPartof(loc, locations):
    for l in locations:
        if str(loc).__contains__(l):
            return True
    return False

def _getNextWord(sent, verbs):
    '''
    Given a Sentence
    :param sent:
    :param verbs:
    :return:(phanse, tag)
    '''
    ret = []
    for start in verbs: # the start verb
        for i, word_pos in enumerate(sent.pos):
            word = word_pos[0]
            pos = word_pos[1]
            word = rp.getWordLemma(word, pos)
            if (start == word):
                #get all the next NN phase
                vnns = rp.getVNNs([sent])
                max_nn = ""
                for vnn in vnns:
                    vnn_list = vnn.split(" ")
                    v = vnn_list[0]
                    nn = vnn[(len(vnn_list[0]) + 1):]
                    if(start == v):
                        if(len(nn)>len(max_nn)):
                            max_nn = nn
                if(len(max_nn)>0):
                    ret.append((max_nn,sent.tag[i+1]))
                else:
                    ret.append((sent.tokens[i+1], sent.tag[i+1]))
    # print('ret:', ret)
    return ret






