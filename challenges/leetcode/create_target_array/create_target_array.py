def create_target_array(nums, index):
    # empty list
    target_array = []
    # iterate over both the nums and the indexes
    for num, idx in zip(nums, index):
        # insert the num at that index to the empty list
        target_array.insert(idx, num)
    # return the list
    return target_array
