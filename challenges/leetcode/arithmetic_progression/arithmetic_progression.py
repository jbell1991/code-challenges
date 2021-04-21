def arithmetic_progression(arr):
    # sort array in ascending order
    arr = sorted(arr)
    # difference between first two elements
    first_diff = arr[1] - arr[0]
    # iterate over each number in the sorted array starting with second element
    for i in range(1, len(arr)-1):
        # calculate the diff between each number
        diff = arr[i+1] - arr[i]
        # if diff between any two consecutive elements does not equal first_diff
        if diff != first_diff:
            # return False
            return False
    # else return True
    return True
    