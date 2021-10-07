"""
Logistic regression implemented using the nn.module class
"""

import torch
import torch.nn as nn
from sklearn import datasets
from datasets import load_dataset
import spacy
from neural_network_as_nnmodule import Model
from src.tf import term_freq

'''
Once choosing the dataset e.g. emotion, the text needs 
to represented as a vector e.g. term_freq or tfidf. 

Dictvectorizer allows one to turn a dictionary representation into 
a vector, before feeding it to the model.

The label needs to be OneHotEncoded
'''

#Import english dictionary
nlp = spacy.load("en_core_web_sm")

#Import dataset
dataset = load_dataset("emotion")

#Create train data
train = dataset["train"][0:5]

#tokenize the dataset
for i in train["text"]:
    docs = []
    doc = nlp(i)
    docs.append(doc)

print(doc)

# Create dataset
token = term_freq(train["text"])

'''
X = torch.tensor(mangernogether, dtype=torch.float)
y = torch.tensor(train['label'], dtype=torch.float)
y = y.view(y.shape[0], 1)


# initialize model
model = Model(n_input_features=10)

# define loss and optimizer
criterion = nn.CrossEntropyLoss()
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