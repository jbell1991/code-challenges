def kth_factor(n, k):
    # come up with list of factors
    factors = []
    # counter
    counter = 0
    # iterate over range 1 to n
    for i in range(1, n+1):
        # if n % i == 0
        if n % i == 0:
            # append i to factors
            factors.append(i)
            # counter
            counter += 1
    if n == 1:
        return 1
    # if k > len(factors)
    elif k > len(factors):
        # return -1
        return -1
    # else
    else:
        return factors[k-1]
