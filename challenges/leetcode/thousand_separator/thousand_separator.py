def thousand_separator(n):
    # empty string
    s = ""
    # counter
    counter = 0
    # if len of n > 3
    if len(str(n)) > 3:
        # iterate over str(n) in reverse
        for num in reversed(str(n)):
            # add each number to empty string
            s += num
            # increment counter by 1
            counter += 1
            # when count is a mulitple of 3
            if counter % 3 == 0:
                # add a "." to the string
                s += "."
        # return reversed string
        s = s[::-1]
        # if s starts with a .
        if s[0] == ".":
            return s[1:]
        else:
            return s
    # else
    else:
        # return str(n)
        return str(n)
