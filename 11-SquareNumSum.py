
'''# Square(n) Sum

# Complete the square sum function so that it squares 
# each number passed into it and then sums the results together.

# For example, for [1, 2, 2] it should return 9 

# def square_sum(numbers):
# your code here
#     return sum([num*num for num in numbers])
'''
# print (square_sum ([2, 2])) # sortie 8


def square_sum2(number):
    result = 0
    for num in number:
        result = result + num*num 
        return result
print(square_sum2([4,4])) # sortie ----> 16

#  another solution 
import numpy

def square_sum(numbers):
    return sum(numpy.array(numbers) ** 2)


# def square_sum(numbers):
#     return sum(x ** 2 for x in numbers)
       
