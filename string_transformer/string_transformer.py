def string_transformer(s):
    # empty string
    new_s = ''
    # iterate over each char in string
    for char in s:
        # if upper
        if char.isupper():
            # change to lower
            new_s += char.lower()
        # if lower
        elif char.islower():
            # change to upper
            new_s += char.upper()
        # if space
        elif char.isspace():
            # add space
            new_s += ' '
    # convert string to list
    l = new_s.split(' ')
    # reverse list
    l.reverse()
    # return list joined on spaces
    return ' '.join(l)
