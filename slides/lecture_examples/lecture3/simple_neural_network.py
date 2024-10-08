# !pip install torch


import torch

perceptron = torch.nn.Linear(2, 1)

# Weights
print(perceptron.weight)
# Parameter containing:
# tensor([[0.0224, 0.0251]], requires_grad=True)

# Bias
print(perceptron.bias)
# Parameter containing:
# tensor([-0.1012], requires_grad=True)

# Forward pass
x = torch.tensor([0.5, 0.5])
output = perceptron(x)
output = torch.sigmoid(output) # activation function
print(output)
# tensor([0.4806], grad_fn=<SigmoidBackward0>)


# Loss
y = torch.tensor([1.0]) # true value
loss = torch.nn.functional.mse_loss(output, y)
loss.backward() # calculate gradients

# Examining the gradient
print(perceptron.bias.grad)
# tensor([-1.1061])

# Updating the weights
