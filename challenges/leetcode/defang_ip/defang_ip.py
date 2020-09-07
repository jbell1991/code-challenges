def defang_ip(address):
    # one line solution using .replace method
    # return address.replace('.', '[.]')
    # empty string
    defanged_ip = ""
    # iterate over each char in the address
    for char in address:
        # if char is a .
        if char == ".":
            # set it to [.]
            defanged_ip += "[.]"
        else:
            defanged_ip += char
    # return defanged ip
    return defanged_ip
