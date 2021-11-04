def get_min_max(list_data, list_size):
    minim = float(list_data[0])
    maxim = float(list_data[0])
    for i in range(list_size):
        if minim > list_data[i]:
            minim = list_data[i]
        if maxim < list_data[i]:
            maxim = list_data[i]

    min_max = (minim, maxim)
    return min_max
