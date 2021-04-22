# There is a queue for the self-checkout tills at the supermarket. Your task is write a function to calculate the total
# time required for all the customers to check out!
# input
#     customers: an array of positive integers representing the queue. Each integer represents a customer, and its
#     value is the amount of time they require to check out.
#     n: a positive integer, the number of checkout tills.
# output
# The function should return an integer, the total time required.
# Important
# Please look at the examples and clarifications below, to ensure you understand the task correctly :)
# Examples
# queue_time([5,3,4], 1)
# # should return 12
# # because when n=1, the total time is just the sum of the times
# queue_time([10,2,3,3], 2)
# # should return 10
# # because here n=2 and the 2nd, 3rd, and 4th people in the
# # queue finish before the 1st person has finished.
# queue_time([2,3,10], 2)
# # should return 12
# Clarifications
#     There is only ONE queue serving many tills, and
#     The order of the queue NEVER changes, and
#     The front person in the queue (i.e. the first element in the array/list) proceeds to a till as soon as it becomes
#     free.
#
# N.B. You should assume that all the test input will be valid, as specified above.


def queue_time(customers, n):
    if customers:
        count_array = customers[:n]
        while len(customers) != 0:
            customers = customers[n:]
            i = 0
            if customers:
                count_array.sort()
                while i < n and len(customers) > i:
                    count_array[0] += customers[i]
                    i += 1
                    count_array.sort()
        return max(count_array)
    else:
        return 0

# def queue_time(customers, n):
#     l=[0]*n
#     for i in customers:
#         l[l.index(min(l))]+=i
#     return max(l)
#
print((queue_time([], 1)))
# print((queue_time([5], 1)))
# print((queue_time([2], 5)))
# print((queue_time([1, 2, 3, 4, 5], 1)))
# print((queue_time([1, 2, 3, 4, 5], 100)))
# print((queue_time([2, 2, 3, 3, 4, 4], 2)))
# print((queue_time([34, 20, 45, 40, 48, 42, 45, 21, 45, 27, 18, 33], 4)))
print((queue_time([18, 2, 16, 35, 10, 6, 21, 30, 46, 9, 46, 9, 38, 23, 19, 16, 15, 35, 1], 6)))


# test.assert_equals(queue_time([], 1), 0, "wrong answer for case with an empty queue")
# test.assert_equals(queue_time([5], 1), 5, "wrong answer for a single person in the queue")
# test.assert_equals(queue_time([2], 5), 2, "wrong answer for a single person in the queue")
# test.assert_equals(queue_time([1, 2, 3, 4, 5], 1), 15, "wrong answer for a single till")
# test.assert_equals(queue_time([1, 2, 3, 4, 5], 100), 5, "wrong answer for a case with a large number of tills")
# test.assert_equals(queue_time([2, 2, 3, 3, 4, 4], 2), 9, "wrong answer for a case with two tills")
