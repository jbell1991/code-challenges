def sales_by_match(n, ar):
    # count pairs
    pairs = 0
    # empty dict
    d = {}
    # group each color with count of color
    # dictionary with key as color and value as count
    for num in ar:
        if num not in d:
            d[num] = 1
        else:
            d[num] += 1
    # iterate over dictionary values
    for value in d.values():
        # if value count is > 2 and % 2 != 0 (odd)
        if value > 2 and value % 2 != 0:
            # subtract 1 from the value
            value -= 1
            # add value / 2 to pairs
            pairs += int(value / 2)
        # elif value count > 2 and % 2 == 0 (even)
        elif value > 2 and value % 2 == 0:
            # add value / 2 to pairs
            pairs += int(value / 2)
        # elif value count == 2
        elif value == 2:
            # add 1 to pairs
            pairs += 1
    # return pairs
    return pairs
