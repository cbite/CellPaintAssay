import sys
sys.path.insert(0, 'C:/Users/tkuijpe1/OneDrive - TU Eindhoven/Documents/03_BiS/04_Projects/08_GitRepo/CellPaintAssay/01_NormalizationAcrossPlates')
from readData import readData
from combineDataAndMetaData import CombineDataAndMetData

# Set the path to the cellpaint data (CellProfiler output)
path_to_data="C:/Users/tkuijpe1/Downloads/2022-05-24_Raw_perturbation_calibration_data_annotated_as_Broad.csv"
# Read the CellPaint CP data
data_cell_profiler=readData(path_to_data,seperator=',')
# Set the path to the metadata (Well - compound info)
path_to_metadata="Z:/Shared folders/Nikita/for Tim/Metadata_Well_ImageNumber_Condition.csv"
# Read the metadata
meta_data=readData(path_to_metadata,seperator=',')

# Combine the metadata with the CP data
data_with_meta_data=CombineDataAndMetData(input_data=data_cell_profiler,meta_data=meta_data)
data_with_meta_data.aggregateData(aggregate_operator='median')
data_with_meta_data.combine_data_based_on_image_number()
data_with_meta_data.write_combined_data_output()
