def contains_duplicate(nums):
    # empty dict
    dict = {}
    # iterate over the array
    for num in nums:
        # if num is not in dict
        if num not in dict:
            # add to the dictionary and assign a value of 1
            dict[num] = 1
        # if num is already in the dict
        else:
            # add 1 to the value
            dict[num] += 1
    # iterate over the dict values
    for value in dict.values():
        # if value > 1
        if value > 1:
            # return true
            return True
        else:
            return False
