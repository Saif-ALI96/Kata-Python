


# Grasshopper - Summation

# Summation
# Write a program that finds the summation of every number from 1 to num. The number will always be a positive integer greater than 0.

# For example (Input -> Output):

# 2 -> 3 (1 + 2)
# 8 -> 36 (1 + 2 + 3 + 4 + 5 + 6 + 7 + 8)


def summation(num):
    return (int(num/2))*(int(1+num))
print('the number is ', summation(8)) # srotie ----> the number is  36



#  another solution 

def summation1(num):
    return sum(range(num+1))
# using built-in function range() and the "sum" method to calculate the total of numbers
# from one till given num.
print(f'the sum is {summation(2)}')