# Class 2

## Preparation for class

No preparation is required for the class.

## Plan for class

### Part 1
Create a corpus object which for each document in the folder `train_corpus` saves to an object the document ID, the text, the tokenization of the text and the sentences of the text. This can preferably be split into three tasks:
- 1) Loading in the files as text.
- 2) Segment the sentences in the text.
- 3) Tokenize each sentence.

If you wish to compare your tokenization with the reference you can do it using:

```python
from utility import check_tokenization
```

Remember you can find out more about the function using `help(check_tokenization)`. *Note* tokenization is hard (and often debatable), don't focus all your energy on obtaining perfect tokenization as defined by the reference.

### Part 2
Calculate the pointwise mutual information (PMI or MI) for each word in the text. Recall that PMI can  be calculated as:

$$
PMI(w_1, w_2) = log \frac{p(w_1, w_2)}{p(w_1) \cdot p(w_2)}
$$

Where $w_i$ is a words. This is equivalent to calcuting the ratio between the observed cooccurances between $w_1$ and $w_2$ and the expected cooccurances given the word frequencies and is essentially a measure for how much more- or less likely we are to see the two words co-occur. For this task let us define cooccurance as being a part of the same bigram.

> *Note*: When dealing with the logs you can always rewrite multiplication into addition e.g. $log(a \cdot b) = log(a) + log(b)$. This is computationally faster and prevents numerical errors when dealing with very low or very high probabilities.

This task can reasonable be split into a couple of subtask:
  - 1) Calculating the frequncies of each word.
  - 2) Calculate the frequency of each bigram.
  - 3) From this calculate the PMI of the words in the corpus.
  