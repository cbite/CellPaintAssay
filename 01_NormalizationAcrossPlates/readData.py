# Python function to read data files
import pandas as pd
import re

def readData(input_file=None,seperator=None,set_headers='infer'):
    data_file=pd.read_csv(input_file,sep=seperator,header=set_headers)
    print('Number of rows is %d and number of columns is %d ' % (data_file.shape))
    return data_file

def checkMissingValues(input_data_frame):
    missing_values=input_data_frame.columns[input_data_frame.isnull().any()].tolist()
    condition= any(missing_values)
    print('Missing values check returned: %s' % condition)
    print('there are %d columns with a missing value' % missing_values.__len__())
    return missing_values

def check_for_metadata(input_data_frame):
    columns=input_data_frame.columns
    # Capatalize all columns names
    columns_capatalized=[name.upper() for name in columns]
    metadata_present=[bool(re.search('METADATA_WELL',i)) for i in columns_capatalized]
    print('Metadata present: %s' % any(metadata_present))
    return metadata_present