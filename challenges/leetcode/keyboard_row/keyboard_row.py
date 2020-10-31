def find_words(words):
    l = []
    # create 3 rows of keyboard
    row_1 = 'qwertyuiop'
    row_2 = 'asdfghjkl'
    row_3 = 'zxcvbnm'

    # iterate over each word in the list words
    for word in words:
        # count for each row
        row_1_count = 0
        row_2_count = 0
        row_3_count = 0

        # iterate over each character in each word
        for char in word.lower():
            # if char in row_1 add 1 to count
            if char in row_1:
                row_1_count += 1
            # elif char in row_2 add 1 to count
            elif char in row_2:
                row_2_count += 1
            # elif char in row_3 add 1 to count
            elif char in row_3:
                row_3_count += 1

        # if row_1_count > 0 and row_2_count > 0 or
        # row_2_count > 0 and row_3_count > 0
        # row_1_count > 0 and row_count 3 > 0
        if (row_1_count > 0 and row_2_count > 0 or
            row_2_count > 0 and row_3_count > 0 or
            row_1_count > 0 and row_3_count > 0):
            # add to list
            l.append(word)

    # remove words from list
    for word in l:
        words.remove(word)

    return words
