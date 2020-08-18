def expanded_form(num):
    # convert int to str
    string = str(num)
    # get length of the string
    length = len(string)
    # empty list to store expanded numbers
    expanded_nums = []
    # iterate over each character in the string
    for i, char in enumerate(string):
        # if the char is not equal to zero
        if char != '0':
            # add zeros to following places (len of string - index position - 1)
            # and append each expaned num to the list
            expanded_nums.append((char + '0' * (length - i - 1)))
    # return string by joining elements with a +
    return ' + '.join(expanded_nums)
