

## Numbers
whole_num_1 = 10
whole_num_2 = 5
print("Adding whole numbers = ", whole_num_1+whole_num_2)

dec_1 = 10.5
dec_2 = 10.7
print("Adding decimals numbers (floats) = ", dec_1+dec_2)

## Text (known as strings)

str_1 = "10"
str_2 = "5"
print("Adding (concatenating) two strings = ", str_1 + str_2)

## lists of numbers
list_1 = [1,2,3,4,5,6]
print("List values = ", list_1)

# Add to the list, where in the list does the append add?
list_1.append(7)
print("List values after adding (appending) = ", list_1)

# Remove from a list, which number is removed?
# Hint, this removes by item passed in
list_1.remove(1)
print("List values after removing by value, with argument 1 = ", list_1)

# How many items are in the list, an you guess?
print("List size/length = ", len(list_1))

# Which item in the list is removed by below?
# Hint this removes by location in the list
list_1.pop(1)
print("List values after removing by location = ", list_1)

# Looping through a list (iterating)
sum_of_list_values = 0
for value in list_1:
    sum_of_list_values += value
print("The sum of the values in the list = ", sum_of_list_values)
