<h1> Aggregation step to transform level 2 data to level 3 data </h1>

This step is used to transform level 2 data (single cell profiles) to level 3 data (aggregated profiles with metadata). here we followed the aggregation steps as described <a href='https://github.com/broadinstitute/lincs-cell-painting/tree/master/profiles'>here.</a>

First at this point and later for the creation of the consensus profiles. Here, the median of all cells within a well is aggregated to one profiler per well. The aggregation method doesn't persist the metadata which is why this step is followed by an annotation step to add the metadata.

<h3> run the aggregation pipeline </h3>
The aggregation pipelines can be called as follows: <br />
<i> Step 1: load the libraries </i>: 

```python
from readData import readData
from combineDataAndMetaData import CombineDataAndMetData
```

<b>Note:</b> readData.py is available in the 01_NormalizationStep repo. <br />
<i> Step 2: load the datasets</i></b>:

```python
path_to_data=""
data_cell_profiler=readData(path_to_data,seperator=',')
path_to_metadata=""
meta_data=readData(path_to_metadata,seperator=',')
```
<i> step 3: create the CombineDataAndMetaData() object. </i>

```python
data_with_meta_data=CombineDataAndMetData(input_data=data_cell_profiler,meta_data=meta_data)
```

Now we can aggregate the data (based on the median) and add the metadata:

```python
data_with_meta_data.aggregateData(aggregate_operator='median')
data_with_meta_data.add_condition_to_data()
```

If needed, you can write the new dataframe to a csv file:

```python
data_with_meta_data.write_combined_data_output()
```



 
