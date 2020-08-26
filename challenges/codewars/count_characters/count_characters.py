def count_char(string):
    # emtpy dict
    dict = {}
    # iterate over string
    for char in string:
        # if char not in dict
        if char not in dict:
            # set value equal to 1
            dict[char] = 1
        # else
        else:
            # add 1 to value
            dict[char] += 1
    return dict
    