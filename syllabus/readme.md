# Syllabus Cultural Data Science - Language #

## Overview ##

The purpose of the course is to introduce students to advanced statistical methods used in the analysis of text and speech data. The course also introduces students to computational models used in speech and text recognition and prediction, and to models used to generate text and speech outputs in artificial intelligence systems, such as digital assistants and chat bots.

The course addresses how we can approach theoretical and applied topics in human cognition using computational linguistics and natural language processing tools. The course also addresses key ethical topics that arise from the analysis of freely available natural language data, and in the development of natural language processing software and technologies.

This course builds on students’ background knowledge in statistics and statistical programming, and introduces students to working with large data sets. The course builds towards the data science course. The course introduces students to ethical and philosophical topics, which will be extended on in the data science course. The course prepares students for careers involving analysis of text and other forms of natural language data, and for careers involving development of natural language software.

### Academic Objectives ###

In the evaluation of the student’s performance, emphasis is placed on the extent to which the student is able to:

1. Knowledge:

* contrast different natural language processing methods in terms of their strengths and weaknesses in different use contexts
* explain how formal analysis of natural language can provide insights into human cognition and behaviour
* discuss ethical and philosophical issues connected to natural language processing software and technology.

2. Skills:

* identify relevant data sources for specific research and applied questions
* correctly choose and apply tools for analysing natural language data.

3. Competences:

* critically reflect on and discuss theoretical and empirical implications of using natural language processing techniques
* justify the choice between relevant methods and analyses used for specific research questions within the field of natural language processing
* clear oral presentation of complex analyses.

## Course Assessment ##

The exam is an individual oral exam based on a written synopsis. The duration is 30 minutes including the student’s presentation of the synopsis project, followed by dialogue with the examinators and assessment.

The synopsis can be done as an individual or group assignment. If it is done as a group assignment, the final product must (i) form a coherent text and (ii) be organized so that it is possible to make individual assessments of the students contributing. In other words, the contribution of each individual student to the whole assignment must be clearly delineated (excluding the introduction, conclusion and bibliography).

A maximum of three students can take part in a group assignment.

* Length of individual synopsis: 4-7 standard pages (not including code and figures)
* Length of synopsis for 2 students: 8-14 standard (not including code and figures)
* Length of synopsis for 3 students: 12-21 standard (not including code and figures)

## Schedule ##

Each course element (1-13) is a four hour session, consisting of a 1hr lecture, 1hr coding task explanation, and 2hrs code-along session.

| Week  | Session | Lecture                     | Classroom                                                               | Reading                                      |
| :---: | :-----: | --------------------------- | ----------------------------------------------------------------------- | -------------------------------------------- |
|  36   |    1    | Introductions               | [Work stack - Slack, UCloud, Github](classes/class1.md)                 | --                                           |
|       |    2    | Simple text processing      | [Tokenization, word counts, collocation](classes/class2/class2.md)      | _Hunston 2002, Chapters 1,2 4_               |
|       |    3    | From text processing to NLP | [Lemmatization, part-of-speech, dependencies](classes/class3/class3.md) | _spaCy documentation, Enevoldsen et al 2021_ |
|       |    4    | Classification 1            | [Logistic regression and vectorization](classes/class4/class4.md)       | _Jurafsky & Martin 2020, Chapter 5_          |
|       |    5    | Classification 2            | [Neural networks with pytorch](classes/class5/class5.md)                       | _Nielsen 2019, Chapter 1 (and throughout!)_  |
|       |    6    | Word embeddings             | Named Entity Recognition                                                | _Mikolov et al 2013; Pennington et al 2014_  |
| BREAK |         |                             |                                                                         |                                              |
|  43   |    7    | Language Modelling 1        | Recurrent Neural Networks, Long short-term memory networks              | _Urban & Gates 2020_                         |
|       |    8    | Language Modelling 2        | Attention                                                               | _Vaswani et al 2017; Lindsay et al 2020_     |
|       |    9    | BERT                        | Implementing (parts of) BERT                                            | _Devlin et al 2019_                          |
|       |   10    | Project presentations       | Implementing (parts of) BERT                                            | _Ettinger 2020; Rogers et al 2020_           |
|       |   11    | More BERT                   | Exploring layers                                                        | _Coenen et al 2019_                          |
|       |   12    | Data bias and ethics        | Augmentation and data bias                                              | _van Miltenburg et al 2021_                  |

