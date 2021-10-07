"""
Logistic regression implemented using the nn.module class
First
pip install torch
pip install datasets
pip install spacy
"""

import torch
import torch.nn as nn
from sklearn import datasets
from datasets import load_dataset
import spacy
nlp = spacy.load("en_core_web_sm")


class Model(nn.Module):
    def __init__(self, n_input_features = 10):
        super(Model, self).__init__()
        self.linear1 = nn.Linear(n_input_features, 30)
        self.linear2 = nn.Linear(30, 30)
        self.linear3 = nn.Linear(30, 1)

    def forward(self, x):
        x = self.linear1(x)
        x = torch.sigmoid(x)
        x = self.linear2(x)
        x = torch.sigmoid(x)
        x = self.linear3(x)
        y_pred = torch.sigmoid(x)
        return y_pred

#from src.class4 import term_freq

def flatten(t):
    return [item for sublist in t for item in sublist]

from collections import Counter

def split_func(sentence):
    return (sentence.split())

# make a train dataset
dataset = load_dataset("emotion")
train = dataset["train"]

string_list = []

# Split the sentences into one list
for s in range(10):
    sentence = train["text"][s]
    split_sentence = split_func(sentence)
    string_list.append(split_sentence)


# Count and dictionary function
# tf(t,d) = count of t in d / number of words in d
def term_freq(tokens: 'list[str]') -> dict:
    #flatten_tokens = flatten(tokens) # only if it is a list of lists
    print(tokens)
    term_freq_list = dict(Counter(tokens))
    
    tf = {}

    # Get term frequency
    for element in term_freq_list:
        tf[str(element)] = term_freq_list[str(element)]/len(tokens)
    return tf



type(train['text'])

term_freq(string_list)

'''

# Create dataset

X_numpy, y_numpy = datasets.make_classification(n_samples=1000, n_features=10, random_state=7)
X = torch.tensor(X_numpy, dtype=torch.float)
y = torch.tensor(train['label'], dtype=torch.float)
y = y.view(y.shape[0], 1)


# initialize model
model = Model(n_input_features=10)

# define loss and optimizer
criterion = nn.BCELoss()
optimizer = torch.optim.Adam(model.parameters()) 

# train
epochs = 10000
for epoch in range(epochs):
    # forward
    y_hat = model(X)

    # backward
    loss = criterion(y_hat, y)
    loss.backward()
    optimizer.step()
    optimizer.zero_grad()

    # some print to see that it is running
    if (epoch+1) % 1000 == 0:
        print(f'epoch: {epoch+1}, loss = {loss.item():.4f}')

'''