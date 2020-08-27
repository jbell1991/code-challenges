def three_consecutive_odds(arr):
    # odds counter
    odds_counter = 0
    # iterate over the array
    for i in range(len(arr) + 1):
        # if the odds counter equals 3
        if odds_counter == 3:
            # return true
            return True
        # if reached end of the list without finding 3 consecutive odds
        elif i == len(arr):
            return False
        # if number is odd
        elif arr[i] % 2 != 0:
            # add to the odds counter
            odds_counter += 1
        # elif number is even
        else:
            # reset the odds counter to 0
            odds_counter = 0
