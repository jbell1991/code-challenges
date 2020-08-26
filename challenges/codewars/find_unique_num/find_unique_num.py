def find_uniq(arr):
    # use a dictionary to store each number as a key with its count as the value
    # empty dict
    dict = {}
    # iterate over the array
    for num in arr:
        # if the number is not in the dict
        if num not in dict:
            # assign its value to 1
            dict[num] = 1
        # if the number is in the dict
        else:
            # add 1 to its value
            dict[num] += 1
    # iterate over the dict
    for key, value in dict.items():
        # if the value == 1 (it's unique)
        if value == 1:
            # return the key
            return key
