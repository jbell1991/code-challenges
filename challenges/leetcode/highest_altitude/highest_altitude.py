def highest_altitude(gain):
    # start at zero
    current_altitude = 0
    # list containing the start altitude of 0
    altitudes = [0]
    # iterate through the list gain
    for num in gain:
        # add each net change in altitude to start
        current_altitude += num
        # add current altitude to empty list
        altitudes.append(current_altitude)
    # return the max of the empty list
    return max(altitudes)
