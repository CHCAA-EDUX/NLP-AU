from collections import Counter
import spacy

nlp = spacy.load("en_core_web_sm")
doc = nlp("This is an English text")

def term_freq(tokens):
    """
    Takes in a list of tokens (str) and return a dictionary of term frequency of each token
    tf(t,d) = count of t in d / number of words in d
    """
    token_counts = Counter([token for token in tokens])
    term_freq = ([(token, count/len(tokens)) for token, count in token_counts.items()])
    return(term_freq)


def doc_freq(docs):
    """
    Takes in a list of documents which each is a list of tokens 
    and return a dictionary of frequencies for each token over all the 
    documents. E.g. {"Aarhus": 20, "the": 2301, ...}
    """
    doc_freq = Counter()
    for d in docs:
        unique_tokens = set(d)
        cur_token_counts = Counter([token for token in unique_tokens])
        doc_freq = doc_freq + cur_token_counts
    return(doc_freq)    
