# Python function to read data files

import pandas as pd

def readData(input_file=None,seperator=None,set_headers='infer'):
    data_file=pd.read_csv(input_file,sep=seperator,header=set_headers)
    print('Number of rows is %d and number of columns is %d ' % (data_file.shape))
    return data_file

def checkMissingValues(input_data_frame):
    missing_values=input_data_frame.columns[input_data_frame.isnull().any()].tolist()
    condition= not missing_values
    print('Missing values check returned: %s' % condition)
    print('there are %d columns with a missing value' % missing_values.__len__())
    return missing_values