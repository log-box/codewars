# Simple, given a string of words, return the length of the shortest word(s).
#
# String will never be empty and you do not need to account for different data types.
# (find_short("bitcoin take over the world maybe who knows perhaps"), 3)
# (find_short("turns out random test cases are easier than writing out basic ones"), 3)
# (find_short("lets talk about javascript the best language"), 3)
# (find_short("i want to travel the world writing code one day"), 1)
# (find_short("Lets all go on holiday somewhere very cold"), 2)


def find_short(s):
    string = s.split(' ')
    max_length = 100
    l = 10000
    for i in string:
        if len(i) < l:
            l = len(i)
    # your code here
    return l # l: shortest word length
#
# def find_short(s):
#     return min(len(x) for x in s.split())

print(find_short("bitcoin take over the world maybe who knows perhaps"))