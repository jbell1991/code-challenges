def power_of_two(n):
    # set exponent variable
    exponent = 0
    # while 2 to the exponent is less than or equal to n
    while 2**exponent <= n:
        # if 2 to the exponent is equal to n
        if 2**exponent == n:
            # return True
            return True
        # else increment the exponent by 1
        else:
            exponent += 1
    return False
