def power_of_three(n):
    # exponent variable
    exponent = 0
    # while 3**exponent <= n
    while 3**exponent <= n:
        # if 3**exponent == n
        if 3**exponent == n:
            # return True
            return True
        # else
        else:
            # increment the exponent by 1
            exponent += 1
    # return False
    return False
