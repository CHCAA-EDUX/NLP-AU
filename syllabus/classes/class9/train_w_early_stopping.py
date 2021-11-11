"""
This script contains pseudo-code for training a neural network with early stopping.
Thus the code is not intended to be executable.
"""

from typing import Callable, Iterable
from torch import nn
import torch

def train(model: nn.Module,
          epochs: int,
          batches: Iterable,
          loss_fn: Callable,
          val_X: torch.Tensor, 
          val_y: torch.Tensor,
          patience: int) -> nn.Module:
    """ Train a model with early stopping.

    Args:
        model(nn.Module): The model to train.
        epochs(int): The number of epochs to train for.
        batches(Iterable): An iterable of batches to train on.
        loss_fn(Callable): A function that takes in a batch and returns the loss.
        val_X(torch.Tensor): The validation data.
        val_y(torch.Tensor): The validation labels.
        patience(int): The number of epochs to wait before stopping.
    """
    # initialize an optimizer
    optimizer = ...

    val_losses = []
    best_val_loss = None

    # or alternatively
    # while True:
    for epoch in epochs:
        
        # set the moded to train mode only relevant if your model includes dropout or batch normalization
        # our model does not, but it is nice, to generalize this code
        model.train()

        for batch in batches:
            X, y = prepare_batch(batch)

            y_hat = model.forward(X)
            # the same as:
            # y_hat = model(X)

            loss = loss_fn(y, y_hat)
            
            # backward
            loss.backward()
            optimizer.step()
            optimizer.zero_grad()

        # early stopping
        model.eval() # set the model to evaluation mode only relevant if your model includes dropout or batch normalization
        val_y_hat = model.forward(val_X)
        val_loss = loss(val_y, val_y_hat)
        val_losses.append(val_loss)

        if val_loss < best_val_loss or best_val_loss is None:
            best_val_loss = val_loss
            # save the model

        better = [vl for vl in val_losses[-patience:] if val_loss >= vl]
        # another way it to compare it to the mean
        if len(better) == patience:
            break

        # another approach which is slightly different:
        # if val_loss < best_val_loss or best_val_loss is None:
        #     best_val_loss = val_loss

        # print(f"Epoch {epoch + 1}/{epochs}")
        # print(f"Loss: {loss.item():.4f}")
        # if val_loss < best_val_loss or best_val_loss is None:
        #     best_val_loss = val_loss
        #     patience_ = patience
        # else:
        #     patience_ -= 1
        #     if patience_ == 0:
        #         break

        # this will stop much earlier than the presented approach (but on the other hand is gauranteed to stop)
        


    #model = load_model(path)
    return model





            


