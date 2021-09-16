"""
Convert EWT to a corpus of txt files.

Only works on unix systems.
"""
import os

from spacy.training import Corpus
import spacy

d_path = "syllabus/classes/class2/data"
write_path = "syllabus/classes/class2/train_corpus"

for ds in ["dev", "test", "train"]:
      cmd = f"python -m spacy convert {d_path}/UD_English-EWT-master/en_ewt-ud-{ds}.conllu {d_path} --converter conllu --n-sents 10 --merge-subtokens"
      os.system(cmd)

# only write train
corpus = Corpus(f"{d_path}/en_ewt-ud-train.spacy")
nlp = spacy.blank("en")
train_data = corpus(nlp)

for i, example in enumerate(train_data):
      path = os.path.join(write_path, f"{i}.txt")
      with open(path, "w") as f:
            f.write(example.y.text)

