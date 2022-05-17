# Python function to normalize features to the reference samples (as in CellPaint protocol)
# T.J.M. Kuijpers 2022/05/17
def normalize_data_to_reference(input_data,median_values,MAD_values):
    # normalization is done feature x = (value - median)/(MAD_values *1.4826)
    data_minus_median=input_data-median_values
    scaled_MAD_values=MAD_values*1.4826
    data_normalized=data_minus_median/scaled_MAD_values
    return data_normalized