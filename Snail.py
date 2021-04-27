# Snail Sort
#
# Given an n x n array, return the array elements arranged from outermost elements to the middle element,
# traveling clockwise.
#
# array = [[1,2,3],
#          [4,5,6],
#          [7,8,9]]
# snail(array) #=> [1,2,3,6,9,8,7,4,5]
#
# For better understanding, please follow the numbers of the next array consecutively:
#
# array = [[1,2,3],
#          [8,9,4],
#          [7,6,5]]
# snail(array) #=> [1,2,3,4,5,6,7,8,9]
#
# This image will illustrate things more clearly:
#
# NOTE: The idea is not sort the elements from the lowest value to the highest; the idea is to traverse the 2-d array
# in a clockwise snailshell pattern.
#
# NOTE 2: The 0x0 (empty matrix) is represented as en empty array inside an array [[]].


def snail(snail_map):
    temp_array_1 = []
    while snail_map:
        temp_array_1.extend(snail_map.pop(0))
        if not snail_map:
            return temp_array_1
        for j in range(len(snail_map)):
            temp_array_1.append(snail_map[j].pop(len(snail_map[j])-1))
        snail_map[len(snail_map) - 1].reverse()
        temp_array_1.extend(snail_map.pop(len(snail_map) - 1))
        for i in reversed(range(len(snail_map))):
            temp_array_1.append(snail_map[i].pop(0))
    return temp_array_1


print(snail([[1, 2, 3, 5, 8],
             [8, 9, 4, 6, 9],
             [7, 6, 5, 7, 10],
             [2, 3, 4, 5, 11]]))

print(snail([[1, 2, 3],
             [8, 9, 4],
             [7, 6, 5]]))

# array = [[1,2,3],
#          [4,5,6],
#          [7,8,9]]
# expected = [1,2,3,6,9,8,7,4,5]
# test.assert_equals(snail(array), expected)
#
#
# array = [[1,2,3],
#          [8,9,4],
#          [7,6,5]]
# expected = [1,2,3,4,5,6,7,8,9]
# test.assert_equals(snail(array), expected)

# def snail(array):
#     ret = []
#     if array and array[0]:
#         size = len(array)
#         for n in xrange((size + 1) // 2):
#             for x in xrange(n, size - n):
#                 ret.append(array[n][x])
#             for y in xrange(1 + n, size - n):
#                 ret.append(array[y][-1 - n])
#             for x in xrange(2 + n, size - n + 1):
#                 ret.append(array[-1 - n][-x])
#             for y in xrange(2 + n, size - n):
#                 ret.append(array[-y][n])
#     return ret
#
#
# import numpy as np
#
# def snail(array):
#     m = []
#     array = np.array(array)
#     while len(array) > 0:
#         m += array[0].tolist()
#         array = np.rot90(array[1:])
#     return m