def unique_occurrences(arr):
    # use a dictionary to store nums as keys with count of occurrences as values
    # if there is a duplicate count in the values return false else return true
    # empty dict
    dict = {}
    # empty set
    storage = set()
    # iterate over the arr
    for num in arr:
        # if num not in dict
        if num not in dict:
            # add it to the dict with value of 1
            dict[num] = 1
        # else
        else:
            # increment value by 1
            dict[num] += 1
    # iterate over the values in the dict
    for value in dict.values():
        # if value not in set
        if value not in storage:
            # add it to the set
            storage.add(value)
        # else
        else:
            # return False
            return False
    # return True
    return True
