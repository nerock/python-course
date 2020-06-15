import json

data = json.load(open("data.json"))

def definition(word):
    return data[word]

word = input("Enter word: ")
print(definition(word))