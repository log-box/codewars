# Alright, detective, one of our colleagues successfully observed our target person, Robby the robber. We followed
# him to a secret warehouse, where we assume to find all the stolen stuff. The door to this warehouse is secured by
# an electronic combination lock. Unfortunately our spy isn't sure about the PIN he saw, when Robby entered it.
#
# The keypad has the following layout:
#
# ┌───┬───┬───┐
# │ 1 │ 2 │ 3 │
# ├───┼───┼───┤
# │ 4 │ 5 │ 6 │
# ├───┼───┼───┤
# │ 7 │ 8 │ 9 │
# └───┼───┼───┘
#     │ 0 │
#     └───┘
#
# He noted the PIN 1357, but he also said, it is possible that each of the digits he saw could actually be another
# adjacent digit (horizontally or vertically, but not diagonally). E.g. instead of the 1 it could also be the 2 or 4.
# And instead of the 5 it could also be the 2, 4, 6 or 8.
#
# He also mentioned, he knows this kind of locks. You can enter an unlimited amount of wrong PINs, they never finally
# lock the system or sound the alarm. That's why we can try out all possible (*) variations.
#
# * possible in sense of: the observed PIN itself and all variations considering the adjacent digits
#
# Can you help us to find all those variations? It would be nice to have a function, that returns an array (or a list
# in Java and C#) of all variations for an observed PIN with a length of 1 to 8 digits. We could name the function
# getPINs (get_pins in python, GetPINs in C#). But please note that all PINs, the observed one and also the results,
# must be strings, because of potentially leading '0's. We already prepared some test cases for you.
#
# Detective, we are counting on you!


# from itertools import product


# pin_pad = [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9],
#     [None, 0, None],
# ]

pin_pad_dict = {
    1: ['1', '2', '4'],
    2: ['1', '2', '3', '5'],
    3: ['2', '3', '6'],
    4: ['1', '4', '5', '7'],
    5: ['2', '4', '5', '6', '8'],
    6: ['3', '5', '6', '9'],
    7: ['4', '7', '8'],
    8: ['0', '5', '7', '8', '9'],
    9: ['6', '8', '9'],
    0: ['0', '8']
}


def get_pins(observed):
    digits_list = []
    elements = [[]]
    pools = []
    result = []
    # этот кусок нужен, если на вход дается число, а не строка
    # while observed != 0:
    #     digits_list.append(observed % 10)
    #     observed = observed // 10
    # digits_list.reverse()
    ############################################################
    # этот кусок нужен если на вход дается строка
    for item in observed:
        digits_list.append(item)
    ############################################################
    for item in digits_list:
        pools.append(pin_pad_dict[int(item)])
    for pool in pools:
        elements = [x+[y] for x in elements for y in pool]
    for item in elements:
        data = ''.join(item)
        result.append(data)
    return result

# def product(*args, repeat=1):
#     # product('ABCD', 'xy') --> Ax Ay Bx By Cx Cy Dx Dy
#     # product(range(2), repeat=3) --> 000 001 010 011 100 101 110 111
#     pools = [tuple(pool) for pool in args] * repeat
#     result = [[]]
#     for pool in pools:
#         result = [x+[y] for x in result for y in pool]
#     temp = []
#     # for pool in pools:
#     #     for y in pool:
#     #         for x in result:
#     #             result.append((x + [y]))
#     for prod in result:
#         yield tuple(prod)

print(get_pins('369'))
# for item in product(['1', '2', '4'], ['3', '5', '6']):
#     print(''.join(item))
# print(pin_pad_returns(5))

# PIN: 8: [1, 2, 3] should equal ['0', '5', '7', '8', '9']
# PIN: 11: [1, 2, 3] should equal ['11', '12', '14', '21', '22', '24', '41', '42', '44']
# PIN: 369: [1, 2, 3] should equal ['236', '238', '239', '256', '258', '259', '266', '268', '269', '296'
# , '298', '299', '336', '338', '339', '356', '358', '359', '366', '368', '369', '396', '398',
# '399', '636', '638', '639', '656', '658', '659', '666', '668', '669', '696', '698', '699']
#
# from itertools import product
#
# ADJACENTS = ('08', '124', '2135', '326', '4157', '52468', '6359', '748', '85790', '968')
#
# def get_pins(observed):
#     return [''.join(p) for p in product(*(ADJACENTS[int(d)] for d in observed))]
