
# Class 3: Classification and vectorization

## Preparation for class


Summary, before the class you are required to:
- 1) have `torch` and `datasets` installed
- 2) inspect the dataset we will be using for the class
- 3) have a function for calculating document frequency and term frequency for a given list of tokens ready for class


### (py)Torch

Pytorch can be installed easily using:
```
pip install torch
```
However, if you find yourself in any problems do go to the [documentation](https://pytorch.org/get-started/locally/).

### Datasets
For this class we will be using the dataset, SST2. The stanford sentiment treebank. It is a part of a set of datasets called [GLUE](https://huggingface.co/datasets/glue)  (General Language Understanding Evaluation benchmark), which we can access using Huggingface's [datasets package](https://huggingface.co/docs/datasets/):

```
pip install datasets
```

> If interested know that you find of bunch of datasets using this package. To see all available check out their [dataset hub](https://huggingface.co/datasets).

To download and load the desired dataset simply run:
```py
from datasets import load_dataset

# load the sst2 dataset
dataset = load_dataset("glue", "sst2")

# select the train split
train = dataset["train"]
```

We can now examine the dataset. Below is a good start but it is maybe a good idea to explore the dataset more. For class we will be using only the list of labels and the list of sentences.
```py
print("Examining train set:")
print(train)
print(train.features)

print("Information about the dataset:")
print(train.info.description)
print("Homepage")
print(train.info.homepage)

print("Examining sentence")
print(type(train["sentence"]))
print(type(train["sentence"][0]))


print("Examining label")
print(type(train["label"]))
print(type(train["label"][0]))
# set takes all the unique values
print(set(train["label"]))

print("A few samples:")
for t in range(10):
    sent = train["sentence"][t]
    lab = train["label"][t]
    print(sent, "-",  lab)
```


### Term frequency
For the class you are required to have a function which takes in a list of strings and return a dictionary of term frequencies, where the term frequency is defined as:

```
tf(t,d) = count of t in d / number of words in d
```

where t is the term (word/token) and d is the document.


The structure of the function could look something like this:
```py
def term_freq(tokens: List[str]) -> dict:
    """
    Takes in a list of tokens (str) and return a dictionary of term frequency of each token
    """
    # your code
```

*Hint*: Recall last weeks exercise

### Document frequency: 
Similarly you are required to have a function which calculates the document frequency:

```
df(t) = occurrence of t in document
```

The structure of the function could look something like this:
```py
def doc_freq(List[List[str]]) -> dict:
    """
    Takes in a list of documents which each is a list of tokens and return a dictionary of frequencies for each token over all the documents. E.g. {"Aarhus": 20, "the": 2301, ...}
    """
    # your code
```


### TF-IDF: Term frequency inverse document frequency

For this class we will be calculating using the TF-IDF as input to our model. You might optionally want to look at this [medium](https://towardsdatascience.com/tf-idf-for-document-ranking-from-scratch-in-python-on-real-world-dataset-796d339a4089) article.



## Plan for class

- 1) Talk about the preperations for class
- 2) Introduction to pytorch
- 3) implement a logistic regression classifier in pytorch
- 4) apply the logistic regression for sentiment classification
  - First using term frequncies
  - then using tf-idf

To convert the dictionary created to a vector we will be uisng the[DictVectorizer](https://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.DictVectorizer.html) from sklearn:
```
from sklearn.feature_extraction import DictVectorizer
```

  - Then using tf-idf, recall that TF-IDF of a token in a document is defined as:

```
tf-idf(t, d) = tf(t, d) * idf(t)
```

Where the inverse document frequency is defined as:
```
idf(t) = log(N/(df(t) + 1))
```

Where N is the number of documents. 

> **Optional**: Consider why we add 1 and why we apply the log.

- 5) Compare performance what performs better? Is there things you could do to improve performance? Some things you might consider are:
    - Are all words relevant? Could we filter some of these?
    - Should "play", "playing", and "played" be considered different words or the same?
    - What about casing? Does it matter?
    - ...

> **Optional**: You can compare your performance on SST2 on the benchmark website [paperswithcode](https://paperswithcode.com/sota/sentiment-analysis-on-sst-2-binary). How far are you off state-of-the-art-models?


