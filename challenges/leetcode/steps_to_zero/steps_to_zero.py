def steps_to_zero(num):
    # steps
    steps = 0
    # while num is not equal to zero
    while num != 0:
        # if the num is even
        if num % 2 == 0:
            # divide it by two
            num = num / 2
            # increment steps by one
            steps += 1
        # if the num is odd
        else:
            # subtract one
            num = num - 1
            # increment steps by one
            steps += 1
    # once loop is exited return steps
    return steps
