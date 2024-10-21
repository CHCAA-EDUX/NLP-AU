# Syllabus: Natural Language Processing

**NB: The information presented here has been taken from the [AU Course Catalogue](https://kursuskatalog.au.dk/en/course/123489/Natural-Language-Processing). It should be viewed as indicative, rather than definitive. In the case of errors, the official AU version is binding.**

## Overview

### Purpose:

The purpose of the course is to introduce students to advanced statistical methods used in the analysis of text and speech data. The course also introduces students to computational models used in speech and text recognition and prediction, and to models used to generate text and speech outputs in artificial intelligence systems, such as digital assistants and chat bots.

The course addresses how we can approach theoretical and applied topics in the cognitive sciences using computational linguistics and natural language processing tools. Examples may include probabilistic topic modelling, sentiment analysis, and word2vec semantic analysis. The course also addresses key ethical topics that arise from the analysis of freely available natural language data, and in the development of natural language processing software and technologies.

This course builds on students’ background knowledge in statistics and statistical programming, and introduces students to working with large data sets. The course introduces students to ethical and philosophical topics.

### Academic Objectives

In the evaluation of the student’s performance, emphasis is placed on the extent to which the student is able to:

1.  Knowledge:
    -   contrast different natural language processing methods in terms of their strengths and weaknesses in different use contexts
    -   explain how formal and computational analysis of natural language can provide insights into human cognition and behaviour
    -   discuss ethical and philosophical issues connected to natural language processing technology applications.
2.  Skills:
    -   identify relevant data sources for specific research and applied questions
    -   correctly choose and apply tools for analysing natural language data.
3.  Competences:
    -   critically reflect on and discuss theoretical and empirical implications of using natural language processing techniques
    -   justify the choice between relevant methods and analyses used for specific research questions within the field of natural language processing
    -   critically evaluate the appropriateness of a given method for a given natural language data set.

## Course Assessment

The examination consists of a take-home assignment on a topic of the student’s choice and a related practical product.

The assignment can be written individually or in groups of up to 4 students. Group assignments must be written in such a way that the contribution of each student, except for the introduction, thesis statement and conclusion, can form the basis of individual assessment. The assignment should clearly state which student is responsible for which section.

-   Length for one student: 10-12 standard pages
-   Length for two students: 17-22 standard pages
-   Length for three students: 24-32 standard pages
-   Length for four students: 31-42 standard pages

The scope and nature of the product must be relevant in relation to the content of the course and is subject to the approval of the teacher. It must be possible to submit the product digitally in a documented form which can be accessed by the examiner and co-examiner.

The product must be accompanied by a take-home assignment on a topic of the student’s choice, in which the student explains the relevance and methodological and theoretical basis of the product. The assignment and the product must be submitted for assessment in the Digital Exam system before the deadline set in the examination plan. Assessment is based on an overall assessment of the take-home assignment and the practical product.

## Schedule

Each course element (1-12) is a four hour session, consisting of a 2hr lecture and 2hrs coding session.

| Week  | Session | Lecture                                                  | Classroom                                | Reading                                                                                                                                                                                                                                                                                                                                                                             |
| :---: | :-----: | -------------------------------------------------------- | ---------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
|  37   |    1    | Introduction to NLP                                      | Ucloud, Github, Prompting                | [Manning 2015](https://www.mitpressjournals.org/doi/pdf/10.1162/COLI_a_00239), Philosophy of understanding (§2.6 of the "Foundation Models" [report](https://crfm.stanford.edu/assets/report.pdf#philosophy)), [Artificial Intelligence: Last Week Tonight](https://youtu.be/Sqa8Zo2XWc4), [Montani 2024](https://ines.io/blog/window-knocking-machine-test/)                       |
|  38   |    2    | Word representations and vector spaces                   | Exploring word vectors                   | *Jurafsky & Martin 2020, Chapter6, pp.5-28*; *Pennington et al., 2014*                                                                                                                                                                                                                                                                                                              |
|  39   |         |                                                          |                                          |                                                                                                                                                                                                                                                                                                                                                                                     |
|  40   |    3    | Document representations                                 | Classification from representations      | *Baroni et al., 2014* (spend the extra time to go to the NLP worksop)                                                                                                                                                                                                                                                                                                               |
|  41   |    4    | Neural Networks                                          | Neural networks with `pytorch`           | *Nielsen 2019, Chapter 1*, 3Blue1Brown Videos (ch.[1](https://www.youtube.com/watch?v=aircAruvnKk&list=PLZHQObOWTQDNU6R1_67000Dx_ZCJB-3pi), [2](https://www.youtube.com/watch?v=IHZwWFHWa-w&list=PLZHQObOWTQDNU6R1_67000Dx_ZCJB-3pi&index=2))                                                                                                                                       |
|  43   |    5    | Contextual Embeddings I, Attention                       | Comparing contextual vectors             | *Vaswani et al 2017*; *Lindsay et al 2020* 3Blue1Brown Videos (ch. [5](https://www.youtube.com/watch?v=wjZofJX0v4M&list=PLZHQObOWTQDNU6R1_67000Dx_ZCJB-3pi&index=5), [6](https://www.youtube.com/watch?v=eMlx5fFNoYc&list=PLZHQObOWTQDNU6R1_67000Dx_ZCJB-3pi&index=6), optionally [7](https://www.youtube.com/watch?v=9-Jl0dxWQs8&list=PLZHQObOWTQDNU6R1_67000Dx_ZCJB-3pi&index=7)) |
|  44   |    6    | Contextual Embeddings II, Language generation            | Prompt engineering                       | Brown et al 2020; Raffel et al 2019                                                                                                                                                                                                                                                                                                                                                 |
|  45   |    7    | Contextual Embeddings III, Transfer learning and Probing | Probing                                  | Devlin et al., 2019; Rogers et al., 2020; Hewitt, 2019                                                                                                                                                                                                                                                                                                                              |
|  46   |    8    | Instruction tuning                                       | Training a model with instruction tuning | *Wei et al., 2021*; *Ouyang et al., 2022*                                                                                                                                                                                                                                                                                                                                           |
|  47   |    9    | Evaluation                                               | Evaluating NLP Systems                   | Wang et al., 2018; Zheng et al., 2023; Chiang et al., 2024; Optional:  Glockner et al., 2018                                                                                                                                                                                                                                                                                        |
|  48   |   10    | Project presentation                                     | Project feedback                         |  Preperation of project presentations                                                                                                                                                                                                                                                                                                                                                                                   |
|  49   |   11    | Group presentation on LLM and cognition                  | Retrieval augmented generation           | Lewis et al., 2020; *group-specific readings*                                                                                                                                                                                                                                                                                                                                       |
|  50   |   12    | Ethics and social impact                                 | Project development                      | *Bender et al., 2021*; *Mitchell et al., 2019*                                                                                                                                                                                                                                                                                                                                      |

## Reading

## Bibliography of Assigned Readings

The assigned readings are a mixture of different kinds of papers. Some of them are considered fundamental papers in contemporary NLP or are at the outer limits of what is possible with today's state-of-the-art approaches. Others are focused on the relationship between NLP and other disciplines in the cognitive sciences, such as pscyhology, neuroscience, and psycholinguistics.

Other suggested readings might be given in lectures related to more specific topics - these will not be compulsory, only for those who wish to explore a specific topic in more detail. However, the following assigned readings will be referred to during lectures, so make sure to read them!

-   Baroni, M., Dinu, G., Kruszewski, G. (2014). "Don’t count, predict! a systematic comparison of context-counting vs. context-predicting semantic vectors." In Proceedings of the 52nd Annual Meeting of the Association for Computational Linguistics (Volume 1: Long Papers), pp. 238-247 (available [here](https://aclanthology.org/P14-1023/)) 
-   Bender, E.M., Gebru, T., McMillan-Major, A., Schmitchell, S. (2021). "On the Dangers of Stochastic Parrots: Can Language Models Be Too Big? 🦜". In Proceedings of FAccT 2021, pp.610-623 (available [here](https://dl.acm.org/doi/10.1145/3442188.3445922))
    * Brown, T.B., et al. (2020). "Language Models are Few-shot Learners", [arXiv:2005.14165](https://arxiv.org/abs/2005.14165) [cs.CL]
    * Devlin, J., Chang, M. W., Lee, K., & Toutanova, K. (2018). "Bert: Pre-training of deep bidirectional transformers for language understanding". [arXiv:1810.04805](https://arxiv.org/abs/1810.04805). -->
-   Jeffrey Pennington, Richard Socher, and Christopher Manning. 2014. GloVe: Global Vectors for Word Representation. In Proceedings of the 2014 Conference on Empirical Methods in Natural Language Processing (EMNLP), pages 1532–1543, Doha, Qatar. Association for Computational Linguistics (available [here](https://aclanthology.org/D14-1162/))
-   Jurafsky, D. & Martin, J.H. (2021). *Speech and Language Processing*, 3rd edition online pre-print. [Access](https://web.stanford.edu/~jurafsky/slp3/);
-   Lindsay, G.W. (2020). "Attention in Psychology, Neuroscience, and Machine Learning", *Frontiers in Computational Neuroscience*, 14(29), 1-21 (available [here](https://www.frontiersin.org/articles/10.3389/fncom.2020.00029/full))
-   Mikolov, T., Chen, K., Corrado, G., & Dean, J. (2013). "Efficient Estimation of Word Representations in Vector Space". [arXiv:1301.3781](https://arxiv.org/abs/1301.3781) \[cs.CL\] 
-   Mitchell, M., Wu, S., Zaldivar, A., Barnes, P., Vasserman, L., Hutchinson, B., Spitzer, E., Raji, I.D., & Gebru, T. (2019). "Model Cards for Model Reporting". In *Proceedings of the Conference on Fairness, Accountability, and Transparency* (FAT* '19). _Association for Computing Machinery_, New York, NY, USA, 220–229 (available [here](https://arxiv.org/abs/1810.03993)) -->
-   Nielsen, M. (2019). "Neural Networks and Deep Learning", available online [here](http://neuralnetworksanddeeplearning.com/). Accessible as single PDF [here](https://static.latexstudio.net/article/2018/0912/neuralnetworksanddeeplearning.pdf) 
-   Ouyang, L., Wu, J., Jiang, X., Almeida, D., Wainwright, C., Mishkin, P., ... & Lowe, R. (2022). "Training language models to follow instructions with human feedback". In *Advances in Neural Information Processing Systems*, 35
-   Raffel, C., et al. (2020). "Exploring the Limits of Transfer Learning with a Unified Text-to-Text Transformer", [arXiv:1910.10683](https://arxiv.org/abs/1910.10683) [cs.LG]
-  Rogers, A., Kovaleva, O., & Rumshisky, A. (2020). "A Primer in BERTology: what we know about about how BERT works", _Transactions of the Association for Computational Linguistics_, 8, 842-866 (available [here](https://aclanthology.org/2020.tacl-1.54/))
-  Urban, C.J & Gates, K.M. (2020). "Deep Learning: A Primer for Psychologists", _Psychological Methods_, 26(6), 743–773 (available [here](https://psycnet.apa.org/record/2021-31499-001)) -->
-   Vaswani, A, Shazeer, N., Parmar, N., Uszkoreit, J., Jones, L., Gomez, A.N., Kaiser, Ł, & Polosukhin, I. (2017). "Attention is all you need", NIPS'17: Proceedings of the 31st International Conference on Neural Information Processing Systems (available [here](https://papers.nips.cc/paper_files/paper/2017/hash/3f5ee243547dee91fbd053c1c4a845aa-Abstract.html)) 
-   Wei, J., Bosma, M., Zhao, V. Y., Guu, K., Yu, A. W., Lester, B., ... & Le, Q. V. (2021). "Finetuned language models are zero-shot learners". arXiv:2109.01652
- Hewitt, J. (2019). Designing and Interpreting Probes. https://nlp.stanford.edu/~johnhew/interpreting-probes.html
- Max Glockner, Vered Shwartz, and Yoav Goldberg. 2018. Breaking NLI Systems with Sentences that Require Simple Lexical Inferences. In Proceedings of the 56th Annual Meeting of the Association for Computational Linguistics (Volume 2: Short Papers), pages 650–655, Melbourne, Australia. Association for Computational Linguistics. (Available [here](https://aclanthology.org/P18-2103/))
- Alex Wang, Amanpreet Singh, Julian Michael, Felix Hill, Omer Levy, and Samuel Bowman. 2018. GLUE: A Multi-Task Benchmark and Analysis Platform for Natural Language Understanding. In Proceedings of the 2018 EMNLP Workshop BlackboxNLP: Analyzing and Interpreting Neural Networks for NLP, pages 353–355, Brussels, Belgium. Association for Computational Linguistics. (Available [here](https://aclanthology.org/W18-5446/))
- Zheng, L., Chiang, W., Sheng, Y., Zhuang, S., Wu, Z., Zhuang, Y., Lin, Z., Li, Z., Li, D., Xing, E.P., Zhang, H., Gonzalez, J., & Stoica, I. (2023). Judging LLM-as-a-judge with MT-Bench and Chatbot Arena. ArXiv, abs/2306.05685.
- Chiang, W., Zheng, L., Sheng, Y., Angelopoulos, A.N., Li, T., Li, D., Zhang, H., Zhu, B., Jordan, M., Gonzalez, J.E., & Stoica, I. (2024). Chatbot Arena: An Open Platform for Evaluating LLMs by Human Preference. ArXiv, abs/2403.04132.
- Lewis, P., Perez, E., Piktus, A., Petroni, F., Karpukhin, V., Goyal, N., ... & Kiela, D. (2020). Retrieval-augmented generation for knowledge-intensive nlp tasks. Advances in Neural Information Processing Systems, 33, 9459-9474.

## Group-specific readings for Week 49

<!-- Will need to be adapted based on groups -->

* **Group 1**: Binz, M., & Schulz, E. (2023). "Turning large language models into cognitive models". [arXiv:2306.03917](https://arxiv.org/abs/2306.03917).
* **Group 2**: Ippolito, D., Duckworth, D., Callison-Burch, C., & Eck, D. (2019). "Automatic detection of generated text is easiest when humans are fooled". [arXiv:1911.00650](https://arxiv.org/abs/1911.00650).
* **Group 3**: Frank, M. C. (2023). "Bridging the data gap between children and large language models". Trends in Cognitive Sciences (available [here](https://www.sciencedirect.com/science/article/pii/S1364661323002036)); Zaadnoordijk, L., Besold, T. R., & Cusack, R. (2022). "Lessons from infant learning for unsupervised machine learning". Nature Machine Intelligence, 4(6), 510-520 (available [here](https://www.nature.com/articles/s42256-022-00488-2)).
* **Group 4**: Hollenstein, N., Barrett, M., Troendle, M., Bigiolli, F., Langer, N., & Zhang, C. (2019). "Advancing NLP with cognitive language processing signals". [arXiv:1904.02682](https://arxiv.org/abs/1904.02682).
* **Group 5**: Park, J. S., O'Brien, J. C., Cai, C. J., Morris, M. R., Liang, P., & Bernstein, M. S. (2023). "Generative agents: Interactive simulacra of human behavior". [arXiv:2304.03442](https://arxiv.org/abs/2304.03442).
* **Group 6**: Bender, E. M., & Koller, A. (2020). "Climbing towards NLU: On meaning, form, and understanding in the age of data". In _Proceedings of the 58th annual meeting of the association for computational linguistics_ (pp. 5185-5198), available [here](https://aclanthology.org/2020.acl-main.463/)
* **Group 7**: Dou, Y., Forbes, M., Koncel-Kedziorski, R., Smith, N. A., & Choi, Y. (2021). "Is GPT-3 text indistinguishable from human text? SCARECROW: A framework for scrutinizing machine text." [arXiv:2107.01294](https://arxiv.org/abs/2107.01294).
* **Group 8**: Sap, M., LeBras, R., Fried, D., & Choi, Y. (2022). "Neural theory-of-mind? On the limits of social intelligence in large lms." [arXiv:2210.13312](https://arxiv.org/abs/2210.13312) 

## Additional Resources

The following resources are *not* compulsory assigned readings. Instead, these are a mixture of textbooks and other resources which can be used as reference texts. Specifically, these will be useful for people who want to improve their understanding of linear algebra and neural networks. I strongly recommend all of the textbooks by Gilbert Strang - he's a fantastically clear writer, which is a rare skill among mathematicians. VanderPlas (2016) is a useful reference text for basic data science using Python (pandas, matplotlib, scikit-learn). It's below the level we'll be working at but it's good to have nevertheless.

-   Bittinger, M.L., Ellenbogen, D.J., & Surgent, S.A. (2012). *Calculus and its Applications, 10th Edition*. Boston, MA: Addison-Wesley.
-   Goldberg, N. (2017). *Neural Network Methods for Natural Language Processing*. New York: Morgan & Claypool Publishers.
-   Strang, G. (2009). *Introduction to Linear Algebra (4th Edition)*. Wellesley, MA: Wellesley-Cambridge Press.
    -   (2016). *Linear Algebra and its Applications, (5th Edition)*. Wellesley, MA: Wellesley-Cambridge Press.
    -   (2019). *Linear Algebra and Learning from Data*. Wellesley, MA: Wellesley-Cambridge Press.
    -   (2020). *Linear Algebra for Everyone*. Wellesley, MA: Wellesley-Cambridge Press.
-   VanderPlas, J. (2016). *Python Data Science Handbook*. [Access](https://jakevdp.github.io/PythonDataScienceHandbook/)

## Padlet on Brightspace

We will use Brightspace for class-related communication. Please ask (and answer) questions in the Discussion forum under `Here you can ask common questions`. There is no such thing as a stupid or trivial question! If a classmates asks a question you know an answer to, try and answer. The padlet is not only for instructor-student interaction, it is for all students to share knowledge and resources, and to get answers as fast as possible.

## Asking questions

1.  Google It First! Google the error Python gives you. English language errors will have more solutions online.
2.  Search existing online resources (Google, StackOverflow, etc.) and class discussion on the Padlet for answers. If the question has already been answered, you're done!
3.  If it has already been asked but you're not satisfied with the answer, refine your question to get the answer you need, and add to the thread.
    -   Document the questions you ask and the responses.
    -   Give your question context from course concepts not course assignments
        -   Good context: "I have a question on POS tagging"
        -   Bad context: "I have a question on HW 1 question 4"
    -   Be precise in your description:
        -   Good description: "I am getting the following error and I'm not sure how to resolve it - `ImportError: No module named spacy`"
        -   Bad description: "Python is giving me errors."

## Disability Resources

Your experience in this class is important to us. If you have already established accommodations with Special Educational Support (SES), please communicate your approved accommodations to us at your earliest convenience so we can discuss your needs in this course. If you have not yet established services through SES, but have a temporary health condition or permanent disability that requires accommodations (conditions include but not limited to; mental health, attention-related, learning, vision, hearing, physical or health impacts), you are welcome to contact 8716 2720 (Monday & Thursday 9-12, Tuesday 13-15) or email sps\@au.dk. SES offers resources and coordinates reasonable accommodations for students with disabilities and/or temporary health conditions. Reasonable accommodations are established through an interactive process between you, your instructor(s) and SES. It is the policy and practice of the Aarhus University to create inclusive and accessible learning environment and ensure that all students have the opportunity to educate themselves on equal terms even if they have a disability.
