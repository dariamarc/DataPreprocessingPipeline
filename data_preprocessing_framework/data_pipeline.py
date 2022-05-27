import configparser
import csv
import numpy as np
from data_preprocessing_framework.data_cleaner import clean_missing_data, invert_list
from data_preprocessing_framework.data_transformer import select_attributes, normalize_data, split_data, \
    to_numerical_values


class DataPipeline:
    def __init__(self, config_file):
        self.data_file = ""
        self.missing_data_method = ""
        self.clean_data_axis = ""
        self.filler_value = ""
        self.normalization_method = ""
        self.input_attributes = ""
        self.output_attributes = ""
        self.numerical_attributes = ""
        self.numerical_attributes_idx = []
        self.read_config_file(config_file)

    def read_config_file(self, config_file):
        config = configparser.ConfigParser()
        config.read(config_file)

        print("Found sections " + str(config.sections()) + " in file " + config_file)

        data_info = config["data_info"]
        self.data_file = data_info["filename"]
        self.missing_data_method = data_info["missing_data_method"]
        self.clean_data_axis = data_info["clean_data_axis"]
        self.filler_value = data_info["filler_value"]
        self.normalization_method = data_info["normalization_method"]
        self.input_attributes = data_info["input_attributes"].strip().split(",")
        self.output_attributes = data_info["output_attributes"].strip().split(",")
        self.numerical_attributes = data_info["numerical_attributes"].strip().split(",")

    def preprocess_data(self):
        """
        Pipeline for preprocessing data. This pipeline follows the following steps: reading the data from the file (supported filetypes are csv)
, dealing with missing data (by ignoring rows or attributes or by using a filler value provided in the config file to replace the Null values)
, attribute selection for input data and output data
, transforming the string values of the attributes into numerical data
, splitting the data into train and test subsets
, normalizing the data by using the provided method in the config file.

        :return:
        The train inputs and outputs and the test inputs and outputs as numpy arrays
        """
        header, data_rows = self.read_csv_data_file(self.data_file)

        data_rows = clean_missing_data(data_rows, method=self.missing_data_method)

        header_map = self.create_header_idx_map(header)
        self.numerical_attributes_idx = [header_map[i] for i in self.numerical_attributes]

        input_data = select_attributes(data_rows, header_map, self.input_attributes)
        output_data = select_attributes(data_rows, header_map, self.output_attributes)

        input_data = self.transform_to_numerical(input_data)
        output_data = self.transform_to_numerical(output_data)

        train_inputs, train_outputs, test_inputs, test_outputs = split_data(input_data, output_data)
        train_inputs = normalize_data(train_inputs, method=self.normalization_method)

        return np.asarray(train_inputs), np.asarray(train_outputs), np.asarray(test_inputs), np.asarray(test_outputs)

    def read_csv_data_file(self, data_file):
        file = open(data_file)
        csvreader = csv.reader(file)
        header = []
        header = next(csvreader)

        rows = []
        for row in csvreader:
            rows.append(row)

        return header, rows

    def create_header_idx_map(self, header):
        header_map = {}
        for i in range(len(header)):
            header_map[header[i]] = i

        return header_map

    def transform_to_numerical(self, data):
        inverted_data = invert_list(data)
        new_data = []

        for i in range(len(inverted_data)):
            if i in self.numerical_attributes_idx:
                new_values = []
                for value in inverted_data[i]:
                    new_values.append(float(value))
                new_data.append(new_values)
            else:
                new_data.append(to_numerical_values(inverted_data[i])[0])

        return invert_list(new_data)