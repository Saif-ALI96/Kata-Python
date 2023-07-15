
# Convert a String to a Number!

# Description
# We need a function that can transform a string into a number. What ways of achieving this do you know?

# Note: Don't worry, all inputs will be strings, and every string is a perfectly valid representation of an integral number.





def string_to_number(s):
    # your code here
    pass
    return int(s)

print(string_to_number('23'))  # ---> 23 


# another solution

def string_to_number(s):
    # ... your code here
    try:
        return int(s)
    except (ValueError):
        return "Input is not valid " 