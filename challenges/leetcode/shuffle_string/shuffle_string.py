def shuffle_string(s, indices):
    # empty dict
    hash_table = {}
    # empty string
    shuffled_string = ''
    # iterate over both indices and string
    for (num, char) in (zip(indices, s)):
        # set index as key and char as value
        hash_table[num] = char
    # iterate over each item in the sorted dictionary
    for k, v in sorted(hash_table.items()):
        # add each value (char) to the shuffled string
        shuffled_string += v
    return shuffled_string
