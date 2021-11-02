# Class 8: Attention

## Preperations for class
No preperations for class

## Plan for the class
- A2 Feedback
- dot product attention
- Vote for the coming classes
  - More understanding BERT or more applying BERT
- Introduction of A3



## Exercises on Attention

- 1) Calculate the dot product between two word embedding which you believe are similar
```
import gensim.downloader as api
model = api.load("glove-wiki-gigaword-50")
```

- 2) Calculate the dot product between the two word and a word which you believe is dissimilar

- 3) make the three words into a matrix $E$ and multiply it with its own transpose using matrix multiplication. So $E \cdot E^T$
  - what does the values in matric correspond to? What do you imagine the dot product is? *Hint*, similarity between vectors (cosine similarity) is exactly the same as the dot product assuming you normalize the lenghth of each vector to 1.

- 4) Examine the attention formula from Vaswani et al. (2017), you have now implemented $Q\cdot K^T$

$$
Attention(Q, K, V) = softmax(\frac{Q\cdot K^T}{\sqrt{d}}) \cdot V
$$
Where $d$ is the dimension of of the embedding and Q, K, V stands for queries, keys and values.


  - 4.1) Now add the softmax. Examining the outcome, how come that the matrix is no longer symmetric?
  - 4.2) Now normalize the using the $\sqrt{d}$, how does this change the outcome?

1) the matrix resulting from the softmax is referred to as the attention matrix and is how much each matrix should pay attention to the others when we multiply our attention matrix by our matrix $E$ (corresponding to $V$). Try it out:

- 5.1) This is essentially a weighted sum, one way to see this is to extract the weight from the first row of the matrix


```
attn = attention[0] # first row
weighted = attn[0] * E[0] + attn[1] * E[1] + attn[2] * E[2]

# compare the wieghted embedding with the first column in the matrix from 5.
```

There is one problem here. Naturally we have here assumed that Q, K and V is the same
Which is not the case. As this is a static function the model really have no
oppurtunity guide the attention, for example if I see the word "you" it might be
relevant to gain information from word embedddings which look like entities.
The way they solve this in the paper is simply by creating Q, K and V
taking it them through a one layer neural network (without a bias) where the weights can be learned using
gradient descent.

6) now I want to create a function called attention to compute the scaled dot product attention presented above. It should return both the output, but also the attention matrix. Use to compute the scaled dot product attention of the embeddings `["man", "woman", "apple", "banana", "pineapple"]` (you shouldn't use any learned weights).

    - 6.1) Examine the attention matrix, which words have a higher attention weight and why?

*Hint* you can plot the matrix using:
```
import matplotlib.pyplot as plt
plt.matshow(attention)
plt.show()
```

- 7) Check the class notebook on inspecting attention. You should mostly disregard the code (with the exception of maybe changing the sentence), but we can now try to explore the attention in an actual model. I have written down a few attentions heads I found to be meaningful. Try to find one or two more.

## More on attention
- This [video](https://www.youtube.com/watch?v=0PjHri8tc1c&t=303s) takes you through the calculations step by step.
