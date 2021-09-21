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
'''


