import json
from difflib import get_close_matches as gcm #lib that take a word input and return closest match from list

# Read data.json file and loading it to data variable
data = json.load(open("data.json",'r'))

#Method which returns the meaning from data object
def find_meaning(word):
    if word in data:
        return(data[word])
    elif word.title() in data:
        return (data[word.title()])
    elif len(gcm(word, data.keys()))>0:
        #get an input from user asking if they meant a closest match from the file we have
        print("word you entered not found, try any from %s instead.: " %gcm(word, data.keys(), cutoff=0.8))
        word = input("your word: ")
        if word in data:
            #get_close_matches(word, possibilities, n=3, cutoff=0.6) is default
            return(data[word])
        else:
            print('Word not found')
            return
    else:
        return("Word not found")


#Get the word from user to search for meaning
word = input("Enter the word to find meaning: ")
#lowering the input
word = word.lower()

#printing return value from find_meaning method
word_meaning = find_meaning(word)
try:
    if len(word_meaning)>1:
        print("More than 1 meaning found for the word '%s' and they are : " %word)
        for each in word_meaning:
            print(each)
    else:
        print("Meaning for the word '%s' is: " %word)
        print(word_meaning[0])
except TypeError:
    print("Try again")
