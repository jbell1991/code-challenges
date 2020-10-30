def single_number(nums):
    # empty dict
    dictionary = {}
    # iterate over each number in the array
    for num in nums:
        # if num not in dict
        if num not in dictionary:
            # add it to dict and assign count to 1
            dictionary[num] = 1
        # if num in dict
        else:
            # add 1 to value
            dictionary[num] += 1
    # iterate over dictionary items
    for k, v in dictionary.items():
        # if value is equal to 1
        if v == 1:
            # return key
            return k
