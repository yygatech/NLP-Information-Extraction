from pathlib import Path

from script import pickle_utils as pu
# from script.trees import Trees

# function: pickle keyword sents if never pickled
# arguments: keyword, sents
# return: boolean(not exist and new pickle)
def _pickle_keyword_sents_if_not(keyword, sents):
    pickled_path = Path("./../../pickle/" + keyword + "_sents.pickle")
    # print(pickled_path)

    if pickled_path.exists():
        # print("file_exists")
        return False
    else:
        # print("file not exists")

        # pickle keyword sents
        pu._set_keyword_sents(keyword, sents)
        # print("finish pickling")
        return True

# doen't work
# function: pickle keyword groves if never pickled
# arguments: keyword, groves
# return: boolean(not exist and new pickle)
# def _pickle_keyword_groves_if_not(keyword, sents):
#     pickled = Path("./../../pickle/" + keyword + "_groves.pickle")
#     if pickled.is_file():
#         print("file exists")
#         return False
#     else:
#         print("file not exists")
#
#         # pickle groves
#         groves = []
#         for i, sent in enumerate(sents[:10]):
#             print("start parsing sentence:", i)
#             trees = Trees(sent)
#             groves.append(trees)
#             print("finish parsing sentence:", i)
#
#         pu._set_groves(keyword, groves)
#         print("finish pickling")
#         return True