def tk_4_fun(list_data, list_size):
    summary = 0
    for i in range(list_size):
        summary += float(list_data[i])
    average = summary / list_size
    list_data_tk_4 = []
    for i in range(list_size):
        list_data_tk_4[i] = list_data[i] * average
    return list_data_tk_4
