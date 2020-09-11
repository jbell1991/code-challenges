def move_zeroes(nums):
    """
    Do not return anything, modify nums in-place instead.
    """
    # pointer
    pointer = 0
    # iterate over the index in the array
    for i in range(len(nums)):
        # if num not equal to zero
        if nums[i] != 0:
            # swap the non-zero value with the value at the index of the pointer
            nums[pointer], nums[i] = nums[i], nums[pointer]
            # increment the pointer by 1
            pointer += 1
    return nums
