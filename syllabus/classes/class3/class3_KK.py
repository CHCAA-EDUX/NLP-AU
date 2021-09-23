###Class 3

'''
Use the following commands in the terminal before class: 

pip install spacy
python -m spacy download en_core_web_sm
python -m spacy download en_core_web_lg

'''
#When spcay is imported this should run: 
import spacy

nlp = spacy.load("en_core_web_sm")
doc = nlp("This is an English text")


'''We can expect this quite easily using, where we see that the output if the pipeline 
is a document class called `Doc`:
'''

#print the class of the doc
print(type(doc))

'''And that if you index the `Doc` you get a `Token` object.'''

token = doc[1]
print(token)
'''
What does this token contain? Well we can (like any other object in python) inspect it using the `dir`:
dir() returns list of the attributes and methods of any object
'''

print(dir(token))

'''Which gives is a very long list of which should look something like this: `['_', '__bytes__', (...), 'is_digit', 'is_punct', 'whitespace_']` of all the attributes of the function. 
We could also just have looked at the [documentation](https://spacy.io/api/token), but that wouldn't teach you how to inspect a class. 
For example we can now check whether a token is a digit:
'''

print(token.is_digit)

'''
You might also find a couple of other interesting things in there especially the `lemma_` 
which denotes the lemma of the token, `pos_` which denotes part-of-speech tag of the token 
and `ent_type_` which denote the entity type of the token.
'''

#**Exercise 1**:
'''
Inspect the `doc`-object using `dir` and `type` along with the [documentation](https://spacy.io/api/Doc). 
You should before class have thought
i) about what is intended use (or benefit) of the `doc`-object 

Doc allows access to sentences and named entities, exporting annotations to numpy arrays, 
and losslessly serialize to compressed binary strings.

ii) What are the two ways in which I can create an `Doc` object?

By Doc.__init__ 

Or by doc = nlp("text")

##Corpus loader
Before the class, you should have a corpus loader ready. This should be able to read in each file in the folder `syllabus/classes/data/train_corpus` as a list of strings (or similar object).
'''

def corpus_loader(folder):
    import os
    list_of_files = os.listdir(folder)
    document_list  = []
    for i in list_of_files:
        with open(os.path.join(folder, i)) as f:
            document = f.read()
            document_list.append(document)
    print(document_list)
    return(document_list)

corpus_loader('/work/NLP/NLP-E21/syllabus/classes/data/train_corpus')

'''
    A corpus loader function which takes in a path to a 
    folder and returns a list of strings.

You can use `os.listdir()` to list all the files in the directory.

import os
path = "syllabus/classes/data/train_corpus"
list_of_files = os.listdir(path)

You can read in a singular file using:

path_to_file = "syllabus/classes/data/train_corpus/1.txt"
with open(path_to_file) as f:
    document = f.read()

print(type(document))
 

You can combine paths using `os.path.join()`.

</details>

<br /> 


## Plan for class

- 1) Talk about exercise 1
- 2) Filter a text to keep only the lemma of nouns, adjectives and verbs


<details>
    <summary> Deconstruction of the task </summary>

The task can meaningfully be deconstructed into a series of functions on the token level:
- A filter function, which decided if a token should be kept.
- A function which extract the lemma

These function can then be combined and used iteratively over the tokens of a document.


</details>

<br /> 

- 3) Calculate the ratio of pos-tags in texts. The ratios of pos-tags on other linguistic feature have for example been [linked](https://www.nature.com/articles/s41537-021-00154-3) to scizophrenia which e.g. use less adverbs, adjectives, and determiners (e.g., “the,” “a,”).

<details>
    <summary> Deconstruction of the task </summary>

The task can meaningfully be deconstructed into a series of functions:
- A function (or list comprehension) which takes a list of tokens (Doc) and extracts the pos tag for each
- A function which counts these. *Hint* look up the `Counter` class.

</details>

<br /> 

- 4) If you get the time calculate PMI (see last weeks class) using the tokenization and sentence segmentation of spaCy.
'''