import torch
from torch import nn
from transformers import AutoModel, AutoTokenizer

tokenizer = AutoTokenizer.from_pretrained("bert-base-uncased")
model = AutoModel.from_pretrained("bert-base-uncased")

# add a classification head
classifier = nn.Linear(
    768, num_labels
)  # embed dim is 768, num_labels is the number of classes

# combine the model and the classifier
model = nn.Sequential(model, classifier)

# training the model
loss = nn.CrossEntropyLoss()
optimizer = torch.optim.AdamW(model.parameters(), lr=5e-5)  # or SGD

train_loader = ...  # create a DataLoader with your data

model.train()

for epoch in range(epochs):  # number of epochs to train for
    for text, label in train_loader:
        optimizer.zero_grad()

        # tokenize text
        token_ids = tokenizer(text, return_tensors="pt", padding=True, truncation=True)
        output = model(**token_ids)

        # compute loss
        loss_value = loss(output, label)

        # compute gradients
        loss_value.backward()
        
        # update weights
        optimizer.step()


# Evaluate ...


# Alternatively the transformer library provides a class that combines the model and the classifier

from transformers import AutoModelForSequenceClassification

model = AutoModelForSequenceClassification.from_pretrained(
    "google-bert/bert-base-cased", num_labels=5
)