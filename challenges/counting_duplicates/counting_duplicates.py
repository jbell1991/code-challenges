def duplicate_count(text):
    '''Takes in string of text and returns the count of 
    duplicate characters in the string.
    '''
    # empty dictionary
    dict = {}
    # make text lowercase
    text = text.lower()
    # iterate over each character in the text
    for char in text:
        # if the character is not in the dictionary
        if char not in dict:
            # create a key and assign the value to 1
            dict[char] = 1
        else:
            # add 1 to the value
            dict[char] += 1
    # count how many characters have values > 1
    count = 0
    # iterate over each value in the dictionary values
    for value in dict.values():
        # if the value is greater than 1 it counts a duplicate
        if value > 1:
            count += 1
    return count
