def letter_count(s):
    # empty hashtable
    dict = {}
    # iterate over each character in the string
    for char in s:
        # if char not in hashtable
        if char not in dict:
            # assign value to 1
            dict[char] = 1
        # else
        else:
            # add 1 to the value
            dict[char] += 1
    # return hashtable
    return dict
