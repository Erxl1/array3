def get_min_max(list_data, list_size):
    minim = list_data[0]
    maxim = list_data[0]
    for i in range(list_size):
        if minim > list_data[i]:
            minim = list_data[i]
        if maxim < list_data[i]:
            maxim = list_data[i]

    min_max = (min, max)
    return min_max
