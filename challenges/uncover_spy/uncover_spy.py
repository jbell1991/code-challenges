def uncover_spy(n, trust):
    # the spy has to be trusted by everyone
    # the spy trusts no one

    # list of people in the city-state
    people = []
    # list of people who trust others
    trusting = []
    # list of people who are trusted
    trusted = []

    # add n people to the people list
    for person in range(1, n + 1):
        people.append(person)
    # for each arr in trust input
    for arr in trust:
        # put the first element in the trusting list
        trusting.append(arr[0])
        # put the second element in the trusted list
        trusted.append(arr[1])
    # iterate through the people
    for person in people:
        # if the person trusts no one and is trusted by everyone (but themselves)
        if person not in trusting and trusted.count(person) == (n - 1):
            # that person is the spy
            return person
    # otherwise there is no spy
    return -1
