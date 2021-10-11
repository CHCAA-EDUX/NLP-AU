"""
Logistic regression implemented using the nn.module class
"""

import torch
import torch.nn as nn
from sklearn import datasets


class Model(nn.Module):
    def __init__(self, n_input_features=10):
        super().__init__()
        self.linear = nn.Linear(n_input_features, 1)

    def forward(self, x):
        x = self.linear(x)
        y_pred = torch.sigmoid(x)
        return y_pred


# Create dataset
X_numpy, y_numpy = datasets.make_classification(
    n_samples=1000, n_features=10, random_state=7
)
X = torch.tensor(X_numpy, dtype=torch.float)
y = torch.tensor(y_numpy, dtype=torch.float)
y = y.view(y.shape[0], 1)


# initialize model
model = Model(n_input_features=10)

# define loss and optimizer
criterion = nn.BCELoss()
optimizer = torch.optim.AdamW(model.parameters())

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
    if (epoch + 1) % 1000 == 0:
        print(f"epoch: {epoch+1}, loss = {loss.item():.4f}")
