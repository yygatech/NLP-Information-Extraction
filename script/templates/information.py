def _gather_info(keyword, sent, subjects, objects, times, locations, persons=None):
    '''
    gather info for one sentence
    :return: extracted info
    '''
    info = {}
    info["keyword"] = keyword
    info["sentence"] = sent.sentence
    info["subjects"] = subjects
    info["objects"] = objects
    info["times"] = times
    info["locaitons"] = locations
    return info


def _gather_info_batch(keyword, sents, subjects_all, objects_all, times, locations, persons=[]):
    '''
    gather info for a batch of sentences
    :return: batch info as a list
    '''
    info_batch = []
    for i, sent in enumerate(sents):
        info = _gather_info(keyword, sent, subjects_all[i], objects_all[i], times[i], locations[i])
        info_batch.append(info)
    return info_batch
