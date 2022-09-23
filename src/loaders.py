import os
import pandas as pd

class CorpusLoader:
    """
    A class which loads all text files in a folder calling the DataLoader() class.

        Parameters:
            folder(string): A filepath for the folder with texts to be loaded

        Returns:
            corpus_dict(dict): A dictionary of values comprising a doc ID, and the vals dict from DataLoader()
    """
    def __init__(self, folder):
        self.folder = folder

    def _get_values(self, filepath):
        # load data with pandas
        data = pd.read_fwf(filepath, header=None)
        # keep only first column
        data = data[0]
        # using pandas methods to split all strings
        split = data.str.split()
        # return a dictionary of values
        vals = {}
        # create a counter for looping over all split data
        i = 0
        # for every entry in the split dataframe
        for row in split:
            # get the original data as a str from the dataframe
            raw = data.iloc[i]
            # create a dictionary entry with the raw data and split data
            vals[i] = {"raw": raw, "split": row}
            # increment by 1
            i += 1
        return vals

    def show_values(self):
        # intialise empty dictionary
        corpus_dict = {}
        # intialise counter at 0
        input_dir = sorted(os.listdir(self.folder))
        i = 0
        # for every file in the specific folder
        for filename in input_dir:
            # return a dictionary of values like above
            vals = self._get_values(self.folder + "/" + filename)
            # append to dict
            corpus_dict[i] = vals
            # increment counter
            i += 1
        # when finished, return complete dictionary
        return corpus_dict

if __name__=="__main__":
    pass            