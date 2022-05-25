from readData import readData,checkMissingValues,check_for_metadata
from calculateMedian import calculateMedian
from calculateMAD import calclateMedianAbsoluteDeviation
from normalizeData import normalize_data_to_reference
import pycytominer
# Set the path to the CellProfiler output
path_to_file='Data_with_metadata.csv'
# Read the data file
data_cell_profiler=readData(path_to_file,seperator=',')
# Check for missing values
missing_values_in_columns=checkMissingValues(data_cell_profiler)
# Check if metadata is present
metadata_in_file=check_for_metadata(data_cell_profiler)

# Remove those columns that are not needed to normalize
data_to_normalize=data_cell_profiler.drop('ImageNumber',axis=1)

# parameters for feature selection pycytominer feature_select
feature_select_ops = ["drop_na_columns","variance_threshold","correlation_threshold","blocklist",]

########################################################################################################
################################ Normalize the data across the plates ##################################
########################################################################################################
if metadata_in_file:
    print('Normalization steps will be performed')
    # Step 1 CellPaint protocol: calculate median and MAD for all features for all reference cells
    reference_cells='DMSO'
    # Get all the reference cells
    data_reference_cells=data_cell_profiler.loc[data_cell_profiler['Metadata_Condition']==reference_cells,:]
    aggregated_profiles=pycytominer.aggregate(population_df=data_cell_profiler,strata='Metadata_Well')
    normalized_dmso=pycytominer.normalize(profiles=data_cell_profiler,method='mad_robustize',samples="Metadata_Condition=='DMSO'")
    feature_selection=pycytominer.feature_select(profiles=normalized_dmso,features="infer",operation=feature_select_ops)

else:
    raise Exception("Metadata to select control/sample is missing")