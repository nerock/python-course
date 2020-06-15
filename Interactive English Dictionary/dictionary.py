import json
from difflib import get_close_matches

definitions = json.load(open("data.json"))

def format_definitions(definition_list):
    if type(definition_list) != list:
        return definition_list

    res = ""
    for i, d in enumerate(definition_list, 1):
        res += f"{i}: {d}\n"

    return res

def definition(word):
    word = word.lower()
    if word in definitions:
        definition = definitions[word]
        
        return format_definitions(definition)

    error = "Please check the spelling."
    close_matches = get_close_matches(word, definitions.keys())

    if len(close_matches) > 0:
        error = "Did you mean any of these? " + ",".join(close_matches)

    return f"The word doesn't exist. {error}"

word = input("Enter word: ")
print(definition(word))