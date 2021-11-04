def create_list(list_size):
    list_data = set_list(list_size)
    return list_data


def set_list(list_size):
    list_data = []
    for i in range(list_size):
        list_data += [float(input('Enter' + str(i + 1) + 'value:'))]
    return list_data
