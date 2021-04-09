def reverse_string(s):
    """
    Do not return anything, modify s in-place instead.
    """
    # last index in list
    last_index = len(s)-1
    # mid point in list
    mid = len(s) // 2
    # iterate over the index of the list until the mid point
    for i in range(len(s)-mid):
        # swap the outer most values
        last = s[last_index]
        s[last_index] = s[i]
        s[i] = last
        # increment the index by one
        last_index -= 1
    return s