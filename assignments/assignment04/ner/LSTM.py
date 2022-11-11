import torch.nn.functional as F
import torch
from torch import nn
import numpy as np


class TokenLSTM(nn.Module):
    """
    An LSTM layer that takes in a sequence of tokens and returns a sequence of tags.
    """

    def __init__(
            self, output_dim: int, embedding_layer: nn.Embedding, hidden_dim_size: int
    ):
        super().__init__()

        # maps each token to an embedding_dim vector using our word embeddings
        self.embedding = embedding_layer

        self.embedding_size = embedding_layer.weight.shape[1]

        # the LSTM takes an embedded sentence
        self.lstm = nn.LSTM(self.embedding_size, 
                            hidden_dim_size,
                            bidirectional=True, # Notice that I'm using Bi-LSTM!
                            batch_first=True)

        # fc (fully connected) layer transforms the LSTM-output to give the final output layer
        self.fc = nn.Linear(hidden_dim_size*2, output_dim) # why am I using hidden_dim_size*2?

    def forward(self, X):
        # apply the embedding layer that maps each token to its embedding
        x = self.embedding(X)  # dim: batch_size x batch_max_len x embedding_dim

        # run the LSTM along the sentences of length batch_max_len
        x, _ = self.lstm(x)  # dim: batch_size x batch_max_len x lstm_hidden_dim

        # reshape the Variable so that each row contains one token
        # such that it is a valid input to the fully connected layer
        x = x.reshape(-1, x.shape[2])  # dim: batch_size*batch_max_len x lstm_hidden_dim

        # apply the fully connected layer and obtain the output for each token
        x = self.fc(x)  # dim: batch_size*batch_max_len x num_tags

        return F.log_softmax(x, dim=1)  # dim: batch_size*batch_max_len x num_tags

    @staticmethod
    def loss_fn(outputs, labels):
        """
        Custom loss function.
        In the section on preparing batches, we ensured that the labels for the PAD tokens were set to -1.
        We can leverage this to filter out the PAD tokens when we compute the loss.
        """
        # reshape labels to give a flat vector of length batch_size*seq_len
        labels = labels.view(-1)

        # mask out 'PAD' tokens
        mask = (labels >= 0).float()

        # the number of tokens is the sum of elements in mask
        num_tokens = int(torch.sum(mask))

        # pick the values corresponding to labels and multiply by mask
        outputs = outputs[range(outputs.shape[0]), labels] * mask

        # cross entropy loss for all non 'PAD' tokens
        return -torch.sum(outputs) / num_tokens

    def predict(self, X):
        """
        Function for converting the forward into an array of argmax results.
        """
        f = self.forward(X)
        return [np.argmax(token.detach().numpy()) for token in f]