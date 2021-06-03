# In this kata you have to create all permutations of an input string and remove duplicates, if present. This means,
# you have to shuffle all letters from the input in all possible orders.
#
# Examples:
#
# permutations('a'); # ['a']
# permutations('ab'); # ['ab', 'ba']
# permutations('aabb'); # ['aabb', 'abab', 'abba', 'baab', 'baba', 'bbaa']

from itertools import permutations as permut


def permutations(string):
    _arr = []
    _set = {}
    for item in permut(string, len(string)):
        _arr.append(''.join(item))

    _set = set(_arr)
    _arr = list(_set)
    return _arr


# import itertools
#
# def permutations(string):
#     return list("".join(p) for p in set(itertools.permutations(string)))
