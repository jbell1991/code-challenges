def reverse_vowels(s):
    # list of vowels
    vowels = "aeiouAEIOU"
    # convert string to list
    string_list = list(s)
    # empty list to store matching vowels
    matches = []
    # iterate over the list of characters
    for char in string_list:
        # if character in vowels
        if char in vowels:
            # add it to another list
            matches.append(char)
    # reverse the list
    matches.reverse()

    # iterate over the list again
    for i, char in enumerate(string_list):
        # if char in vowels
        if char in vowels:
            # replace it with char at 0th index position
            string_list[i] = matches[0]
            # pop 0th index from list
            matches.pop(0)
    return "".join(string_list)
