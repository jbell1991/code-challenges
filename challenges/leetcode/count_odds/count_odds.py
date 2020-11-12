def count_odds(low, high):
    # if high minus low + 1 is even
    if (high - low + 1) % 2 == 0:
        # the number of evens and odds will be the same
        return int((high - low + 1) / 2)
    # if high - low + 1 is odd
    elif (high - low + 1) % 2 != 0:
        # if high and low are odd numbers
        if high % 2 != 0 and low % 2 != 0:
            return int(((high - low) / 2) + 1)
        else:
            return int((high - low) / 2)
