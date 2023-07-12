# 
# Remove First and Last Character

# It's pretty straightforward. Your goal is to create a function that removes the first and last characters of a string. You're given one parameter, the original string.
#  You don't have to worry with strings with less than two characters.

def remove_char(s):
    #your code here
    return s[1:-1]

print(remove_char('hello world'))  # sortie -----> ello worl


# another solution 

remove_char=lambda s: s[1:-1]


# another solution 

def remove_char(s):
    return s[1:len(s)-1]