# Write a function that takes in a string of one or more words, and returns the same string,
# but with all five or more letter words reversed (like the name of this kata).
#
#     Strings passed in will consist of only letters and spaces.
#     Spaces will be included only when more than one word is present.
#
# Examples:
#
# spinWords("Hey fellow warriors") => "Hey wollef sroirraw"
# spinWords("This is a test") => "This is a test"
# spinWords("This is another test") => "This is rehtona test"


def spin_words(sentence):
    new_string = ''
    def reverse_string(s):
        return s[::-1]
    for word in sentence.split():
        if len(word) >= 5:
            word = reverse_string(word)
        new_string += word + ' '
    return new_string.rstrip()

# def spin_words(sentence):
#     # Your code goes here
#     return " ".join([x[::-1] if len(x) >= 5 else x for x in sentence.split()])


if __name__ == '__main__':


    print(spin_words('abcccc defj '))