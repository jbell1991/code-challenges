def shuffle_array(nums, n):
    # iterate over ever other item the list
    for i in range(0, len(nums), 2):
        # insert item from second half of list
        nums.insert(i + 1, nums[i + n])
    # delete extra nums 
    del nums[-n:]
    # return shuffled array
    return nums
