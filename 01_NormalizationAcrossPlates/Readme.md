<h1> Python scripts to normalize CellPaint data </h1>

This repository contains the python scripts to read the CellProfiler output data from a local folder, and the python scripts to normalize the data. The normalization steps are based on the LINCS cell painting protocol as described by the Broad institue <a href="https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5223290/">in this paper (Bray et al, PMID: 27560178)</a>.

<h3> Normalization pipeline </h3>
<h4> Read the CellProfiler output </h4>
<p>The CellProfiler data is loaded via the readData() function (loaded form the readData.py file). This function takes 3 arguments:<i>input_file</i>, <i>seperator</i>, and <i>set_headers</i>. To read a csv file with headers (standard CellProfiler csv output), the following command can be used:</p>

```python
path_to_file="D:\Example\CellProfiler_image.csv"
data_cell_profiler=readData(path_to_file,seperator=',')
```
Note: the set_headers argument is not necessary to explicitly specify since it will be inferred. However, if your csv file does not contain any headers, you can set set_headers=None.
<h5> Data check: missing values and metadata column present </h5>
<p>For the downstream analysis, the csv file needs a column with metadata specifying whether the sample condition (control/threated). Furthermore, we can perform a basic check to see whether any columns have missing values.</p>

<p> To check for missing values in a column:</p>

```python
missing_values_in_columns=checkMissingValues(data_cell_profiler)
```
This will return the following output:

```python
Missing values check returned: True
there are 350 columns with a missing value
```
<p> To check whether there is a metadata column </p>

```
metadata_in_file=check_for_metadata(data_cell_profiler)
```

This will return the following error when the metadata is missing:

```
raise Exception("Metadata to select control/sample is missing")
Exception: Metadata to select control/sample is missing
```

If an exception is raised, python will stop the analysis (because of the importance of the metadata for normalization). If the metadata column is present, the normalization protocol will be continued.
 
