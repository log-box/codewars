# There is a secret string which is unknown to you. Given a collection of random triplets from
# the string, recover the original string.
#
# A triplet here is defined as a sequence of three letters such that each letter occurs somewh
# ere before the next in the given string. "whi" is a triplet for the string "whatisup".
#
# As a simplification, you may assume that no letter occurs more than once in the secret string.
#
# You can assume nothing about the triplets given to you other than that they are valid triple
# ts and that they contain sufficient information to deduce the original string. In particular
# , this means that the secret string will never contain letters that do not occur in one of the triplets given to you.
# Есть секретная строка, которая вам неизвестна. Учитывая набор случайных троек из строки, восстановите исходную строку.
#
# Тройка здесь определяется как последовательность из трех букв, так что каждая буква встречается где-то перед следую
# щей в данной строке. «whi» - тройка для строки «whatisup».
#
# В качестве упрощения вы можете предположить, что ни одна буква не встречается в секретной строке более одного раза.
#
# Вы не можете ничего предполагать о данных вам триплетах, кроме того, что они являются действительными триплетами и
# что они содержат достаточно информации для вывода исходной строки. В частности, это означает, что секретная строка
# никогда не будет содержать букв, которых нет ни в одной из данных вам троек.


def recoverSecret(triplets):

    result_array = set()
    for i in range(len(triplets)):
        for j in range(len(triplets[i])):
            result_array.add(triplets[i][j])
    result_array = list(result_array)
    for i in range(len(triplets)):
        for j in range(len(triplets[i])):
            temp = triplets[i].index(triplets[i][j])




    print(result_array)


# secret = "whatisup"
triplets = [
  ['t','u','p'],
  ['w','h','i'],
  ['t','s','u'],
  ['a','t','s'],
  ['h','a','p'],
  ['t','i','s'],
  ['w','h','s']
]
recoverSecret(triplets)

#'w' 'h' 'a' 't' 'i' 's' 'u' 'p'