# Class 8: Attention

*Note this class contains laTeX formula which is not rendered in GitHub*

## Preparations for class
No preparation required for the  class

<!--
Preperation for class could in the future be the first exercises and maybe a video on the dot product as a projection and the relation between cosine similarity and the dot product.
-->

## Plan for the class
- A2 Feedback
- dot product attention
- Introduction of A3, you can sign up for it [here](https://classroom.github.com/a/2Xsl5Qby).


## Exercises on Attention

In the following exercises, we will take a look at dot product attention, we will use word embeddings for this, however these would in the context of encoder-decoder models be hidden states from the decoder and encoder.

1) Calculate the dot product between two words embeddings that you believe are similar
```
import gensim.downloader as api
model = api.load("glove-wiki-gigaword-50")
```

2) Calculate the dot product between the two words and a word which you believe is dissimilar

3) make the three words into a matrix $E$ and multiply it with its own transpose using matrix multiplication. So $E \cdot E^T$
  - what do the entries in the matrix correspond to? What do you imagine the dot product is? *Hint*, the similarity between vectors (cosine similarity) is exactly the same as the dot product assuming you normalize the length of each vector to 1.

Following the article by Lindsay et al (2020) this is one way (out of many) to implement the attention mechanism denoted ${\tilde{\alpha_t}} = \phi(h_{t-1}, c) = h_{t-1} \cdot c^T$ (3.1) called dot product attention. 


4) Assume $h_{t-1}$ our previous hidden state is the word vector for "hei", calculate the attention the $h_{t-1}$ and the embeddings $\mathcal{E}_{greetings}$, $\mathcal{E}_{hello}$, $\mathcal{E}_{jungle}$. Remember that the attention weight is given by $\boldsymbol{\alpha_t} = softmax(\boldsymbol{\tilde{\alpha_t}})$ (3.2).


5) The matrix resulting from the softmax is referred to as the attention matrix and is how much each embedding should be weighted (paid attention to) when we multiply our attention matrix by our matrix embeddings consisting of $\mathcal{E}_{greetings}$, $\mathcal{E}_{hello}$, $\mathcal{E}_{jungle}$. Try it out:

- 5.1) This is essentially a weighted sum, one way to see this is to extract the weight from the first row of the matrix


```
attn = attention[0] # first row of our attention matrix
weighted = attn[0] * model["greetings"] + attn[1] * model["hello"] + attn[2] * model["jungle"]

# compare the weighted embedding with the first column in the matrix from 5).

matrix_from_5[0] - wieghted < 0.001
```

6) Create a function called attention to compute the dot product attention. It should take as input an embedding matrix corresponding to the $h$ and a matrix corresponding to $c$. It should return both the output, but also the attention matrix. Use to compute the dot product attention of the embeddings `["man", "banana"]` and `["woman", "apple", "pineapple"]`.

  - 6.1) Examine the attention matrix, which words have a higher attention weight and why?

*Hint* you can plot the matrix using:
```
H = model["man", "banana"]
C = model[["woman", "apple", "pineapple"]
wieghted, attn = attention(H, C)

import matplotlib.pyplot as plt
plt.matshow(attn)
plt.show()
```

Examining the attention formula from Vaswani et al. (2017):

$$
Attention(Q, K, V) = softmax(\frac{Q\cdot K^T}{\sqrt{d}}) \cdot V
$$
Where Q, K, V stands for queries, keys and values.

You have implemented it for the special case where $\sqrt{d} = 1$, however $d$ typically denote the dimension of the embedding (50 in our case).

>Optional:
>  - O.1) What does the Q, K, V correspond to in this case?
>  - O.2) Add the normalization ($\sqrt{d}$) to your function, how does this change the outcome?
>  - O.3) Check the class notebook on inspecting attention. This inspect the attention of a BERT model which we have naturally not looked at yet, but you might find it interesting that these attention layers can be visualized and interpreted. Thus the notebook is mostly to give you the tools to do so. You can mostly disregard the code (with the exception of maybe changing the sentence or the BERT model), but we can try to explore the attention in an actual model. I have written down a few attentions heads I found to be meaningful. Try to find one or two more.


## More on attention
- This [video](https://www.youtube.com/watch?v=0PjHri8tc1c&t=303s) takes you through the calculations step by step.
