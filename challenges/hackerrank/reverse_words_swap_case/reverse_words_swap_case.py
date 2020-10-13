def reverse_words_order_and_swap_cases(sentence):
    # empty string
    new_sentence = ""
    # iterate over each character the string
    for char in sentence:
        # if character is lower
        if char.islower():
            # set it equal to upper
            new_sentence += char.upper()
        # elif charcter is upper
        elif char.isupper():
            # set it equal to lower
            new_sentence += char.lower()
        # elif character is space
        elif char.isspace():
            # add space
            new_sentence += char
    # convert sentence to list of words using split
    new_sentence = new_sentence.split()
    # reverse list
    new_sentence.reverse()
    # convert reversed list back to string
    return " ".join(new_sentence)
