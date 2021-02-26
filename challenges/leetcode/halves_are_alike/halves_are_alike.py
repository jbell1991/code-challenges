def halves_are_alike(s):
    # split s in two
    first_half = s[:int(len(s)/2)]
    second_half = s[int(len(s)/2):]
    # count vowels
    first_count = 0
    second_count = 0
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    for char1, char2 in zip(first_half, second_half):
        if char1 in vowels:
            first_count += 1
        if char2 in vowels:
            second_count += 1
    return first_count == second_count
