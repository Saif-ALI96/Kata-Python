# Counting sheep...

# Consider an array/list of sheep where some sheep may be missing from their place. 
# We need a function that counts the number of sheep present in the array (true means present).

sheep_liste = [True,False,True,False,True,False,True,False,True]
'''
# def count_sheeps(sheep):
#     count = 0
#     for loop in sheep:
#         if loop == True: 
#             count +=1
#     return count
# print("Number of Sheep:",count_sheeps(sheep_list))'''


#  another solution :

# The count() method takes a single argument:

def count_sheeps():   
    return sheep_liste.count(True)
print ("Counted", count_sheeps(), "Sheep")   # ----> Counted 5 Sheep


 
        