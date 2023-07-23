
# Create a function that takes an integer as an argument and returns 
# "Even" for even numbers or "Odd" for odd numbers.

def even_or_odd(number):
    
    if number %2 == 0:
#         print (number,"Even")
        return 'Even'
        
    else:
#         print(number,"Odd")
        return 'Odd'
print(even_or_odd(4)) # sortie ----> Even


#  this is another solution 

def even_or_odd(number):
	return 'Odd' if number % 2 else 'Even'
# using ternary operator to check whether the remainder of dividing by two with no decimal part equals
# zero, which means it's an even number
# ; otherwise its odd
# باستخدام عامل التشغيل الثلاثي للتحقق مما إذا كان باقي القسمة على اثنين بدون جزء عشري يساوي
# # صفر ، مما يعني أنه رقم زوجي
# # ؛ خلاف ذلك من الغريب

