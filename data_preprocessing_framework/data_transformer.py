import numpy as np
from data_preprocessing_framework.data_cleaner import invert_list


def normalize_data(data, method="scale"):
    """
    Normalizes the provided data by using either scale or z-scale as a method. Default method is scale.
    :param data: the data to be normalized (with a 2D shape)
    :param method: the normalization method
    :return: the normalized data
    """
    if method not in ["scale", "z-score"]:
        raise ValueError("Method " + method + "undefined for normalize_data. Available methods are \"scale\", "
                                              " and \"z-score\".")

    if len(np.shape(data)) != 2:
        raise ValueError("Provided list of attributes needs to have 2 dimensions. Array provided with shape " + np.shape(data_row))

    if method == "scale":
        new_data = []
        for data_row in data:
            new_data_row = []
            for x in data_row:
                new_data_row.append(x - min(data_row) / (max(data_row) - min(data_row)))
            new_data.append(new_data_row)

    if method == "z-score":
        new_data = []
        for data_row in data:
            mean = sum(data_row) / len(data_row)
            std = np.std(data_row)
            new_data_row = []
            for x in data_row:
                new_data_row.append(x - mean / std)
            new_data.append(new_data_row)

    return new_data


def split_data(input_data, output_data):
    """
    Splits the provided input and output data into train and test sets by following the 80-20 rule.
    :param input_data: the input data provided
    :param output_data: the output data provided
    :return: the split train inputs and outputs and the test inputs and outputs
    """
    np.random.seed(5)
    indexes = [i for i in range(len(input_data))]
    train_sample = np.random.choice(indexes, int(0.8 * len(input_data)), replace=False)
    test_sample = [i for i in indexes if i not in train_sample]

    train_inputs = [input_data[i] for i in train_sample]
    train_outputs = [output_data[i] for i in train_sample]
    test_inputs = [input_data[i] for i in test_sample]
    test_outputs = [output_data[i] for i in test_sample]

    return train_inputs, train_outputs, test_inputs, test_outputs


def shuffle_data(data):
    """
    Shuffles the provided data randomly
    :param data: the data to be shuffled
    :return: the shuffled data
    """
    data_len = len(data)
    permutation = np.random.permutation(data_len)

    shuffled_data = [data[i] for i in permutation]

    return shuffled_data


def select_attributes(data, attribute_map, attributes):
    """
    Selects from the provided data the columns that are corresponding to the attributes provided in the attributes list.
    The method needs a map between the attribute names and the column indexes
    :param data: the whole data having all of the attributes
    :param attribute_map: the map correlating the attribute names to their indexes
    :param attributes: the list of attribute names to be selected
    :return:
    """
    new_data = []
    column_idxes = []
    for attribute in attributes:
        column_idxes.append(attribute_map[attribute])

    inverted_data = invert_list(data)
    for i in range(len(inverted_data)):
        if i in column_idxes:
            new_data.append(inverted_data[i])

    return invert_list(new_data)


def to_numerical_values(data_row):
    """
    Transforms the data row containing a finite number of strings to numerical values by providing to each string a unique number
    :param data_row: the data row containing the strings
    :return: the data row having numerical values and a mapping between the string values and the numerical values
    """
    values_set = set(data_row)

    values_map = {}
    i = 0
    for value in values_set:
        values_map[value] = i
        i = i + 1

    print(values_map)
    numerical_data_row = []
    for value in data_row:
        numerical_data_row.append(values_map[value])

    return numerical_data_row, values_map
