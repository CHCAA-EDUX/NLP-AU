'''
run in terminal before class

pip install spacy
pip install networkx==2.3
python -m spacy download en_core_web_sm
python -m spacy download en_core_web_lg
pip install torch
pip install datasets
'''
from datasets import load_dataset
from collections import Counter

# load the sst2 dataset
dataset = load_dataset("glue", "sst2")

# select the train split
train = dataset["train"]

tokens = ('this', 'is', 'a', 'test', 'this', 'this')
tokens2= ('this', 'is', 'a', 'test', 'this', 'rabbit')

docs = (tokens, tokens2)

def term_freq(tokens):
    """
    Takes in a list of tokens (str) and return a dictionary of term frequency of each token
    tf(t,d) = count of t in d / number of words in d
    """
    token_counts = Counter([token for token in tokens])
    term_freq = ([(token, count/len(tokens)) for token, count in token_counts.items()])
    return(term_freq)


def doc_freq(docs):
    """
    Takes in a list of documents which each is a list of tokens 
    and return a dictionary of frequencies for each token over all the 
    documents. E.g. {"Aarhus": 20, "the": 2301, ...}
    """
    doc_freq = Counter()
    for d in docs:
        cur_token_counts = Counter([token for token in d])
        doc_freq = doc_freq + cur_token_counts
    return(doc_freq)    

doc_freq(docs)