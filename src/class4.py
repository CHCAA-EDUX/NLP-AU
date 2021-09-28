from datasets import load_dataset

# load the sst2 dataset
dataset = load_dataset("glue", "sst2")

# select the train split
train = dataset["train"]
'''
print("Examining train set:")
print(train)
print(train.features)

print("Information about the dataset:")
print(train.info.description)
print("Homepage")
print(train.info.homepage)

print("Examining sentence")
print(type(train["sentence"]))
print(type(train["sentence"][0]))


print("Examining label")
print(type(train["label"]))
print(type(train["label"][0]))
# set takes all the unique values
print(set(train["label"]))

print("A few samples:")
for t in range(10):
    sent = train["sentence"][t]
    lab = train["label"][t]
    print(sent, "-",  lab)
'''
#Term frequency
# tf(t,d) = count of t in d / number of words in d
#print(train["sentence"][0])
def split_func(sentence):
    return (sentence.split())

# make a train subset
sub_train = train[0:10]

string_list = []

# Split the sentences into one list
for s in range(10):
    sentence = sub_train["sentence"][s]
    split_sentence = split_func(sentence)
    string_list.append(split_sentence)

def flatten(t):
    return [item for sublist in t for item in sublist]

from collections import Counter

# Count and dictionary function
# tf(t,d) = count of t in d / number of words in d
def term_freq(tokens: 'list[str]') -> dict:
    flatten_tokens = flatten(tokens) # only if it is a list of lists
    #print()
    term_freq_list = dict(Counter(flatten_tokens))
    
    tf = {}

    # Get term frequency
    for element in term_freq_list:
        tf[str(element)] = term_freq_list[str(element)]/len(tokens)
    return tf
#print(term_freq(string_list))

# Document frequency
# df(t) = occurrence of t in document

def doc_freq(tokens: 'List[List[str]]') -> dict:

    """
    Takes in a list of documents which each is a list of tokens and return a dictionary of frequencies for each token over all the documents. E.g. {"Aarhus": 20, "the": 2301, ...}
    """
    flatten_tokens = flatten(tokens) # only if it is a list of lists
    #print()
    df = dict(Counter(flatten_tokens))
    
    return df

print(doc_freq(string_list))
    


    

#def term_freq(tokens: List[str]) -> dict:
    
'''
    Takes in a list of tokens (str) and return a dictionary of term frequency of each token
'''
    # your code