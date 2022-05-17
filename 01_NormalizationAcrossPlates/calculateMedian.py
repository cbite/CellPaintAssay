# Python function to calculate the median based on the statistics package
# T.J.M. Kuijpers 2022-05-17
import pandas as pd

def calculateMedian(input_dataframe):
    median=input_dataframe.median(axis=0)
    return median
