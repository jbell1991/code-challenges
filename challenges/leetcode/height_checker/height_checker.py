def height_checker(heights):
    # sort list of heights from low to high
    expected = sorted(heights)
    # counter
    counter = 0
    # iterate over both the heights and expected
    for height, expect in zip(heights, expected):
        # if values do not match
        if height != expect:
            # increment counter by 1
            counter += 1
    # return counter
    return counter
