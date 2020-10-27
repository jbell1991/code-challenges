def max_product(nums):
    # empty list
    l = []
    # iterate over each index i in nums
    for i in range(len(nums)):
        # iterate over each index j in nums again
        for j in range(len(nums)):
            # if i != j
            if i != j:
                # multiply nums[i]-1 by nums[j]-1 and append it to a list
                l.append((nums[i] - 1) * (nums[j] - 1))
    # return the max value from that list
    return max(l)
