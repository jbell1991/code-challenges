def decompress_RLElist(nums):
    # empty list
    l = []
    # iterate over every other num in nums
    for i in range(0, len(nums), 2):
        # val = first num
        val = nums[i]
        # freq = second num
        freq = nums[i + 1]
        # append val * [freq] to empty list
        l = l + (val * [freq])
    # return l
    return l
