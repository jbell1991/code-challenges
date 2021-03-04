def count_matches(items, ruleKey, ruleValue):
    # counter
    count = 0
    # iterate through each item
    for item in items:
        # if rulekey == "type" and rulevalue == item[0]
        if ruleKey == "type" and ruleValue == item[0]:
            # count += 1
            count += 1
        # elif rulekey == "color" and rulevalue == item[1]
        elif ruleKey == "color" and ruleValue == item[1]:
            # count += 1
            count += 1
        # elif rulekye == "name" and rulevalue == item[2]
        elif ruleKey == "name" and ruleValue == item[2]:
            # count += 1
            count += 1
    # return count
    return count
