def replace_elements(arr):
    # iterate over each index in the array
    for i in range(0, len(arr)-1):
        # replace the element with the max of the slice
        # of the array on the right side of the element
        arr[i] = max(arr[i+1:])
    # replace the last element with -1
    arr[-1] = -1
    # return arr
    return arr
