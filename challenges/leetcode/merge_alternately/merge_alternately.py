def merge_alternately(word1, word2):
    # empty string
    s = ''
    # iterate over both strings
    for char1, char2 in zip(word1, word2):
        # add char to s
        s += char1
        s += char2
    # if len word 1 is less than len of word 2
    if len(word1) < len(word2):
        # add extra letters on the end
        return s + word2[len(word1) - len(word2):]
    # if len word 1 is greater than len of word 2
    elif len(word1) > len(word2):
        # add extra letters on the end
        return s + word1[len(word2) - len(word1):]
    else:
        return s
