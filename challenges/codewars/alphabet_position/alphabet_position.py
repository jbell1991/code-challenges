def alphabet_position(text):
    # create a dictionary mapping letters to numbers
    mapping = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8, 'i': 9,
                'j': 10, 'k': 11, 'l': 12, 'm': 13, 'n': 14, 'o': 15, 'p': 16, 'q': 17,
                'r': 18, 's': 19, 't': 20, 'u': 21, 'v': 22, 'w': 23, 'x': 24, 'y': 25,
                'z': 26}
    # empty string
    new_string = ''
    # iterate over each character in string
    for char in text.lower():
        # if character in dictionary
        if char in mapping:
            # add its value to the empty string
            new_string += str(mapping[char])
            # add a space to the empty string
            new_string += ' '
    # return string without last space new_string[0:len(new_string)-1]
    return new_string[0:(len(new_string)-1)]
                                                                                    