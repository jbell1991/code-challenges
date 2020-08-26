def find_numbers(nums):
    # counter
    counter = 0
    # iterate over the list of nums
    for num in nums:
        # if the len of the string of the num % 2 == 0
        if len(str(num)) % 2 == 0:
            # add 1 to the counter
            counter += 1
    # return counter
    return counter
