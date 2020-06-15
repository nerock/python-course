import json
from difflib import get_close_matches

definitions = json.load(open("data.json"))

def definition(word):
    word = word.lower()
    if word in definitions:
        definition = definitions[word]

        if type(definition) == list:
            definition = " ".join(definition)

        return definition

    error = "Please check the spelling."
    close_matches = get_close_matches(word, definitions.keys())

    if len(close_matches) > 0:
        error = "Did you mean any of these? " + ",".join(close_matches)

    return f"The word doesn't exist. {error}"

word = input("Enter word: ")
print(definition(word))