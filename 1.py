from functools import reduce

numbers = [2, 4, 6, 8, 10]

product = reduce((lambda x, y: x * y), numbers)

print("The product of all the numbers in the list is:", product)