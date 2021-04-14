def reverse_integer(x):
    # if the length of the number is 1
    if len(str(x)) == 1:
        # return x
        return int(x)
    # elif integer is positive
    elif x > 0:
        # empty string
        s = ""
        # iterate over reversed str of int
        for digit in reversed(str(x)):
            # add digit to string
            s += digit
        # if s outside 32-bit range on high end
        if int(s) > ((2**31) - 1):
            # return 0
            return 0
        # else
        else:
            # return reversed int
            return int(s)
    elif x < 0:
        # empty string
        s = ""
        # change int to str
        x = str(x)
        # remove negative
        x = x[1:]
        # iterate over reversed str of int
        for digit in reversed(str(x)):
            # add digit to string
            s += digit
        # if s outside 32-bit range on low end
        if (-2**31) > (int(s) * -1):
            # return 0
            return 0
        # else
        else:
            # return reversed int and negate
            return int(s) * -1
        