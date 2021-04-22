def average_salary(salary):
    # one liner
    # sort the list from low to high
    # take the average of the list from [1:-1]
    return sum(sorted(salary)[1:-1])/(len(salary) - 2)
    
    # alternative solutions
    
    # remove the max and min from the list
    # salary.remove(max(salary))
    # salary.remove(min(salary))
    # # return the average of the remaining numbers
    # return sum(salary) / len(salary)
    
    # # sort the list
    # salary = sorted(salary)
    # # sum variable 
    # total = 0
    # # iterate over the sorted list from [1:-1]
    # for num in salary[1:-1]:
    #     # add each num to sum
    #     total += num
    # # return sum / len(list) - 2
    # return total / (len(salary) - 2)
