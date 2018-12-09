# task4.py

# 4 Information Extraction
# [nltk] Extracting Information from Text
# https://www.nltk.org/book/ch07.html
# chapter 5: Named Entity Recognition
# chapter 6: Relation Extraction

# Step 1: preprocessing
# keywords -> candidate synsets
from script.task4_utils.select_synset import _display_synsets

keywords = ["compose", "sing", "play", "invent", "title", "publish", "influence", "study", "visit", "born", "die"]
for i, keyword in enumerate(keywords):
    _display_synsets(keyword)

# choose the target synset
synsets = {}
synset["compose"] = ""


# template 1: compose(verb, composer, music, at-time, at-loc)

# template 2: sing(verb, singer, song, at-time, at-loc)

# template 3: play an instrument(verb, player, instrument, at-time, at-loc)

# template 4: invent/create(verb, inventor, invention, at-time, at-loc)

# template 5: style?

# template 6: titled/known as(verb, sb/sth, title)

# template 7: publish(verb, author, publication, publisher/media, at-time, at-location)

# template 8: influence(verb, influencer, affected, effect, degree/range)

# template 9: give/gain(verb, giver, gainer, item, currency, quantity, at-time, at-location)

# template 10: study(verb, sb, sth, at-time, at-loc)

# candidates: visit, reside, utilize, work, possess, born, die

