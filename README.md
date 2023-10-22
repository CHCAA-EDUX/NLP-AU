# Summary
This repo contains one possible solution to assignment 4, training a (Bi-)LSTM for named entity recognition.

This assignment using the [CONLLPP dataset](https://huggingface.co/datasets/conllpp) from Huggingface and uses Pytorch for model training.

The results are logged using [Weights and Biases](https://wandb.ai/). You can sign up for free for this service and use it to track your own models during training. This is a really useful way of following models during training and sharing the results with other people.

For example, [here are the training loss curves for some models I trained](https://wandb.ai/rdkm/classrooms/reports/loss-22-11-11-10-55-25---VmlldzoyOTUzODMw?accessToken=bgjx2zzqhhoie6ew5qjbqpok82r3hluqf9xn7kzqj7kj5kxghasdauxhilxalgfc).

<!-- 
This should include a short description of which models you have tried and conclusions from comparing these models. This should be no longer than an abstract. This section can also include questions regarding the assignment.
-->

# Performance
The table below presents one set of results from one model, trained with the default parameters set in [main.py](ner/main.py)
<!-- 
This should include a table of performance metrics of different models. The performance metrics should at least include accuracy and F1-score.
 -->
```
              precision    recall  f1-score   support

         LOC       0.78      0.86      0.82      1646
        MISC       0.62      0.53      0.57       723
         ORG       0.75      0.59      0.66      1715
         PER       0.83      0.83      0.83      1618

   micro avg       0.77      0.73      0.75      5702
   macro avg       0.74      0.70      0.72      5702
weighted avg       0.76      0.73      0.74      5702
```

## Project Organization
The organization of the project is as follows:

<!-- 
Correct this to reflect changes
-->

```
├── LICENSE                    <- the license of this code
├── README.md                  <- The top-level README for this project.
├── .github            
│   └── workflows              <- workflows to automatically run when code is pushed
│   │    └── pytest.yml        <- A workflow which runs pytests upon push
├── ner                        <- The main folder for scripts
|   └── ...
├── .gitignore                 <- A list of files not uploaded to git
├── requirements.txt            <- A requirements file of the required packages.
└── assignment_description.md  <- the assignment description
```



## Running the code
To run the whole project including installing the requirements, you can simply run the following (macOS or Linux only):

```
bash run.sh
```

If you wish to perform these steps manually, you should first update pip and install the requirements:
<!-- 
Update the code below such that it runs all the experiments in the performance section and print the performances.
-->

```
pip install --upgrade pip
pip install -r requirements.txt
```

Then, you can reproduce the experiments by running:

```
python ner/main.py experiments
```

Finally, you can run a new experiment by running the program with optional arguments:
```
python ner/main.py -e 100 -gE glove-wiki-gigaword-50
```

Run `python ner/main.py --help` for all optional arguments.
