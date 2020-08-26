def persistence(n, count=0):
    # convert the int to str to iterate over it
    n = str(n)
    # base case - if the length of the str is 1
    if len(n) == 1:
        # return the count of function calls it took to get there
        return count
    else:
        multiplier = 1
        # iterate over each digit in the number
        for digit in n:
            # multiply each digit by the next
            multiplier *= int(digit)
        # recursively call the function and update the count
        return persistence(multiplier, count + 1)
