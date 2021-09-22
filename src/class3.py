import spacy # Got an error when the document was called spacy. Changed the name and no longer no attribute "load"
nlp = spacy.load("en_core_web_sm")
doc = nlp("This is an English text")

#print(type(doc))
# <class 'spacy.tokens.doc.Doc'>

token = doc[1]
#print(token)
# is

#print(type(token))
# <class 'spacy.tokens.token.Token'>

#print(dir(token))

#print(token.is_digit)
# False

'''
Exercise 1: 
Inspect the doc-object using dir and type along with the documentation. 
You should before class have been through 
i) about what is intended use (or benefit) of the doc-object 
ii) What are the two ways in which I can create a Doc object? 
'''
# A Doc is a sequence of Token objects

# The intended use as a container for accessing linguistic annotations.

# I can make a doc object via the nlp function
doc2 = nlp("this is a doc")

# Or like this
from spacy.tokens import Doc

words = ["hello", "world", "!"]
spaces = [True, False, False]
doc = Doc(nlp.vocab, words=words, spaces=spaces)
print(doc)

''' 
Exercise 2: Make a corpus loader
'''
import sys, os
from pathlib import Path

def corpus_loader(folder: str):
    
    #A corpus loader function which takes in a path to a 
    #folder and returns a list of strings.
    infile = os.path.join(folder)

    for filepath in Path(infile).glob("*.txt"):
        with open(filepath, "r", encoding = "utf-8") as file:
            loaded_text = file.read()
            
            # Split text into sentences
            text = loaded_text.split('.')

            # split sentences into tokens
            text = loaded_text.split(' ')


    return text

#corpus_loader(folder = "train_corpus")



infile = os.path.join("syllabus/xlasses/data/train_corpus")

for filepath in Path(infile).glob("*.txt"):
    with open(filepath, "r", encoding = "utf-8") as file:
        loaded_text = file.read()
            
        # Split text into sentences
        text = loaded_text.split('.')

        # split sentences into tokens
        text = loaded_text.split(' ')

        print(text)