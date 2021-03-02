def maximum_wealth(accounts):
    # iterate over each list of accounts
    for i, account in enumerate(accounts):
        # change the element to the sum of the elements
        accounts[i] = sum(account)
    # take the max of the summed elements
    return max(accounts)
