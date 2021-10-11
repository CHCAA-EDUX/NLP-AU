
# Class 5: Classification and vectorization

## Preparation for class

Before the class you are required to:
- 1) have an implementation of logistic regression or at least a strong attempt.


## Plan for class

- 1) Feedback on assignment 1
- 2) Example solution for logistic regression
- 3) introduction to nn.Module
- 4) Exercises on using Neural networks for classification
  - Find a multilabel classification dataset on [huggingface datasets](https://huggingface.co/datasets?task_ids=task_ids:multi-class-classification&sort=downloads)
  - Apply train a multiclass classification neural network on it
    - Do note you will need to change out the binary cross entropy to [cross entropy](https://pytorch.org/docs/stable/generated/torch.nn.CrossEntropyLoss.html) and remove the sigmoid on the last layer (the cross entropy applied to softmax so you shouldn't)
- 5) Introduction to next assignment


## Assignment 1: General feedback
- Generally, very good, no groups with major problems or misunderstandings
  - A few were requested minor changes.
- (Minor) almost all should do a clean-up of their code and/or the repository before submission
- Future assignments will include a written where you will get a few lines to convey your solution.
  - It is especially convenient if you have questions or bugs which weren't solvable

## Assignment 2 

You can sign up for the assignment 2 [here](https://classroom.github.com/a/qmdoEYhh).

<!--
For next time:

Introduce people to the tfidf vectorizer (too much time was spent moving from text to input) 
-->