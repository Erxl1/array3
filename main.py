import sys
from TK_1 import create_list
from TK_2 import get_min_max
from TK_3 import tk_3_fun
from TK_4 import tk_4_fun
from TK-5 import tk_5_fun


def main():
    list_size = int(input('List size:'))
    list_data = []
    list_data = create_list(list_data)
    print(list_data)
    temp_list = []
    temp_list = get_min_max(list_data, list_size)
    print("Min: " + float(temp_list[0]) + "Max: " + float(temp_list[1]))
    temp_list = tk_3_fun(list_data, list_size)
    print("TK-3 result:")
    print(temp_list)
    temp_list = tk_4_fun(list_data, list_size)
    print("TK-4 result:")
    print(temp_list)
    temp_list = tk_5_fun(list_data, list_size)
    print("TK-5 result:")
    print(temp_list)
    return 0


if __name__ == '__main__':
    sys.exit(main())
