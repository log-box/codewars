# Move the first letter of each word to the end of it, then add "ay" to the end of the word. Leave punctuation marks untouched.
# Examples
#
# pig_it('Pig latin is cool') # igPay atinlay siay oolcay
# pig_it('Hello world !')     # elloHay orldway !


def pig_it(text):
    result = []
    original_text = text.split(' ')
    for item in original_text:
        if item != '!' and item != '?' and item != '.' and item != ',':
            item = item[1:] + item[0:1] + 'ay'
        result.append(item)
    return ' '.join(result)

# def pig_it(text):
#     lst = text.split()
#     return ' '.join( [word[1:] + word[:1] + 'ay' if word.isalpha() else word for word in lst])


print(pig_it('Hello world !'))
print(pig_it('Pig latin is cool'))
print(pig_it('This is my string'))

#
# test.assert_equals(pig_it('Pig latin is cool'),'igPay atinlay siay oolcay')
# test.assert_equals(pig_it('This is my string'),'hisTay siay ymay tringsay')