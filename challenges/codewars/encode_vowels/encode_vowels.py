def encode(st):
    # dictionary with vowels as keys and numbers as values
    encoding = {'a': 1, 'e': 2, 'i': 3, 'o': 4, 'u': 5}
    # iterate over each key value pair in dictionary
    for k, v in encoding.items():
        # if key in st
        if k in st:
            # replace key with value
            st = st.replace(k, str(v))
    return st


def decode(st):
    # dictionary with numbers as keys and vowels as values
    decoding = {'1': 'a', '2': 'e', '3': 'i', '4': 'o', '5': 'u'}
    # iterate over each key value pair in dictionary
    for k, v in decoding.items():
        # if key in st
        if k in st:
            # replace key with value
            st = st.replace(k, str(v))
    return st
