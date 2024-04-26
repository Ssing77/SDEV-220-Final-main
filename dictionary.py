import json
from difflib import get_close_matches
with open('dictionary_compact.json') as f:
    data = json.load(f)

# Giving the program a word, program finds closest match to word,
# then gives definition vvv

def translate(word):
    word = word.lower()
    # program looks for word
    if word in data:
        return data[word]
    elif word.title() in data:
        return data[word.title()]
    elif word.upper() in data:
        return data[word.upper()]
    elif len (get_close_matches(word, data.keys())) > 0:
        # program asks if the given word is what you are looking for
        print("Do you want to find %s" %get_close_matches(word, data.keys())[0])
        decide = input("Press y for yes and n for no: ")
        # if word is found
        if decide == "y":
            return data[get_close_matches(word, data.keys())[0]]
        # if word is not found
        elif decide == "n":
            return("Word not found! Please try again.")
        else:
            return("Please just enter y or n.")
    else: print("Word not found! Please try again.")
    # if word was not found, enter word again, or enter a different word
word = input("What word do you want to search: ")
output = translate(word)
if type(output) == list:
    for item in output:
        print(item)
else:
    print(output)