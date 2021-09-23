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

# The intended use is as a container for accessing linguistic annotations.
# More information about the individual tokens. 

# I can make a doc object via the nlp function
doc2 = nlp("this is a doc")

# Or like this
from spacy.tokens import Doc

words = ["hello", "world", "!"]
spaces = [True, False, False]
doc = Doc(nlp.vocab, words=words, spaces=spaces)


# or with the 
#doc = Doc.__init__() 
# Classes are usually denoted with uppercase
''' 
Exercise 2: Make a corpus loader
'''
import sys, os
from pathlib import Path
path = "syllabus/classes/data/train_corpus"
list_of_files = os.listdir(path)
#print(len(list_of_files))

#path_to_file = "syllabus/classes/data/train_corpus/1.txt"

file_list = []

def corpus_loader(folder: str):
    
    #A corpus loader function which takes in a path to a 
    #folder and returns a list of strings.

    for file in folder:
        path_to_file = os.path.join("syllabus/classes/data/train_corpus", str(file))
        with open(path_to_file) as f:
            document = f.read()
            file_list.append(document)

    return list(file_list)

texts = corpus_loader(folder = list_of_files)
doc = nlp(texts[0])
'''
Exercise 3: 
Filter a text to keep only the lemma of nouns, adjectives and verbs
'''
kept_tokens = []
for token in doc:
    pos = ['NOUN', 'VERB', 'ADJ']
    if token.pos_ in pos:
        token = token.lemma_
        kept_tokens.append(token)

#print(kept_tokens)
'''
# Exercise 4
Calculate the ratio of pos-tags in texts. 
The ratios of pos-tags on other linguistic feature have for example been linked to scizophrenia 
which e.g. use less adverbs, adjectives, and determiners (e.g., “the,” “a,”).
'''
from collections import Counter
tokens_list = []

for token in doc:
    tokens_list.append(token.pos_)

counts = Counter(tokens_list)

for element in counts:
    print(str(element), round(counts[str(element)]/len(doc)*100, 1), '%')




## other ways
#You can also do count as a list comprehension
# counts = Counter([token.pos_ for token in doc])
#counts.values can extract the values. Frida did this for each list and then zipped them

'''
Exercise 5
Calculate the mean dependacy distance
'''
# How do we get the distance between the words?
# We have a token
#token.head 
# which token it refers to
# Take the indices of the tokens .i and subtract the two indices. (Remember to get the absolute value)