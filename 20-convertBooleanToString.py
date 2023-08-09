
# Convert a Boolean to a String


'''
Implement a function which convert the given boolean value into its string representation.

Note: Only valid inputs will be given.
Function Signature: boolToString (boolean) -> str
Example Input 1 : True
Output         : "true"
Explanation    : The input is true, so we need to return the corresponding string "true".   
Example Input 2 : False
Output         : "false"
Explanation    : Similarly for false case also it returns as output with capital F in front of word     

print(str(True)) # Output: 'True'
'''

def boolean_to_string(b):
    #your code here
    if b == True:
        return "True , is covert as a stirng"
    else:
        return "False , is covert as a string"

print(boolean_to_string(False))

#  another solutions

# 1

def boolean_to_string(b):
    return str(b)

#  2

def boolean_to_string(b):
    return 'True' if b else 'False'

#  3

def boolean_to_string(b):
    return str(b)