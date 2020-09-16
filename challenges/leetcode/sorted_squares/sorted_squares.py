def sorted_squares(A):
    # iterate over the array
    for i in range(len(A)):
        # change index to squared num
        A[i] = A[i]**2
    # return sorted array
    return sorted(A)
    