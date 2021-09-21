import sys, os
from pathlib import Path


#LOAD DATA
infile = os.path.join("NLP","NLP-E21","syllabus","classes","class2","train_corpus")

for filepath in Path(infile).glob("*.txt"):
    with open(filepath, "r", encoding = "utf-8") as file:
        loaded_text = file.read()
        
        loaded_text)