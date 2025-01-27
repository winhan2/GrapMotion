# coding: utf-8

from copy import deepcopy

def od_to_td(od_list: list):
    add_num = 2
    if len(od_list) == 8:
        add_num = 4
    return deepcopy([[od_list[i], od_list[i+1]] for i in range(0, int(len(od_list) / 2) + add_num, 2)])