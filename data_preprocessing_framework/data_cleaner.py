import numpy


def clean_missing_data(data, method="drop", axis=(0,), filler_value=None):
    '''
    Clean missing data from a 2D array, either by removing Null values (removing the attributes that contain Null values
    or removing the rows that contain Null values) or by filling the missing values with a given filler value.
    The removal of Null values can be done by providing the axis, which can be either 0 or 1 (or both), 0 for removing
    rows that contain Null values and 1 for removing attributes that contain Null values.
    :param data: data to be cleaned up
    :param method: either "drop" or "fill" - default is "drop"
    :param axis: axis for the "drop" method - default is (0,)
    :param filler_value: filler value for "fill" method, default is None
    :return:
    The cleaned data after applying the selected method
    '''
    if method != "drop" and method != "fill":
        raise ValueError("Method " + method + " undefined for clean_missing_data")

    if data is None:
        raise ValueError("Undefined data passed to method clean_missing_data")

    if len(numpy.shape(data)) != 2:
        raise ValueError("Data must have 2 dimensions, but the method was provided data with shape " + str(numpy.shape(data)))

    if type(axis) != tuple:
        raise ValueError("Axis must be a tuple")
    if 0 not in axis and 1 not in axis:
        raise ValueError("Axis must have 0, 1 or both, provided value is " + str(axis))

    if method == "drop":
        if 1 in axis:
            # clean all columns that have null values
            inverted_data = invert_list(data)
            new_data = []
            for row in inverted_data:
                remove = False
                for value in row:
                    if value is None or value == '':
                        remove = True
                        break
                if not remove:
                    new_data.append(row)
            data = invert_list(new_data)

        if 0 in axis:
            # clean all rows that have null values
            new_data = []
            for row in data:
                remove = False
                for value in row:
                    if value is None or value == '':
                        remove = True
                        break
                if not remove:
                    new_data.append(row)
            data = new_data.copy()

    if method == "fill":
        new_data = []
        for row in data:
            new_row = []
            for value in row:
                if value is None or value == '':
                    new_row.append(filler_value)
                else:
                    new_row.append(value)
            new_data.append(new_row)
        data = new_data

    return data


def invert_list(data):
    """
    Inverts a 2D list
    :param data: list to be inverted
    :return: inverted list
    """
    new_list = [[data[j][i] for j in range(len(data))] for i in range(len(data[0]))]
    return new_list
