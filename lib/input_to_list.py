# coding: utf-8

def input_to_list(input_data: str, split_chars: list) -> list:
    return_list = []
    for i in input_data.split(', '):
        if split_chars[0] in i:
            i = i.replace(split_chars[0], '')
        elif split_chars[1] in i:
            i = i.replace(split_chars[1], '')
        elif split_chars[2] in i:
            i = i.replace(split_chars[2], '')
        elif split_chars[3] in i:
            i = i.replace(split_chars[3], '')
        return_list.append(int(i))
    return return_list