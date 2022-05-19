# Python function to aggregate data based on metadata columns
# T.J.M. Kuijpers 2022/05/19

import pandas as pd

def aggregateData(data_frame=None,columns_to_aggregate_by=None,aggregate_operator=None):
    # per cell observation is aggregated to per well observation
    if aggregate_operator=='mean':
        aggregated_data=data_frame.groupby(columns_to_aggregate_by).mean()
    if aggregate_operator=='median':
        aggregated_data=data_frame.groupby(columns_to_aggregate_by).median()
    if aggregate_operator==None:
        raise Exception('No aggregation operator (median or mean) is selected')
    return aggregated_data

