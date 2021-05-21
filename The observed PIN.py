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


pin_pad = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [None, 0, None],
]

pin_pad_dict = {
    1: ['1', '2', '4'],
    2: ['1', '2', '3', '5'],
    3: ['3', '5', '6', '9'],
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
    result = []
    tracking_dict = {}
    while observed != 0:
        digits_list.append(observed % 10)
        observed = observed // 10
    digits_list.reverse()
    for i in range(len(digits_list)):
        tracking_dict[digits_list[i]] = {len(pin_pad_dict[digits_list[i]]): 0}
    for i in range(len(digits_list)):
        for j in range(len(digits_list)):
            temp = pin_pad_dict[digits_list[j]][i]
            if digits_list[j] == digits_list[len(digits_list)-1]:
                temp = pin_pad_dict[digits_list[j]][i+1]
                print(temp)
            print(temp)

    return tracking_dict


print(get_pins(519))
# print(pin_pad_returns(5))

# PIN: 8: [1, 2, 3] should equal ['0', '5', '7', '8', '9']
# PIN: 11: [1, 2, 3] should equal ['11', '12', '14', '21', '22', '24', '41', '42', '44']
# PIN: 369: [1, 2, 3] should equal ['236', '238', '239', '256', '258', '259', '266', '268', '269', '296'
# , '298', '299', '336', '338', '339', '356', '358', '359', '366', '368', '369', '396', '398',
# '399', '636', '638', '639', '656', '658', '659', '666', '668', '669', '696', '698', '699']
