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
    snail_map = [[1, 2, 3, 5, 8],
                 [8, 9, 4, 6, 9],
                 [7, 6, 5, 7, 10],
                 [1, 2, 3, 4, 11]]
    temp_array_1 = []
    while snail_map:
        if not temp_array_1:
            temp_array_1 = snail_map.pop(0)
        # for i in range(len(snail_map)):
        for j in range(len(snail_map)):
            # for j in range(len(snail_map[i])-1):
                # temp1 = snail_map[j]
                # temp = snail_map[j].pop(len(temp1)-1)
            temp_array_1.append(snail_map[j].pop(len(snail_map[j])-1))
        test = range(len(snail_map))
        for i in range(len(snail_map[len(snail_map)-1])):
            # reverse_array = snail_map[len(snail_map)-1].reverse()
            snail_map[len(snail_map) - 1].reverse()
            temp_array_1.append(snail_map[i].pop(len(snail_map)-1))

        print(temp_array_1)
    print('done')
    # for string in range(len(snail_map)):
    #     for row in range(len(snail_map[string])):
    #         print(snail_map[row][string], end=' ')


snail([[1, 2, 3],
       [8, 9, 4],
       [7, 6, 5]])

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
