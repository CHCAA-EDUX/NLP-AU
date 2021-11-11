"""
This script contains pseudo-code for training a neural network with early stopping.
Thus the code is not intended to be executable.
"""

from typing import Callable, Iterable
from torch import nn

def train(model: nn.Module,
          epochs: int,
          batches: Iterable,
          loss_fn: Callable,
          val_X, val_y,
          patience: int) -> nn.Module:
    """[summary]

    Args:
        model (nn.Module): [description]
        epochs (int): [description]
        batches (Iterable): [description]
    """
    # initialize an optimizer
    optimizer = ...

    val_losses = []
    best_val_loss = None

    # or alternatively
    # while True:
    for epoch in epochs:
        
        # set the moded to train mode (allow the models parameters to be updated)
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
        model.eval() # set the model to evaluation mode (i.e. disable gradients)
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





            


