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

# load the sst2 dataset
dataset = load_dataset("glue", "sst2")

# select the train split
train = dataset["train"]




def term_freq(tokens: List[str]) -> dict:
    """
    Takes in a list of tokens (str) and return a dictionary of term frequency of each token
    tf(t,d) = count of t in d / number of words in d
    """
    for token in tokens:
        if token in document: 
            
    sum(if tok)
    # your code