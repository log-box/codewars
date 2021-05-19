# Create a function that takes a positive integer and returns the next bigger number that can be formed by
# rearranging its digits. For example:
#
# 12 ==> 21
# 513 ==> 531
# 2017 ==> 2071
#
# nextBigger(num: 12)   // returns 21
# nextBigger(num: 513)  // returns 531
# nextBigger(num: 2017) // returns 2071
#
# If the digits can't be rearranged to form a bigger number, return -1 (or nil in Swift):
#
# 9 ==> -1
# 111 ==> -1
# 531 ==> -1
#
# nextBigger(num: 9)   // returns nil
# nextBigger(num: 111) // returns nil
# nextBigger(num: 531) // returns nil



def next_bigger(n):
    s = list(str(n))
    for i in range(len(s)-2,-1,-1):
        if s[i] < s[i+1]:
            t = s[i:]
            m = min(filter(lambda x: x>t[0], t))
            t.remove(m)
            t.sort()
            s[i:] = [m] + t
            return int("".join(s))
    return -1

# def int_to_list(num):
#     result = []
#     while num > 0:
#         result.append(num % 10)
#         num //= 10
#     result.reverse()
#     return result
#
#
# def list_to_int(lst):
#     num = 0
#     for i, v in enumerate(reversed(lst)):
#         num += v * 10 ** i
#     return num  # 1234
#
#
# def next_bigger(n):
#     temp = int_to_list(n)
#     target = None
#     _next = None
#     target_index = None
#     next_index = None
#     while n != 0:
#         _current = n % 10
#         n = n // 10
#         _next = n % 10
#         if _current > _next and n != 0 or _next == 0:
#             target = _current
#             break
#
#     for i in reversed(range(len(temp))):
#         if temp[i] == target and target_index is None and temp[i - 1] == _next and target !=0 and _next !=0:
#             target_index = i
#         if temp[i] == _next and next_index is None:
#             next_index = i
#     if target_index is not None and next_index is not None:
#         temp[target_index], temp[next_index] = temp[next_index], temp[target_index]
#
#     if target_index == None or next_index == None:
#         return -1
#     else:
#         return list_to_int(temp)


# print(next_bigger(201717))  # 207171
# print(next_bigger(35694))  # 35964
# print(next_bigger(123))  # 132
# print(next_bigger(531))  # -1
print(next_bigger(1234567980))  # 1234567908
print(next_bigger(76655543211100))  # 1234567908
print(next_bigger(144))  # 414

# test.assert_equals(next_bigger(12), 21)
# test.assert_equals(next_bigger(513), 531)
# test.assert_equals(next_bigger(2017), 2071)
# test.assert_equals(next_bigger(414), 441)
# test.assert_equals(next_bigger(144), 414)
