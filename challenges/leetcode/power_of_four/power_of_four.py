def power_of_four(n):
    if n < 1:
        return False
    while n > 1:
        n /= 4
    return True if n == 1 else False
