# Python function to read data files

import pandas as pd

def readData(input_file=None,seperator=None,set_headers='infer'):
    data_file=pd.read_csv(input_file,sep=seperator,headers=set_headers)
    print('Number of rows is %d and number of columns is %d ' % (data_file.shape))
    return data_file
