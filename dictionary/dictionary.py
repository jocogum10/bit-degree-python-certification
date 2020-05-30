import json
from difflib import get_close_matches

data = json.load(open('data.json'))

def translate(word):
    word = word.lower()
    if word in data:
        return data[word]
    elif word.title() in data:
        return data[word.title()]
    elif word.upper() in data:
        return data[word.upper()]
    elif len(get_close_matches(word, data.keys())) > 0:
        print('did you mean \'%s\' instead?' % get_close_matches(word, data.keys())[0])
        decide = input("press y for yes: ")
        if decide.lower() == 'y':
            return data[get_close_matches(word, data.keys())[0]]
        elif decide.lower() == 'n':
            return 'Word cannot be found.'
        else:
            return 'You have entered a wrong choice.'
    else:
        return 'Word cannot be found.'


word = input("Enter the word you want to search: ")
output = translate(word)
if type(output) == list:
    for definition in output:
        print(definition)
else:
    print(output)