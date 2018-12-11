class Sentence:
    def __init__(self, idx, sentence, tokens, pos, tag, lemmas):
        self.idx = idx
        self.sentence = sentence
        self.tokens = tokens
        self.pos = pos
        self.tag = tag
        self.lemmas = lemmas
