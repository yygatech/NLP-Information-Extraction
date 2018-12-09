# task3_4.py

## 3.4 (updated version)
# perform dependency parsing
# or full-syntactic parsing
# to parse tree-based patterns as features

### 3.4.0 preparation
# Setup CoreNLP with Python:
# https://www.khalidalnajjar.com/setup-use-stanford-corenlp-server-python/
# Download Stanford CoreNLP:
# https://stanfordnlp.github.io/CoreNLP/index.html#download
# Unzip to local directory:
# for example: ../resources/stanford-corenlp-full-2018-10-05/
# Run Stanford CoreNLP Server in command line:
# java -mx4g -cp "*" edu.stanford.nlp.pipeline.StanfordCoreNLPServer -annotators "tokenize,ssplit,pos,lemma,parse,sentiment" -port 9000 -timeout 30000

# nlkt.parse API:
# http://www.nltk.org/api/nltk.parse.html#nltk.parse.corenlp.GenericCoreNLPParser

def _dependency_parse(sentences):
    ### 3.4.1 CoreNLP Dependency Parser
    from nltk.parse.corenlp import CoreNLPDependencyParser as DP
    dep_parser = DP(url='http://localhost:9000')

    # example:
    # parse, = dep_parser.raw_parse(
    #     'The quick brown fox jumps over the lazy dog.'
    # )
    # print(parse.to_conll(4))

    parse = dep_parser.raw_parse_sents(sentences)

    dep_trees = []
    for itr_tree in parse:
        for tree in itr_tree:
            dep_trees.append(tree)
            # print(tree.to_conll(4))
    #         print(tree.tree())
    #     print()

    return dep_trees

def _parse(sentences):
    ### 3.4.2 CoreNLP Parser
    from nltk.parse.corenlp import CoreNLPParser as CP
    parser = CP(url='http://localhost:9000')

    # example:
    # parse, = parser.raw_parse(
    #     'The quick brown fox jumps over the lazy dog.'
    # )
    # print(parse.pretty_print())

    parse = parser.raw_parse_sents(sentences)
    # print(sentences[5:6])

    parse_trees = []
    for itr_tree in parse:
        for tree in itr_tree:
            parse_trees.append(tree)
            # tree.pretty_print()
        # print()

    return parse_trees