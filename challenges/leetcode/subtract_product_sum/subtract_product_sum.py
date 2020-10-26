def subtract_product_sum(n):
    # product variable
    product = 1
    # sum variable
    sum = 0
    # iterate over each integer
    for num in str(n):
        # multiply by product variable
        product *= int(num)
        # add each integer to sum
        sum += int(num)
        # return product - sum
    return product - sum
