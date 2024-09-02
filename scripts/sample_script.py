import argparse


parser = argparse.ArgumentParser()
parser.add_argument("--start", type=int, default=0, 
                    help="start index for slicing")
parser.add_argument("--end", type=int, default=0, 
                    help="end index for slicing")
parser.add_argument("--filename", type=str, 
                    help="filename for the input text")


def string_slicer(filename, start_idx=0, end_idx=10):
    '''
    Returns a slice of of war and peace, indexed by character position

            Parameters:
                    filename (str): Filename where input text is found
                    start_idx (int): Start index
                    end_idx (int): End index

            Returns:
                    sliced_text (str): Text using input indices
    '''
    text = open(f'../data/{filename}').read()
    sliced_text = text[start_idx:end_idx]
    return sliced_text


if __name__=='__main__':
    args = parser.parse_args()
    result = string_slicer(args.start, args.end)
    print(result)
