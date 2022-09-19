# Syllabus: Natural Language Processing #

**NB: The information presented here has been taken from the [AU Course Catalogue](https://kursuskatalog.au.dk/en/course/114478/Natural-Language-Processing). It should be viewed as indicative, rather than definitive. In the case of errors, the official AU version is binding.**

## Overview ##

The purpose of the course is to introduce students to advanced statistical methods used in the analysis of text and speech data. The course also introduces students to computational models used in speech and text recognition and prediction, and to models used to generate text and speech outputs in artificial intelligence systems, such as digital assistants and chat bots.

The course addresses how we can approach theoretical and applied topics in the cognitive sciences using computational linguistics and natural language processing tools. Examples may include probabilistic topic modelling, sentiment analysis, and word2vec semantic analysis. The course also addresses key ethical topics that arise from the analysis of freely available natural language data, and in the development of natural language processing software and technologies. 

This course builds on students’ background knowledge in statistics and statistical programming, and introduces students to working with large data sets. The course introduces students to ethical and philosophical topics.

### Academic Objectives ###
In the evaluation of the student’s performance, emphasis is placed on the extent to which the student is able to:

1. Knowledge:
    - contrast different natural language processing methods in terms of their strengths and weaknesses in different use contexts
    - explain how formal and computational analysis of natural language can provide insights into human cognition and behaviour
    - discuss ethical and philosophical issues connected to natural language processing technology applications.

2. Skills:
    - identify relevant data sources for specific research and applied questions
    - correctly choose and apply tools for analysing natural language data.

3. Competences:
    - critically reflect on and discuss theoretical and empirical implications of using natural language processing techniques
    - justify the choice between relevant methods and analyses used for specific research questions within the field of natural language processing
    - critically evaluate the appropriateness of a given method for a given natural language data set.

## Course Assessment ##

The examination consists of a take-home assignment on a topic of the student’s choice and a related practical product.

The assignment can be written individually or in groups of up to 4 students. Group assignments must be written in such a way that the contribution of each student, except for the introduction, thesis statement and conclusion, can form the basis of individual assessment. The assignment should clearly state which student is responsible for which section.

- Length for one student: 10-12 standard pages
- Length for two students: 17-22 standard pages
- Length for three students: 24-32 standard pages
- Length for four students: 31-42 standard pages

The scope and nature of the product must be relevant in relation to the content of the course and is subject to the approval of the teacher. It must be possible to submit the product digitally in a documented form which can be accessed by the examiner and co-examiner.

The product must be accompanied by a take-home assignment on a topic of the student’s choice, in which the student explains the relevance and methodological and theoretical basis of the product.
The assignment and the product must be submitted for assessment in the Digital Exam system before the deadline set in the examination plan. Assessment is based on an overall assessment of the take-home assignment and the practical product.

## Schedule ##

Each course element (1-13) is a four hour session, consisting of a 1hr lecture, 1hr coding task explanation, and 2hrs code-along session.

| Week  | Session | Lecture | Classroom  |Reading |
| :---: | :-----: | ----------| -------| ---|
|  36   |    1    | Introductions               | [Work stack - Slack, UCloud, Github](classes/class1.md)                   | 
|  37   |    2    | Simple text processing      | Basic NLP methods                    | _Hunston 2002, Chapters 1,2_       |
|  38   |    3    | Classification 1            | Logistic regression and vectorization| _Jurafsky & Martin 2020, Chapter5_ |
|  39   |    4    | Classification 2            | Neural networks with ```pytorch```   | _Nielsen 2019, Chapter 1_                     |
|  40   |         |       *NO TEACHING*         |                            |                                              |
|  41   |    5    | Word embeddings             | Exploring word embeddings  | _Mikolov et al 2013_                         |
|  42   |         |       *NO TEACHING*         |                            | _Urban and Gates (2019)_                     |
|  43   |    6    | Language Modelling 1        | Recurrent neural networks  |   _(No readings)_                            |
|  44   |    7    | Language Modelling 2        | (Self-) Attention          | _Vaswani et al 2017; Lindsay et al 2020_     |
|  45   |    8    | BERT                        | Project development        | _Rogers et al 2020_                         |
|  46   |   9    | More BERT                   | Exploring BERT             | _Ettinger 2020_                              |
|  47   |   10    | Project presentations       | Project presentations      | _Brown et al 2020_; Raffle et al 2019        |
|  48   |   11    | GPT-3 & T5                  | Prompt engineering         | _CRFM 2019_                                  |
|  49   |   12    | Social impact               | Project development  | _Mitchell et al. (2019)_; _Bender et al. (2021)_       |

Typically lectures take place Wednesday 08:00 - 10:00 at 1467-515 and classes 12:00 - 14:00 1467-215.


## Reading ##

## Bibliography of Assigned Readings
The assigned readings are a mixture of different kinds of papers. Some of them are considered fundamental papers in contemporary NLP or are at the outer limits of what is possible with today's state-of-the-art approaches. Others are focused on the relationship between NLP and other disciplines in the cognitive sciences, such as pscyhology, neuroscience, and psycholinguistics. 

Other suggested readings might be given in lectures related to more specific topics - these will not be compulsory, only for those who wish to explore a specific topic in more detail. However, the following assigned readings will be referred to during lectures, so make sure to read them!

* Bender, E.M., Gebru, T., McMillan-Major, A., Schmitchell, S. (2021). "On the Dangers of Stochastic Parrots: Can Language Models Be Too Big? 🦜". In Proceedings of FAccT 2021, pp.610-623.
* Brown, T.B., et al. (2020). "Language Models are Few-shot Learners", [arXiv:2005.14165](https://arxiv.org/abs/2005.14165) [cs.CL]
* Center for Research on Foundation Models (CRFM) (2019). "On the Opportunities and Risks of Foundation Models", [arXiv:2108.07258](https://arxiv.org/abs/2108.07258) [cs.LG]
* Ettinger, A. (2020). "What BERT is not: Lessons from a new suite of psycholinguistic diagnostics for language models", _Transactions of the Association for Computational Linguistics_, 8, 34–48.
* Hunston, S. (2002). _Corpora in Applied Linguistics_. Cambridge: Cambridge University Press.
* Jurafsky, D. & Martin, J.H. (2021). _Speech and Language Processing_, 3rd edition online pre-print. [Access](https://web.stanford.edu/~jurafsky/slp3/)
* Lindsay, G.W. (2020). "Attention in Psychology, Neuroscience, and Machine Learning", _Frontiers in Computational Neuroscience_, 14(29), 1-21.
* Mikolov, T., Chen, K., Corrado, G., & Dean, J. (2013). "Efficient Estimation of Word Representations in Vector Space". [arXiv:1301.3781](https://arxiv.org/abs/1301.3781) [cs.CL]
* Mitchell, M., Wu, S., Zaldivar, A., Barnes, P., Vasserman, L., Hutchinson, B., Spitzer, E., Raji, I.D., & Gebru, T. (2019). "Model Cards for Model Reporting". In *Proceedings of the Conference on Fairness, Accountability, and Transparency* (FAT* '19). _Association for Computing Machinery_, New York, NY, USA, 220–229.
* Nielsen, M. (2019). "Neural Networks and Deep Learning", available online [here](http://neuralnetworksanddeeplearning.com/). Accessible as single PDF [here](https://static.latexstudio.net/article/2018/0912/neuralnetworksanddeeplearning.pdf)
* Raffel, C., et al. (2020). "Exploring the Limits of Transfer Learning with a Unified Text-to-Text Transformer", [arXiv:1910.10683](https://arxiv.org/abs/1910.10683) [cs.LG]
* Rogers, A., Kovaleva, O., & Rumshisky, A. (2020). "A Primer in BERTology: what we know about about how BERT works", _Transactions of the Association for Computational Linguistics_, 8, 842-866.
* Urban, C.J & Gates, K.M. (2020). "Deep Learning: A Primer for Psychologists", _Psychological Methods_, 26(6), 743–773.
* Vaswani, A, Shazeer, N., Parmar, N., Uszkoreit, J., Jones, L., Gomez, A.N., Kaiser, Ł, & Polosukhin, I. (2017). "Attention is all you need", NIPS'17: Proceedings of the 31st International Conference on Neural Information Processing Systems.

## Additional Resources ###
The following resources are *not* compulsory assigned readings. Instead, these are a mixture of textbooks and other resources which can be used as reference texts. Specifically, these will be useful for people who want to improve their understanding of linear algebra and neural networks. I strongly recommend all of the textbooks by Gilbert Strang - he's a fantastically clear writer, which is a rare skill among mathematicians. VanderPlas (2016) is a useful reference text for basic data science using Python (pandas, matplotlib, scikit-learn). It's below the level we'll be working at but it's good to have nevertheless.

* Bittinger, M.L., Ellenbogen, D.J., & Surgent, S.A. (2012). _Calculus and its Applications, 10th Edition_. Boston, MA: Addison-Wesley.
* Goldberg, N. (2017). _Neural Network Methods for Natural Language Processing_. New York: Morgan & Claypool Publishers.
* Strang, G. (2009). _Introduction to Linear Algebra (4th Edition)_.  Wellesley, MA: Wellesley-Cambridge Press.
  * (2016). _Linear Algebra and its Applications, (5th Edition)_. Wellesley, MA: Wellesley-Cambridge Press.
  * (2019). _Linear Algebra and Learning from Data_. Wellesley, MA: Wellesley-Cambridge Press.
  * (2020). _Linear Algebra for Everyone_. Wellesley, MA: Wellesley-Cambridge Press.
* VanderPlas, J. (2016). _Python Data Science Handbook_. [Access](https://jakevdp.github.io/PythonDataScienceHandbook/)

## Slack Channel ##

We will use the "CogSci-AU" channel for class-related communication. Please ask (and answer) questions in this Slack channel. There is no such thing as a stupid or trivial question! If a classmates asks a question you know an answer to, try and answer. Slack is not only for instructor-student interaction, it is for all students to share knowledge and resources, and to get answers as fast as possible. 

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

Your experience in this class is important to me. If you have already established accommodations with Special Educational Support (SES), please communicate your approved accommodations to me at your earliest convenience so we can discuss your needs in this course. If you have not yet established services through SES, but have a temporary health condition or permanent disability that requires accommodations (conditions include but not limited to; mental health, attention-related, learning, vision, hearing, physical or health impacts), you are welcome to contact 8716 2720 (Monday & Thursday 9-12, Tuesday 13-15) or email sps@au.dk. SES offers resources and coordinates reasonable accommodations for students with disabilities and/or temporary health conditions. Reasonable accommodations are established through an interactive process between you, your instructor(s) and SES. It is the policy and practice of the Aarhus University to create inclusive and accessible learning environment and ensure that all students have the opportunity to educate themselves on equal terms even if they have a disability.