import numpy as np

NUMBER_OF_ITEMS_LIMIT = 9


def mean_function(matrix):
    mean_list = [np.mean(matrix, axis=0).tolist(),
                 np.mean(matrix, axis=1).tolist(),
                 np.mean(matrix).tolist()]
    return mean_list


def variance_function(matrix):
    variance_list = [np.var(matrix, axis=0).tolist(),
                     np.var(matrix, axis=1).tolist(),
                     np.var(matrix).tolist()]
    return variance_list


def std_dev_function(matrix):
    std_dev_list = [np.std(matrix, axis=0).tolist(),
                    np.std(matrix, axis=1).tolist(),
                    np.std(matrix).tolist()]
    return std_dev_list


def max_function(matrix):
    max_list = [np.max(matrix, axis=0).tolist(),
                np.max(matrix, axis=1).tolist(),
                np.max(matrix).tolist()]
    return max_list


def min_function(matrix):
    min_list = [np.min(matrix, axis=0).tolist(),
                np.min(matrix, axis=1).tolist(),
                np.min(matrix).tolist()]
    return min_list


def sum_function(matrix):
    sum_list = [np.sum(matrix, axis=0).tolist(),
                np.sum(matrix, axis=1).tolist(),
                np.sum(matrix).tolist()]
    return sum_list


def calculate(a_list):
    if len(a_list) < NUMBER_OF_ITEMS_LIMIT:
        raise ValueError("List must contain nine numbers.")

    my_dictionary = {
        'mean': None,
        'variance': None,
        'standard deviation': None,
        'max': None,
        'min': None,
        'sum': None
    }
    matrix = np.reshape(np.array(a_list), (3, 3))  # convert a_list argument to a 3 by 3 matrix
    my_dictionary['mean'] = mean_function(matrix)
    my_dictionary['variance'] = variance_function(matrix)
    my_dictionary['standard deviation'] = std_dev_function(matrix)
    my_dictionary['max'] = max_function(matrix)
    my_dictionary['min'] = min_function(matrix)
    my_dictionary['sum'] = sum_function(matrix)

    return my_dictionary
