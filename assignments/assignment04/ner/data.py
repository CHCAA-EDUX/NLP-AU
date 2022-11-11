"""
Contains function for loading, batching and converting data.
"""

from itertools import islice
from typing import Iterable, List, Tuple

import numpy as np
import torch

import datasets
from datasets.dataset_dict import DatasetDict

from gensim.models.keyedvectors import KeyedVectors
from torch import nn
import random


def load_data() -> DatasetDict:
    """Load the conllpp dataset.

    Returns:
        DatasetDict: A dictionary containing the train, test and dev sets.
    """
    dataset = datasets.load_dataset("conllpp")
    return dataset


def batch(dataset: Iterable, batch_size: int) -> Iterable:
    """Creates batches from an iterable.

    Args:
        dataset (Iterable): Your dataset you want to batch given as an iterable (e.g. a list).
        batch_size (int): Your desired batch size

    Returns:
        Iterable: An iterable of tuples of size equal to batch_size.

    Example:
        >>> batches = batch([1,2, 3, 4, 5], 2)
        >>> print(list(batches))
        [(1, 2), (3, 4), (5,)]
    """
    iterable_dataset = iter(dataset)
    while True:
        chunk = tuple(islice(iterable_dataset, batch_size))
        if not chunk:  # when the dataset/chunk is empty break the while loop
            break
        yield chunk


def gensim_to_torch_embedding(gensim_wv: KeyedVectors) -> Tuple[nn.Embedding, dict]:
    """
    Convert a gensim KeyedVectors object into a pytorch Embedding layer.

    Args:
        gensim_wv: gensim KeyedVectors object

    Returns:
        torch.nn.Embedding: torch Embedding layer
        dict: dictionary of word to index mapping
    """
    embedding_size = gensim_wv.vectors.shape[1]

    # create unknown and padding embedding
    unk_emb = np.mean(gensim_wv.vectors, axis=0).reshape((1, embedding_size))
    pad_emb = np.zeros((1, gensim_wv.vectors.shape[1]))

    # add the new embedding
    embeddings = np.vstack([gensim_wv.vectors, unk_emb, pad_emb])

    weights = torch.FloatTensor(embeddings)

    emb_layer = nn.Embedding.from_pretrained(embeddings=weights, padding_idx=-1)

    # creating vocabulary
    vocab = gensim_wv.key_to_index
    vocab["UNK"] = weights.shape[0] - 2
    vocab["PAD"] = emb_layer.padding_idx

    return emb_layer, vocab
    
def tokens_to_idx(tokens, vocab):
    """
    Ideas to understand this function:
    - Write documentation for this function including type hints for each arguement and return statement
    - What does the .get method do?
    - Why lowercase?
    """
    return [vocab.get(t.lower(), vocab["UNK"]) for t in tokens]

def prepare_batch(tokens: List[List[str]], labels: List[List[int]], vocab) -> Tuple[torch.Tensor, torch.Tensor]:
    """Prepare a batch of data for training.

    Args:
        tokens (List[List[str]]): A list of lists of tokens.
        labels (List[List[int]]): A list of lists of labels.

    Returns:
        Tuple[torch.Tensor, torch.Tensor]: A tuple of tensors containing the tokens and labels.
    """

    batch_tok_idx = [tokens_to_idx(sent, vocab) for sent in tokens]
    batch_size = len(tokens)

    # compute length of longest sentence in batch
    batch_max_len = max([len(s) for s in batch_tok_idx])

    # prepare a numpy array with the data, initializing the data with 'PAD'
    # and all labels with -1; initializing labels to -1 differentiates tokens
    # with tags from 'PAD' tokens
    batch_input = vocab["PAD"] * np.ones((batch_size, batch_max_len))
    batch_labels = -1 * np.ones((batch_size, batch_max_len))

    # copy the data to the numpy array
    for i in range(batch_size):
        tok_idx = batch_tok_idx[i]
        tags = labels[i]
        size = len(tok_idx)

        batch_input[i][:size] = tok_idx
        batch_labels[i][:size] = tags

    # since all data are indices, we convert them to torch LongTensors (integers)
    batch_input, batch_labels = torch.LongTensor(batch_input), torch.LongTensor(
        batch_labels
    )
    return batch_input, batch_labels
