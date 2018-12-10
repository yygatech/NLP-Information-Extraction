from nltk.parse.corenlp import CoreNLPParser as CP
from nltk.parse.corenlp import CoreNLPDependencyParser as DP
from nltk import ne_chunk

# parsed tree objects
class Trees:
    # def __init__(self, sentence, pos):
    #     parser = CP(url='http://localhost:9000')
    #     dep_parser = DP(url='http://localhost:9000')
    #     self.cp = next(parser.raw_parse(sentence))
    #     self.dp = next(dep_parser.raw_parse(sentence))
    #     self.ne = ne_chunk(pos)

    def __init__(self, sent):
        parser = CP(url='http://localhost:9000')
        dep_parser = DP(url='http://localhost:9000')
        self.cp = next(parser.raw_parse(sent.sentence))
        self.dp = next(dep_parser.raw_parse(sent.sentence))
        self.ne = ne_chunk(sent.pos)