def count_negatives(grid):
    return len([1 for arr in grid for num in arr if num < 0])
