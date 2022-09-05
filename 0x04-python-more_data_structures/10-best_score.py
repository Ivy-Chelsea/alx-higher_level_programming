#!/usr/bin/python3
def best_score(a_dictionary):
    if not a_dictionary:
        return None
    ret = list(a_dictionary.keys())[0]
    big = a_dictionary[ret]
    for a, b in a_dictionary.items():
        if b > big:
            big = b
            ret = a
    return (ret)
