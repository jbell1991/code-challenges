def sort_array_by_parity(A):
    # two new arrays that store odds and evens
    odds = []
    evens = []
    # iterate over each num in the list
    for num in A:
        # if num is odd
        if num % 2 != 0:
            # append to odds
            odds.append(num)
        # else
        else:
            # append to evens
            evens.append(num)
    # return evens + odds
    return evens + odds
