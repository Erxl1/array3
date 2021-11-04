import sys


def main():
    list_size = int(input('List size:'))
    list_data = set_list(list_size)
    print(list_data)


def set_list(list_size):
    list_data = []
    for i in range(list_size):
        list_data += [float(input('Enter' + str(i + 1) + 'value:'))]
    return list_data


if __name__ == '__main__':
    sys.exit(main())
