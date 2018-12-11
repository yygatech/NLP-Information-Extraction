from nltk.parse.corenlp import CoreNLPParser as CP
from nltk.parse.corenlp import CoreNLPDependencyParser as DP
from nltk import ne_chunk


# parsed tree objects
class Trees:
    def __init__(self, sent, cp=True, dp=True, ne=True):
        self.sent = sent
        if cp:
            parser = CP(url='http://localhost:9000')
            self.cp = next(parser.raw_parse(sent.sentence))

        if dp:
            dep_parser = DP(url='http://localhost:9000')
            self.dp = next(dep_parser.raw_parse(sent.sentence))

        if ne:
            self.ne = ne_chunk(sent.pos)

# Sample
# trees = Trees(sent)
# ctree = trees.cp
# dtree = trees.dp
# netree = trees.ne
#
# print("print ctree:")
# ctree.pretty_print()
#
# print("print dtree:")
# print(dtree.to_conll(4))
#
# print("print ner tree:")
# print(netree)
