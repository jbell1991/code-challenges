def num_good_pairs(nums):
    # count how many times a number appears
    storage = set()
    # counter
    counter = 0
    # for each number in nums
    for num in nums:
        # add num to set
        storage.add(num)
    # for each number in set
    for num in storage:
        # add count times (n - 1) // 2 to calculate number of good pairs
        counter += ((nums.count(num) * (nums.count(num) - 1)) // 2)
    return counter
