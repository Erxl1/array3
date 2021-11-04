import math


def tk_5_fun(list_data, list_size):
    list_data_tk_5 = []
    for i in range(list_size):
        list_data_tk_5[i] = math.sqrt(list_data[i])
    return list_data_tk_5
