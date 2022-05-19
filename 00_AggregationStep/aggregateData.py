# Python function to aggregate data based on metadata columns
# T.J.M. Kuijpers 2022/05/19

def aggregateData(data_frame=None,columns_to_aggregate_by=None,aggregate_operator=None):
    # per cell observation is aggregated to per well observation
