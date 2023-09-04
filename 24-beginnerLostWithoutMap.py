# Beginner - Lost Without a Map

'''
Given an array of integers, return a new array with each value doubled.

For example:

[1, 2, 3] --> [2, 4, 6]
'''
def maps(a):
    numbre = []
    for i in a:
        numbre.append(i * 2)
    return numbre
print (maps([1,2,4,5]))


#  another solution 
# 1
def maps(a):
    pass
    return [x * 2 for x in a]

# 2

def maps(a):
    return list(map(lambda s: s*2, a))

'''
using map() function to iterate over the list and multiply by two at once
```python
nums=[1,2,3,4,5]
double_num=list(map((lambda y :y*2), nums))
# using lambda expression inside map(). Here we are doubling all elements present in 'nums' list
one-by-one without any loop or iteration through it. The result is stored back into variable
called "double_num".

'''

test = [1,2,3,4,5]
for loop in range(len(test)):
    test[loop] *= 2
print(test)

