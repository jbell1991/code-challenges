def find_special_int(arr):
    # 25% threshold
    threshold = .25
    # store the count for each arr in a dictionary
    # empty dict
    dict = {}
    # for num in arr:
    for num in arr:
        # if the num not in dict
        if num not in dict:
            # add it to the dict and make value 1
            dict[num] = 1
        # if num in dict already
        else:
            # add 1 to the value
            dict[num] += 1
    # iterate over the dictionary values
    for key, value in dict.items():
        # if value / len(arr) > 25% threshold
        if (value / len(arr)) > threshold:
            # return the key
            return key
