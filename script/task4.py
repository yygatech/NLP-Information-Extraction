# task4.py

# 4 Information Extraction
# [nltk] Extracting Information from Text
# https://www.nltk.org/book/ch07.html
# chapter 5: Named Entity Recognition
# chapter 6: Relation Extraction

from templates import t1_compose as t1

# preprocessing
# keywords -> candidate synsets
from script.task4_utils.select_synset import _display_synsets

keywords = ["compose", "sing", "play", "invent", "entitle", "publish", "influence", "study", "visit", "be_born", "die"]
# for i, keyword in enumerate(keywords):
#     _display_synsets(keyword)

# choose the target synsets
synsets = {}

# template 1: compose(verb, composer, music, at-time, at-loc)
synsets["compose"] = "compose.v.02"
# definition: write music
# t1._test()

# template 2: sing(verb, singer, song, at-time, at-loc)
synsets["sing"] = "sing.v.02"
# definition: produce tones with the voice

# template 3: play an instrument(verb, player, instrument, at-time, at-loc)
synsets["play"] = "play.v.03"
# definition: play on an instrument

# template 4: invent/create(verb, inventor, invention, at-time, at-loc)
synsets["invent"] = "invent.v.01"
# definition: come up with (an idea, plan, explanation, theory, or principle) after a mental effort

# template 5: style?

# template 6: entitle(verb, sb/sth, title)
synsets["entitle"] = "entitle.v.02"
# definition: give a title to

# template 7: publish(verb, author, publication, publisher/media, at-time, at-location)
synsets["publish"] = "publish.v.03"
# definition: have (one's written work) issued for publication

# template 8: influence(verb, influencer, affected, effect, degree/range)
synsets["influence"] = "influence.v.01"
# definition: have and exert influence or effect

# template 9: give/gain(verb, giver, gainer, item, currency, quantity, at-time, at-location)

# template 10: study(verb, sb, subject, at-time, at-loc)
synsets["study"] = "learn.v.04"
# definition: be a student of a certain subject

# template 11: visit(verb, sb, to-loc, time?)
synsets["visit"] = "visit.v.01"
# definition: go to see a place, as for entertainment

# template 12: be_born(verb, sb, at-time, at-place)
synsets["be_born"] = "be_born.v.01"
# definition: come into existence through birth

# template 13: die/pass away(verb, sb, at-time, at-place, cause)
synsets["die"] = "die.v.01"
# definition: pass from physical life and lose all bodily attributes and functions necessary to sustain life

# candidates: reside, utilize, work, possess
