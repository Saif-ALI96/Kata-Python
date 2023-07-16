# Beginner - Lost Without a Map

'''
Given an array of integers, return a new array with each value doubled.

For example:

[1, 2, 3] --> [2, 4, 6]
'''
def maps(a):
    num = []
    for i in a:
        num.append(i * 2)
    return num
print (maps([1,2,4,5]))



# def maps(a):
#     pass
#     return [x * 2 for x in a]