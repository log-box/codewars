# Complete the function/method (depending on the language) to return true/True when its argument is an array that
# has the same nesting structures and same corresponding length of nested arrays as the first array.

#
def count_items(item_list):
    check_list = []
    if not isinstance(item_list, list):
        return False
    for item in item_list:
        if isinstance(item, list):
            check_list.append(count_items(item))
        else:
            check_list.append('item')
    return check_list


def same_structure_as(original, other):
    if count_items(original) == count_items(other):
        return True
    else:
        return False
# def same_structure_as(original,other):
#     if isinstance(original, list) and isinstance(other, list) and len(original) == len(other):
#         for o1, o2 in zip(original, other):
#             if not same_structure_as(o1, o2): return False
#         else: return True
#     else: return not isinstance(original, list) and not isinstance(other, list)
#
# def same_structure_as(original, other):
#     if type(original) == list == type(other):
#         return len(original) == len(other) and all(map(same_structure_as, original, other))
#     else:
#         return type(original) != list != type(other)

print(same_structure_as([1, 1, 1], [2, 2, 2]))
print(same_structure_as([1, [1, 1]], [2, [2, 2]]))
print(same_structure_as([1, [1, 1]], [[2, 2], 2]))
print(same_structure_as([1, [1, 1]], [[2], 2]))
print(same_structure_as([[[], []]], [[[], []]]))
print(same_structure_as([[[], []]], [[1, 1]]))
# # should return True
# same_structure_as([ 1, 1, 1 ], [ 2, 2, 2 ] )
# same_structure_as([ 1, [ 1, 1 ] ], [ 2, [ 2, 2 ] ] )
#
# # should return False
# same_structure_as([ 1, [ 1, 1 ] ], [ [ 2, 2 ], 2 ] )
# same_structure_as([ 1, [ 1, 1 ] ], [ [ 2 ], 2 ] )
#
# # should return True
# same_structure_as([ [ [ ], [ ] ] ], [ [ [ ], [ ] ] ] )
#
# # should return False
# same_structure_as([ [ [ ], [ ] ] ], [ [ 1, 1 ] ] )
# def same_structure_as(original,other):
#     if isinstance(original, list) and isinstance(other, list) and len(original) == len(other):
#         for o1, o2 in zip(original, other):
#             if not same_structure_as(o1, o2): return False
#         else: return True
#     else: return not isinstance(original, list) and not isinstance(other, list)