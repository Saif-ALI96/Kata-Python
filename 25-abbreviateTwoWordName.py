
# Abbreviate a Two Word Name

'''
Write a function to convert a name into initials. 
This kata strictly takes two words with one space in between them.

The output should be two capital letters with a dot separating them.

It should look like this:

Sam Harris => S.H

patrick feeney => P.F
'''


def abbrev_name(name):
        
    initial  = '.'.join([loop[0].upper() for loop in name.split(' ')])
    return initial
print(abbrev_name('Hello World'))



#  another solution
# 1
def abbrev_name(name):
    # Convert name to uppercase
    uppername = name.upper()
    # Split string
    seprate_words = uppername.split()
    # Get first letters
    letters = [word[0] for word in seprate_words]
    # Return + join letters with a seperating "."
    return (".".join(letters))