def repeated_n_times(A):
    # empty set
    storage = set()
    # iterate over the list
    for num in A:
        # if the num not in set
        if num not in storage:
            # add it to the set
            storage.add(num)
        # if the num in the set already it would be a duplicate
        else:
            # return that num
            return num
