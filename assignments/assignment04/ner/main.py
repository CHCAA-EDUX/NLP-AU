import argparse
import random
import numpy as np
import torch
import gensim.downloader as api
from data import batch, gensim_to_torch_embedding, load_data, prepare_batch
from LSTM import TokenLSTM
from seqeval.metrics import classification_report
import wandb

# w&b setup
# this should be made a bit smarter by adding args to the dictionary - I got lazy
wandb.init(project="classrooms", 
    entity="rdkm",
    config = {
        "learning_rate": 0.01,
        "epochs": 1000,
        "batch_size": 16,
        "model_name":"glove-wiki-gigaword-100"
    }
)

def train_model(model, optimizer, epochs, training, validation, vocab, patience):
    """
    A function for training the model.
    """
    best_val_loss = None
    X_val, y_val = prepare_batch(validation["tokens"], validation["ner_tags"], vocab)

    for epoch in range(epochs):
        for tokens, tags in training:
            # prepare data
            X, y = prepare_batch(tokens, tags, vocab)

            #forward
            y_hat = model(X)
            #loss & backward
            loss = model.loss_fn(y_hat, y)
            loss.backward()

            #optimizer
            optimizer.step()
            optimizer.zero_grad()

        #  periodically calculate loss on validation set
        if epoch % 5 == 0:
            y_hat = model(X_val)
            loss = model.loss_fn(y_hat, y_val)

            # save model if better than current best, else reduce patience
            if best_val_loss is None or loss < best_val_loss:
                best_val_loss = loss
                torch.save(model, 'model.pt')
                patience_ = patience
            else:
                patience_ -= 5
                if patience_ <= 0:
                    break


def main(gensim_embedding: str, batch_size: int, epochs: int, learning_rate: float, patience: int = 10, optimizer=0):
    """
    Main function for training and testing the model.
    """
    # set a seed to make the results reproducible
    torch.manual_seed(0)
    np.random.seed(0)
    random.seed(0)

    dataset = load_data()
    embeddings = api.load(gensim_embedding)

    # convert gensim word embedding to torch word embedding
    embedding_layer, vocab = gensim_to_torch_embedding(embeddings)

    # Preparing data
    # shuffle dataset
    train = dataset["train"].shuffle(seed=1)
    test = dataset["test"]
    validation = dataset["validation"]

    # number of classes for LSTM output (+1 for PAD)
    num_classes = train.features["ner_tags"].feature.num_classes

    # batch it using a utility function
    batches_tokens = batch(train["tokens"], batch_size)
    batches_tags = batch(train["ner_tags"], batch_size)

    # Initialize the model
    lstm = TokenLSTM(num_classes + 1, embedding_layer, 20)

    # Initialize optimizer
    if optimizer == 0:
        optimizer = torch.optim.AdamW(lstm.parameters(), lr=learning_rate)
    elif optimizer == 1:
        optimizer = torch.optim.Adam(lstm.parameters(), lr=learning_rate)
    else:
        optimizer = torch.optim.RMSprop(lstm.parameters(), lr=learning_rate)

    # train model with given settings
    train_model(lstm, optimizer, epochs, zip(batches_tokens, batches_tags), validation, vocab, patience)

    # Load the best model
    best = torch.load('model.pt')

    # test it on testing set
    X, y = prepare_batch(test["tokens"], test["ner_tags"], vocab)
    y_hat = best.predict(X)

    # reformat results by removing pad tokens and flattening
    y_hat_depadded = []
    pos = 0
    for sen in test["ner_tags"]:
        for i in range(pos, pos + len(sen)):
            y_hat_depadded.append(y_hat[i])
        pos += y.shape[1]

    # flatten the test sentences into a single list
    flat_tags = [item for sublist in test["ner_tags"] for item in sublist]
    
    # get actual label
    actual = []
    predicted = []
    ner_dict = {0:'O', 1:'B-PER', 2:'I-PER', 3:'B-ORG', 4:'I-ORG', 5:'B-LOC', 6:'I-LOC', 7:'B-MISC', 8:'I-MISC'}
    actual.append([ner_dict.get(k, k) for k in flat_tags])
    predicted.append([ner_dict.get(k, k) for k in y_hat_depadded])

    # calculate f1 and acc (currently the same number?)
    report = classification_report(actual, predicted)
    print(report)

    return None


def parseArguments():
    # Create argument parser
    parser = argparse.ArgumentParser()

    # Optional arguments
    parser.add_argument("-e", "--epochs", type=int, default=1000)
    parser.add_argument("-gE", "--gensim_embedding", type=str, default="glove-wiki-gigaword-100")
    parser.add_argument("-o", "--optimizer", type=int, default=1, help="0 for AdamW, 1 for Adam, 2 for RMSprop")
    parser.add_argument("-b", "--batch_size", type=int, default=5)
    parser.add_argument("-lr", "--learning_rate", type=float, default=0.01)
    parser.add_argument("-p", "--patience", type=int, default=20)

    # Parse arguments
    args = parser.parse_args()

    return args


if __name__ == "__main__":
    args = parseArguments()
    main(gensim_embedding=args.gensim_embedding, 
        epochs=args.epochs, 
        batch_size=args.batch_size,
        learning_rate=args.learning_rate, 
        patience=args.patience, 
        optimizer=args.optimizer)
