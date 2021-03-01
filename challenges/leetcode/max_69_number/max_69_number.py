def max_69_number(num):
    num = list(str(num))
    l = [int("".join(num))]
    for i, digit in enumerate(num):
        # change the six to a 9
        num = list(str(l[0]))
        if num[i] == '9':
            num[i] = '6'
        else:
            num[i] = '9'
        l.append(int("".join(num)))

    return max(l)
