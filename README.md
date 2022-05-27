# Data Preprocessing Pipeline Framework

This framework provides a configurable pipeline for data preprocessing. The steps present in this pipeline are as follows:
1. Reading the data from the file (supported filetypes are csv)
2. Dealing with missing data (by ignoring rows or attributes or by using a filler value provided in the config file to replace the Null values)
3. Attribute selection for input data and output data
4. Transforming the string values of the attributes into numerical data
5. Splitting the data into train and test subsets
6. Normalizing the data by using the provided method in the config file

### Installation
The Data Preprocessing Pipeline Framework is an open-source framework available on [GitHub](https://github.com/dariamarc/DataPreprocessingPipeline). <br/>
The first step is to download the project archive or to clone the GitHub repository.
<br/>
Copy all of the provided files into your own project. <br/>
Start using all of the available functionalities provided by the *Data Preprocessing Pipeline Framework*. <br/>

### Example usage for the framework
The example provided in the framework_use_example/test_framework.py shows how this framework can be used for a task of Logistic Regression. In order to run the example run the `test_framework.py` file.

### Usage
After the installation step all of the methods should be available in your project. In order to use the pipeline you have to import `DataPipeline` into your .py file.

```python
from data_preprocessing_framework.data_pipeline import DataPipeline
```
Create an instance of the `DataPipeline` into your file with the filename to your config file
```python
data_pipeline = DataPipeline("../data_pipeline_config.ini")
```
Use method `preprocess_data` to obtain the training and testing data
```python
train_inputs, train_outputs, test_inputs, test_outputs = data_pipeline.preprocess_data()
```

### Configuration
The framework can be configured through the `data_pipeline_config.ini` file or through any other ini file that has the following format
```ini
[data_info]

filename = <name of the file containing data>
filetype = <type of file containing data>
missing_data_method = <method used to deal with missing values from the data>
normalization_method = <method used for normalization>
input_attributes = <list of attributes to be used as input separated by comma>
output_attributes = <list of attributes to be used as output separated by comma>
numerical_attributes = <list of numerical attributes in the data>
clean_data_axis = <axis for the drop cleaning method>
filler_value = <filler value for the fill cleaning method>
```
Note: all of the attributes that have lists as values need to not have spaces between the commas and the values <br/>
If one of the config attributes is not to be used than its value is left empty. <br/>
<br/>
An example of configuration that uses the *drop* cleaning method and the *scale* normalization technique can be seen below:

```ini
[data_info]

filename = ../train_ctrUa4K.csv
filetype = csv
missing_data_method = drop
normalization_method = scale
input_attributes = Gender,Married,Dependents,Education,ApplicantIncome,LoanAmount,Loan_Amount_Term,Credit_History
output_attributes = Loan_Status
numerical_attributes = ApplicantIncome,LoanAmount,Loan_Amount_Term,Credit_History
clean_data_axis =
filler_value =
```

### Author
Marc Anastasia-Daria, dariamarc.am[at]gmail.com

### Contributing
All pull requests are welcome. For major changes, please open an issue first to discuss the changes.
