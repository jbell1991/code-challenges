def running_sum(nums):
    # keep a running total
    total = 0
    # iterate over the array
    for i, num in enumerate(nums):
        # add each number to the total
        total += num
        # replace position in the array with the total
        nums[i] = total
    # return the running sum
    return nums
