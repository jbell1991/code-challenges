def array_sign(nums):
    # # first pass solution
    # # set product variable equal to 1
    # prod = 1
    # # iterate over each num in nums
    # for num in nums:
    #     # multiply by product
    #     prod *= num
    # # return the sign of the numbers
    # if prod == 0:
    #     return 0
    # elif prod > 0:
    #     return 1
    # else:
    #     return -1
    
    # alternative solution
    # could count the positives and negatives
    # this way the count is just growing linearly rather than
    # a number that keeps getting multiplied and growing exponentially
    # count positives
    pos = 0
    # count negatives
    neg = 0
    # iterate over each num in nums
    for num in nums:
        # if num equals 0
        if num == 0:
            # return 0
            return 0
        # elif num > 0:
        elif num > 0:
            # increment pos by 1
            pos += 1
        # else
        else:
            # increment neg by 1
            neg += 1
    # if count of negatives is odd
    if neg % 2 != 0:
        # return negative
        return -1
    # else
    else:
        # return positive
        return 1
