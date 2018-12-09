from script.task3_5 import __synsets

def _display_synsets(keyword):
    print("keyword:", keyword, "\n")
    synsets = __synsets(keyword)
    for i, synset in enumerate(synsets):
        definition = synset.definition().lower()
        examples = synset.examples()

        print(synset)
        print("definition:", definition)
        print("examples:", examples)
        print()
    print("---------------------------------------------")
