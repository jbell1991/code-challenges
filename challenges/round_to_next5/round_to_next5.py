def round_to_next5(n):
    # if is evenly divisible by 5
    if n % 5 == 0:
        # return n
        return n
    # else
    else:
        # add 1 to n using recursion until true
        return round_to_next5(n + 1)
