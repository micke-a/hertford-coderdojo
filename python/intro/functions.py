

# Note use of "def" to define the function and giving it a name "sum_list"
# the_list is what is called a parameter to the function, what we give it to do stuff
def sum_list(the_list):
    result = 0
    for value in the_list:
        result += value
    return result


# Now we can use the summing function loads of times, no need to write that over and over again :)
print("Sum 1 = ", sum_list([1,2,3,4,5,6]))
print("Sum 1 = ", sum_list([10,20,30]))

