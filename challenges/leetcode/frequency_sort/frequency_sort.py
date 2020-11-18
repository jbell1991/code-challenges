def frequency_sort(s):
    # put characters and count into dictionary
    # empty dict
    dictionary = {}
    # iterate over each char in string
    for char in s:
        # if char not in dict
        if char not in dictionary:
            # add to dict with value of 1
            dictionary[char] = 1
        # else
        else:
            # add 1 to value
            dictionary[char] += 1

    # new emtpy string
    new_string = ''
    # for each k, v in dictionary sorted by value from high to low
    for k, v in sorted(dictionary.items(), key=lambda item: item[1], reverse=True):
        # new string += k*v
        new_string += (k*v)
    # return new string
    return new_string
