# Python function file to calculate the MAD
# T.J.M. Kuijpers 2022/05/17
from scipy import stats

def calclateMedianAbsoluteDeviation(input_dataframe):
    MADvalues=stats.median_abs_deviation(input_dataframe,axis=0)
    return MADvalues


