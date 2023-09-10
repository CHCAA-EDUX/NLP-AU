from collections import Counter
import argparse


parser = argparse.ArgumentParser()
parser.add_argument("--start", type=int, default=0, 
                    help="start index for slicing")
parser.add_argument("--end", type=int, default=0, 
                    help="end index for slicing")


def string_slicer(start_idx=0, end_idx=10):
    '''
    Returns a slice of of war and peace, indexed by character position

            Parameters:
                    start_idx (int): Start index
                    end_idx (int): End index

            Returns:
                    binary_sum (str): Binary string of the sum of a and b
    '''
    text = open('../data/book-war-and-peace.txt').read()
    return text[start_idx:end_idx]


if __name__=='__main__':
    args = parser.parse_args()
    result = string_slicer(args.start, args.end)
    print(result)