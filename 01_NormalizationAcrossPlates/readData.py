# Python function to read data files

import pandas as pd

def readData(input_file=None,seperator=None,set_headers='infer'):
    data_file=pd.read_csv(input_file,sep=seperator,header=set_headers)
    print('Number of rows is %d and number of columns is %d ' % (data_file.shape))
    return data_file

def checkMissingValues(input_data_frame):
    missing_values=input_data_frame.isnull()
    any_missing_values=any(missing_values)
    print('Missing values check returned: %s' % any_missing_values)
    missing_value_in_column_name=input_data_frame.columns[any_missing_values]
    print('There are %d columns with missing values' % missing_value_in_column_name[0].__len__())
    print('The following columns have missing values %s' % missing_value_in_column_name)
    return missing_values