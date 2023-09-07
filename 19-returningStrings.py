
#  Returning Strings


'''
Make a function that will return a greeting statement that uses an input; your program should return, "Hello, <name> how are you doing today?".

[Make sure you type the exact thing I wrote or the program may not execute properly]
To return a string in Python, we use quotation marks to enclose it. Here
is an example:

```python
def greetings():
message = "Hello World!"
return message # This line returns the value of'message' as output from this function
print(greetings())   # Output will be 'Hello World!'

'''

def greet(name):
    #Good Luck (like you need it)
    message = "Hello, " + name + " how are you doing today?"
    return  message 
print(greet('Saif'))

#  another solutions

# 1
def greet(name):
    return "Hello, %s how are you doing today?" % name

'''
# 2
def greet(name):
    return "Hello, {} how are you doing today?".format(name)

'''
