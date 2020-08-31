def kids_with_candies(candies, extraCandies):
  output_list = []
  max_candies = max(candies)
  for candy in candies:
    total = candy + extraCandies
    if total >= max_candies:
      output_list.append(True)
    else:
      output_list.append(False)
  return output_list
