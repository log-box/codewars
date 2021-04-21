# Implement the function unique_in_order which takes as argument a sequence and returns a list of items without any
# elements with the same value next to each other and preserving the original order of elements.
#
# For example:
#
# unique_in_order('AAAABBBCCDAABBB') == ['A', 'B', 'C', 'D', 'A', 'B']
# unique_in_order('ABBCcAD')         == ['A', 'B', 'C', 'c', 'A', 'D']
# unique_in_order([1,2,2,3,3])       == [1,2,3]


def unique_in_order(iterable):
    _list = []
    for i in range(len(iterable)):
        if iterable[i] != iterable[i-1] and i != 0:
            _list.append(iterable[i])
        if i == 0:
            _list.append(iterable[0])
    return _list

    # return [iterable[i] for i in range(len(iterable)) if iterable[i] != iterable[i-1] and i > 0]



print(unique_in_order('AAAABBBCCDAABBB'))
print(unique_in_order('ABBCcAD'))
print(unique_in_order([1,2,2,3,3]))
print(unique_in_order('A'))
print(unique_in_order('AAAABBBB'))

# def unique_in_order(iterable):
#     result = []
#     prev = None
#     for char in iterable[0:]:
#         if char != prev:
#             result.append(char)
#             prev = char
#     return result