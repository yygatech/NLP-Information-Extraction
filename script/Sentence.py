class Sentence:
    def __init__(self, i):
        self.sentence = sentences[i]
        self.tokens = words_all[i]
        self.pos = pos_tags_all[i]
        self.tags = tags_all[i]
        self.lemmas = lemmas_all[i]