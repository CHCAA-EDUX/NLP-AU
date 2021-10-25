## Class 7: Contextual embeddings using RNNs


## Preparation for class

No preparation is required for class. I recommend you spend your time finishing assignment 2, such that any questions you might have can be send to me before class.


## Plan for class:
- Introduction of NER
- introduce the varying length batches (padding)
- Exercises

## Exercise:
You likely won't have the time to finish this in class, but that is also not the intention as the next assignment you will get will build on this class in particular.

- 0) Get a broad overview of the code `main.py`. This include getting an initial understanding of
  - The dataset
  - and the intention of the 5 steps:
    - DATASET
    - CONVERTING EMBEDDING
    - PREPARING A BATCH
    - CREATING MODEL
    - FORWARD PASS

- 1) Create documentation for the `gensim_to_torch_embedding` function to understand what it does
- 2) Convert the section "PREPARING A BATCH" into a function
- 3) Using this function create a new function which shuffles and batches the training dataset
- 4) Examine the RNN class
  - Examine the `forward(...)` and discuss the changes to the dimensions
    - *Hint*: You can always perform one step at a time by calling a specific layer in the model, for instance `embedding_output = model.embedding(X)`
    - *Optional*: You will note that a part of the output of the LSTM block is ignored (the `_`), what does this contain and what might you use it for?
  - It uses a custom loss function. Why is this custom function important?
- 5) Evaluate the performance of the untrained model
  - Typically for NER we use F1-score feel free to use the sklearn [implementation](https://scikit-learn.org/stable/modules/generated/sklearn.metrics.f1_score.html), which is combined measure of precision and recall. Most of you do know these, but as it is 1-semester stuff it might be ideal to discuss it.
- 6) Finally, train the model
  - Does the performance improve?
    - Some more detailed question you could answer is:
      - How does the model perform on longer or shorter sentence?
      - Is there a particular tag which the model have a harder time dealing with?
      - If a model classifies a name incorrectly on the test set is it more likely to be a man that a woman? (You can e.g. use [*gender_guesser*](https://pypi.org/project/gender-guesser/) to figure out the gender)
      - Does changing the initial embeddings improve the performance of the model?
