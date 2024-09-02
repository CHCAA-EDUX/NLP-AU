# Class 2: SpaCy and document vectors

This classroom will introduce you one of the most widely-used NLP frameworks in both academia and industry.

In the lecture this week, we saw that language is not simply just a series of character strings. Instead, language comprises words which have their own special properties, such as word class, grammatical relations, and so on. spaCy is a flexible and user-friendly way of annotating text strings to provide this kind of extra information, in the form of a new data type known as a Doc.

For the rest of this semester, we'll be more interested in the machinary and architecture underlying a tool like spaCY than using it directly for linguistic analysis of data. But it's good to start by seeing what kind of things are possible with NLP tools, when we have good language models and deep learning frameworks to build on.

In addition to this, we will also experiment with `scikit-learn`, a powerful machine learning framework with extremely useful utilities to implement some of the methods we have discussed in the Lecture (e.g., term-document counts, and Tf-Idf methods). The second notebook for this class guides you through using scikit-learn to represent documents, and guides you through a very, very basic implementation of sentiment classification based on count (and Tf-Idf) vectors.