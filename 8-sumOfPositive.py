
# Sum of positive

# You get an array of numbers, return the sum of all of the positives ones.

# Example [1,-4,7,12] => 1 + 7 + 12 = 20

# Note: if there is nothing to sum, the sum is default to 0.

def positive_sum(arrey):
    total = 0
    for num in arrey:
        if num > 0:
            
            total += num
    return total
print(positive_sum([-1,5,8,4,-5]))  # sortie ----> 17 
#  il sum que les chiffres positives 




#  another solution 
def positive_sum(arr):
    # Your code here
    total = 0
    if not arr:
        return 0
    else:
        for loop in arr:
            if loop > 0:
                total += loop 
        return total