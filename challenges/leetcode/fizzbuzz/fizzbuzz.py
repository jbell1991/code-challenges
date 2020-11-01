def fizz_buzz(n):
    # empty list
    l = []
    # iterate over each number from range 1 to n
    for i in range(1, n + 1):
        # if num % 3 == 0 and num % 5 == 0:
        if i % 3 == 0 and i % 5 == 0:
            # append "FizzBuzz" to the list
            l.append("FizzBuzz")
        # elif num % 3 == 0:
        elif i % 3 == 0:
            # append "Fizz" to the list
            l.append("Fizz")
        # elif num % 5 == 0:
        elif i % 5 == 0:
            # append "Buzz" to the list
            l.append("Buzz")
        # else
        else:
            # append num to the list
            l.append(str(i))
    # return list
    return l
