import nltk

# parsed tree objects
class Trees:
    def __init__(self, i):
        sentence = sentences[i]
        parser = CP(url='http://localhost:9000')
        dep_parser = DP(url='http://localhost:9000')
        self.cp = next(parser.raw_parse(sentence))
        self.dp = next(dep_parser.raw_parse(sentence))
        self.ne = nltk.ne_chunk(Sentence(i).pos)