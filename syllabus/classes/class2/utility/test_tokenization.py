import os
from typing import List
from spacy.training import Corpus
import spacy
from wasabi import msg


def read_corpus() -> dict:
    path = os.path.join(
        os.path.dirname(os.path.abspath(__file__)),
        "..",
        "data",
        "en_ewt-ud-train.spacy",
    )
    corpus = Corpus(path)
    nlp = spacy.blank("en")
    return {i: e for i, e in enumerate(corpus(nlp))}


class TokenizationTester:
    def __init__(self):
        self.corpus = read_corpus()

    @staticmethod
    def check_tokens(x_tokens: List[str], y_tokens: List[str], verbose: bool = True) -> List[str]:
        if all(t==tt for t, tt in zip(tokens, y_tokens)):
            msg.good("\tCongratuations: All tokens are correct!")
            return True
        elif verbose:
            for x, y in zip(x_tokens, y_tokens):
                if x == y:
                    msg.good(f"\t\t{x} == {y}")
                else:
                    msg.fail(f"\t\t{x} != {y}")
        else:
            msg.fail("\tNot all tokens were correct!")
        return False

    def check_tokenization(self, text_id: int, tokens: List[str], verbose: bool = True):
        
        y_tokens = [[t.text for t in sent] for sent in self.corpus[text_id].y.sents]
        correct = []
        for i, tok in enumerate(zip(tokens, y_tokens)):
            x, y = tok
            msg.info(f"Checking sentence: {i}")
            c = self.check_tokens(x, y, verbose=verbose)
            correct.append(c)

        return y_tokens


tok_tester = TokenizationTester()


def check_tokenization(
    text_id: int, tokens: List[str], print_token_discrepancy: bool = False
) -> List[List[str]]:
    """Check whether the tokenization is correct of 

    Args:
        text_id (int): The id of the text
        tokens (List[List[str]]): The tokens supplied as a list of sentences, which itself is a list of strings.
        print_token_discrepancy (bool, optional): Whether the function should print the differences in tokens. Defaults to False.

    Returns:
        List[List[str]]: The reference tokens
    """
    return tok_tester.check_tokenization(
        text_id=text_id, tokens=tokens, verbose=print_token_discrepancy
    )

# Testing script
if __name__ == "__main__":
    tokens = [t.split(" ") for t in tok_tester.corpus[0].text.split(".")]
    check_tokenization(text_id=0, tokens=tokens, print_token_discrepancy=False)