## Reading ##

## Bibliography of Assigned Readings
The assigned readings are a mixture of different kinds of papers. Some of them are considered fundamental papers in contemporary NLP or are at the outer limits of what is possible with today's state-of-the-art approaches. Others are focused on the relationship between NLP and other disciplines in the cognitive sciences, such as pscyhology, neuroscience, and psycholinguistics. 

Other suggested readings might be given in lectures related to more specific topics - these will not be compulsory, only for those who wish to explore a specific topic in more detail. However, the following assigned readings will be referred to during lectures, so make sure to read them!

* Coenen, A., Reif, E., Yuan, A., Kim, B., Pearce, A., Viégas, F., Wattenberg, M. (2020). "Visualizing and Measuring the Geometry of BERT", 33rd Conference on Neural Information Processing Systems.
* Devlin, J., Chang, M., Lee, K., & Toutanova, K. (2019). "BERT: Pre-training of Deep Bidirectional Transformers for Language Understanding", _Proceedings of NAACL-HLT 2019_, 4171–4186.
* Enevoldsen, K., Hansen, L., & Nielbo, K.L (2021). "DaCy: A Unified Framework for Danish NLP", arXiv:2107.05295 [cs.CL]
* Ettinger, A. (2020). "What BERT is not: Lessons from a new suite of psycholinguistic diagnostics for language models", _Transactions of the Association for Computational Linguistics_, 8, 34–48.
* Honnibal, M., Montani, I., Van Landeghem, S., & Boyd, A. (2020). "spaCy: Industrial-strength natural language processing in python". Zenodo. <https://doi.org/10.5281/zenodo.1212303>
* Hunston, S. (2002). _Corpora in Applied Linguistics_. Cambridge: Cambridge University Press.
* Jurafsky, D. & Martin, J.H. (2021). _Speech and Language Processing_, 3rd edition online pre-print. [Access](https://web.stanford.edu/~jurafsky/slp3/)
* Lindsay, G.W. (2020). "Attention in Psychology, Neuroscience, and Machine Learning", _Frontiers in Computational Neuroscience_, 14(29), 1-21.
* Mikolov, T., Chen, K., Corrado, G., & Dean, J. (2013). "Efficient Estimation of Word Representations in Vector Space". [arXiv:1301.3781](https://arxiv.org/abs/1301.3781) [cs.CL]
* Nielsen, M. (2019). "Neural Networks and Deep Learning", available online [here](http://neuralnetworksanddeeplearning.com/). Accessible as single PDF [here](https://static.latexstudio.net/article/2018/0912/neuralnetworksanddeeplearning.pdf)
* Pennington, J., Socher, R., & Manning, C.D. (2014). "GloVe: Global Vectors for Word Representation", Proceedings of the 2014 Conference on Empirical Methods in Natural Language Processing (EMNLP), 1532-1543.
* Rogers, A., Kovaleva, O., & Rumshisky, A. (2020). "A Primer in BERTology: what we know about about how BERT works", _Transactions of the Association for Computational Linguistics_, 8, 842-866.
* Urban, C.J & Gates, K.M. (2020). "Deep Learning: A Primer for Psychologists", _Psychological Methods_.
  * (NB: Article to be published 2022, open source pre-print available through library.)
* van Miltenburg, E., van der Lee, C., Krahmer, E. (2021). "Preregistering NLP research", _Proceedings of the 2021 Conference of the North American Chapter of the Association for Computational Linguistics: Human Language Technologies_, 613-623.
* Vaswani, A, Shazeer, N., Parmar, N., Uszkoreit, J., Jones, L., Gomez, A.N., Kaiser, Ł, & Polosukhin, I. (2017). "Attention is all you need", NIPS'17: Proceedings of the 31st International Conference on Neural Information Processing Systems.

## Additional Resources ###
The following resources are *not* compulsory assigned readings. Instead, these are a mixture of textbooks and other resources which can be used as reference texts. Specifically, these will be useful for people who want to improve their understanding of linear algebra and neural networks. I strongly recommend all of the textbooks by Gilbert Strang - he's a fantastically clear writer, which is a rare skill among mathematicians. VanderPlas (2016) is a useful reference text for basic data science using Python (pandas, matplotlib, scikit-learn). It's below the level we'll be working at but it's good to have nevertheless.

* Goldberg, N. (2017). _Neural Network Methods for Natural Language Processing_. New York: Morgan & Claypool Publishers.
* Strang, G. (2009). _Introduction to Linear Algebra (4th Edition)_.  Wellesley, MA : Wellesley-Cambridge Press.
  * (2016). _Linear Algebra and its Applications, (5th Edition)_. Wellesley, MA : Wellesley-Cambridge Press.
  * (2019). _Linear Algebra and Learning from Data_. Wellesley, MA : Wellesley-Cambridge Press.
  * (2020). _Linear Algebra for Everyone_. Wellesley, MA : Wellesley-Cambridge Press.
* VanderPlas, J. (2016). _Python Data Science Handbook_. [Access](https://jakevdp.github.io/PythonDataScienceHandbook/)

## Slack Channel ##

We will use the "NLP-E21" channel for class-related communication. Please ask (and answer) questions in this Slack channel. There is no such thing as a stupid or trivial question! If a classmates asks a question you know an answer to, try and answer. Slack is not only for instructor-student interaction, it is for all students to share knowledge and resources, and to get answers as fast as possible. 

Slack is best-suited for short technical questions and individual threads or channels for extended conversations on a given topic.

## Rules of Slack ##

1. use your github username or post.au.dk address to register and use the channel.
2. post on the general, spatial-analytics, or other relevant channel instead of direct messaging instructors.
3. use proper formatting: When asking questions involving code, please make sure to use inline code formatting for short bits of code or code snippets for longer, multi-line chunks
    * Formatting messages: <https://get.slack.help/hc/en-us/articles/202288908-Format-your-messages>
    * Code snippets: <https://get.slack.help/hc/en-us/articles/204145658-Creating-a-Snippet>
4. For specific coding advise, please use minimal reproducible examples, e.g. <https://stackoverflow.com/questions/5963269/how-to-make-a-great-r-reproducible-example>

## Asking questions (on Slack, in class, and elsewhere) ##

1. Google It First! Google the error Python gives you. English language errors will have more solutions online.
2. Search existing online resources (Google, StackOverflow, etc.) and class discussion on Slack for answers. If the question has already been answered, you're done!
3. If it has already been asked but you're not satisfied with the answer, refine your question to get the answer you need, and add to the thread.
    * Document the questions you ask and the responses.
    * Give your question context from course concepts not course assignments
        * Good context: "I have a question on POS tagging"
        * Bad context: "I have a question on HW 1 question 4"
    * Be precise in your description:
        * Good description: "I am getting the following error and I'm not sure how to resolve it - ```ImportError: No module named spacy```"
        * Bad description: "Python is giving me errors."
    * You can edit a question in Slack after posting it.

## Disability Resources ##

Your experience in this class is important to me. If you have already established accommodations with Special Educational Support (SES), please communicate your approved accommodations to me at your earliest convenience so we can discuss your needs in this course. If you have not yet established services through SES, but have a temporary health condition or permanent disability that requires accommodations (conditions include but not limited to; mental health, attention-related, learning, vision, hearing, physical or health impacts), you are welcome to contact 8716 2720 (Monday & Thursday 9-12, Tuesday 13-15) or email sps@au.dk. SES offers resources and coordinates reasonable accommodations for students with disabilities and/or temporary health conditions. Reasonable accommodations are established through an interactive process between you, your instructor(s) and SES. It is the policy and practice of the Aarhus University to create inclusive and accessible learning environment and ensure that all students have the opportunity to educate themselves on equal terms even if they have a disability
