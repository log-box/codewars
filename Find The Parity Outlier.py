# You are given an array (which will have a length of at least 3, but could be very large) containing integers.
# The array is either entirely comprised of odd integers or entirely comprised of even integers except for a
# single integer N. Write a method that takes the array as an argument and returns this "outlier" N.
# 315 / 5000
# Результаты перевода
# Вам предоставляется массив (который будет иметь длину не менее 3, но может быть очень большим),
# содержащий целые числа. Массив либо полностью состоит из нечетных целых чисел, либо полностью состоит из
# четных целых чисел, за исключением одного целого числа N. Напишите метод, который принимает массив в качестве
# аргумента и возвращает этот «выброс» N.


def find_outlier(integers):
    sign_odd = 0
    sign_even = 0
    for i in range(3):
        if integers[i] % 2 == 0:
            sign_odd += 1
        if integers[i] % 2 == 1:
            sign_even += 1
    if sign_odd > sign_even:
        for i in range(len(integers)):
            if integers[i] % 2 == 1:
                return integers[i]
    else:
        for i in range(len(integers)):
            if integers[i] % 2 == 0:
                return integers[i]

if __name__ == '__main__':
    find_outlier([2, 4, 6, 8, 10, 3])


# def find_outlier(int):
#     odds = [x for x in int if x%2!=0]
#     evens= [x for x in int if x%2==0]
#     return odds[0] if len(odds)<len(evens) else evens[0]