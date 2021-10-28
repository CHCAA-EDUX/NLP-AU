## Class 7: Contextual embeddings using RNNs


## Preparation for class

No preparation is required for class. I recommend you spend your time finishing assignment 2, such that any questions you might have can be send to me before class.


## Plan for class:
- Introduction of NER
- introduce the varying length batches (padding)
- Exercises

## Exercise:
You likely won't have the time to finish this in class, but that is also not the intention as the next assignment you will get will build on this class in particular.

- 0) Get a broad overview of the code `main.py`. This includes getting an initial understanding of
  - The dataset
  - and the intention of the five steps:
    - DATASET
    - CONVERTING EMBEDDING
    - PREPARING A BATCH
    - CREATING MODEL
    - FORWARD PASS





<details>
    <summary>
This code used the PyTorch LSTM implementation, but I want to understand how to implement the LSTM cell!
    </summary>

Wonderful! However, the time doesn't allow for it, but you can take a look at the LSTM implementation [here](https://www.gushiciku.cn/pl/2A03/zh-tw). 
I also tried digging a bit deeper into the LSTM implementation in PyTorch but it is a C++ implementation.

</details>

<br /> 




- 1) Create documentation for the `gensim_to_torch_embedding` function to understand what it does
- 2) Convert the section "PREPARING A BATCH" into a function
- 3) Using this function create a new function that shuffles and batches the training dataset.

<details>
    <summary>
    You can conveniently use PyTorch dataset and dataloaders for this. This code should get you started with it.
    </summary>

```py
import torch


vocab= 1000
n_texts = 100

# create an example matrix 
tf_idf = torch.zeros(n_texts, vocab) 
# or X

labels = torch.zeros(n_texts)
# or y

from torch.utils.data import TensorDataset, dataloader

# create a dataset with X, y
ds = TensorDataset(tf_idf, labels)

# create a data loader, which shuffles and batches the dataset
loader = dataloader.DataLoader(ds, batch_size=10, shuffle=True)

for batch in loader:
    print(type(batch))
    print(len(batch))
    X, y = batch
    print(X.shape)
    print(y.shape)
    
    # fit model on each batch
    break # to only print once by stopping the loop
```


</details>

<br /> 


- 4) Examine the RNN class
  - Examine the `forward(...)` and discuss the changes to the dimensions
    - *Hint*: You can always perform one step at a time by calling a specific layer in the model, for instance `embedding_output = model.embedding(X)`
    - *Optional*: You will note that a part of the output of the LSTM block is ignored (the `_`), what does this contain and what might you use it for?
  - It uses a custom loss function. Why is this custom function important?
- 5) Evaluate the performance of the untrained model
  - For NER we, typically, use F1-score I recommend using the Scikit-learn [implementation](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.f1_score.html), which is a combined measure of precision and recall. Most of you might recall these, but as it is material from 1st semester it might be ideal to spend a few minutes discussing it.
- 6) Finally, train the model
  - Does the performance improve?
    - OPTIONAL: Some more detailed question you could answer is:
      - How does the model perform on longer or shorter sentences?
      - Is there a particular tag which the model has a hard time tagging?
      - If a model classifies a name incorrectly on the test set is it more likely to be a man than a woman? (You can for example use [*gender_guesser*](https://pypi.org/project/gender-guesser/) to figure out the gender)
      - Does changing the initial embeddings improve the performance of the model?
