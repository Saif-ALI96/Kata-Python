

# Remove String Spaces

# Write a function that removes the spaces from the string, then return the resultant string.





def remove_spaces(string):
    return string.replace(" ", "")
print('{}' .format(remove_spaces('hello world my name is Saif')))
# sortie -----> helloworldmynameisSaif



# another solution 

def no_space(x):
    return "".join(x.split())
print(no_space('hello world'))   # sortie ----> helloworld
