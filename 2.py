input_string = "Hello, World!"

uppercase_count = sum(1 for letter in input_string if letter.isupper())
lowercase_count = sum(1 for letter in input_string if letter.islower())

print("Original string : ", input_string)
print("Number of uppercase letters : ", uppercase_count)
print("Number of lowercase letters : ", lowercase_count)
