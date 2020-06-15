import json

definitions = json.load(open("data.json"))

def definition(word):
    if word in definitions:
        return definitions[word]

    return "The word doesn't exists. Please check the spelling."

word = input("Enter word: ")
print(definition(word))