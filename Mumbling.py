# This time no story, no theory. The examples below show you how to write function accum:
# accum("abcd") -> "A-Bb-Ccc-Dddd"
# accum("RqaEzty") -> "R-Qq-Aaa-Eeee-Zzzzz-Tttttt-Yyyyyyy"
# accum("cwAt") -> "C-Ww-Aaa-Tttt"


def accum(s):
    _string = ''
    for _char in range(len(s)):
        _string += s[_char].upper() + s[_char].lower()*_char
        if (_char + 1) < len(s):
            _string += '-'
    return _string

# def accum(s):
#     return '-'.join(c.upper() + c.lower() * i for i, c in enumerate(s))

# >>> spisok = [16, 46, 26, 36]
# >>> for i in enumerate(spisok):
# ...     print(i)
# ...
# (0, 16)
# (1, 46)
# (2, 26)
# (3, 36)


if __name__ == '__main__':
    print(accum("abcd"))

