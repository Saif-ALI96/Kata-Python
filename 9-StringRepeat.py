
# String repeat

# Write a function that accepts an integer n and a string s as parameters,
#  and returns a string of s repeated exactly n times.


def repeat_str(repeat, string):
    
    repeatition = repeat * string
    
    return repeatition 


# another solution 

def repeat_str(repeat, string):
    solution = ""
    for i in range(repeat):
        solution += string
    return solution


#  another one
from operator import mul as repeat_str