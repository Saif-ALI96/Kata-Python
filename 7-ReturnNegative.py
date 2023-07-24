

#  Return Negative

# In this simple assignment you are given a number and have to make it negative.
#  But maybe the number is already negative?

def make_negative( number ):
    pass
    return -abs(number)

#  abs() retrun le number vers le positive et le 
# -abs() retrun le number vers le negative 
print(make_negative(45)) # sorite ----> -45


#  another solution 

def make_negative( number ):
    return -number if number>0 else number
