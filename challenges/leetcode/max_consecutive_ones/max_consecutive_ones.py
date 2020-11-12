def max_consecutive_ones(nums):
    # counter
    counter = 0
    # empty list
    l = []
    # iterate over the list
    for num in nums:
        # if digit is a 1
        if num == 1:
            # add 1 to counter
            counter += 1
            #append count to list
            l.append(counter)
        # if digit is not 1
        elif num != 1:
            # append count to list
            l.append(counter)
            # reset counter
            counter = 0
    # return max of list
    return max(l)
