#!/usr/bin/python3
def element_at(list, index):
    if index < 0 or index > len(list) - 1:
        return 'None'
    else:
        return list[index]
