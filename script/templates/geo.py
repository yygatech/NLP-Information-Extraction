from script.templates import repattern as rp
from script.templates import entity


def _getLocation(sents, groves, verbs):
    ret = []
    locs = entity._extract_entity_batch(sents, groves, ['GPE', 'GSP', 'GPE', 'ORGANIZATION'])
    locations = []
    for loc in locs:
        for l in loc:
            locations.append(l)

    for sen in sents:
        pps = rp.getPPs([sen])
        prp = entity.getAllPRP()
        nextwords = _getNextWord(sen, verbs)
        # print()
        # print('sentence:', sen.sentence)
        # print('nextwords:', nextwords)
        # print('pps:',pps)
        # print('locations:',locations)

        location = []

        for word, tag in nextwords:
            #first priority
            if(tag == 'TO'):
                for pp in pps:
                    pp_list = pp.split(" ")
                    loc = pp[(len(pp_list[0]) + 1):]
                    if(pp_list[0].upper() == tag):
                        l = getLocForGeo(loc,locations)
                        if len(l)>0:
                            location.append(l)
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
                n_word = len(word.split(" "))
                if(tag == 'IN') and (n_word != 1):
                    location.append(word)
                elif(n_word == 1) and (len(word)>2):
                    location.append(word)
        # print('location:', location)
        ret.append(list(set(location)))

    return ret


def _toLocation(sents, groves, verbs):
    ret = []

    locs = entity._extract_entity_batch(sents, groves, ['GPE', 'GSP', 'GPE', 'ORGANIZATION'])
    locations = []
    for loc in locs:
        for l in loc:
            locations.append(l)

    for sen in sents:
        pps = rp.getPPs([sen])
        prp = entity.getAllPRP()
        nextwords = _getNextWord(sen, verbs)
        # print()
        # print(sen.sentence)
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
                        l = getLocForGeo(loc, locations)
                        if len(l) > 0:
                            location.append(l)
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

def getLocForGeo(loc, locations):
    for l in locations:
        if str(loc).__contains__(l):
            print(loc, l)
            return l
    return ""

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






