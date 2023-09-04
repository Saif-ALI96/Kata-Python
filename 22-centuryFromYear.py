
# Century From Year

'''
Introduction
The first century spans from the year 1 up to and including the year 100, the second century - from the year 101 up to and including the year 200, etc.

Task
Given a year, return the century it is in.

Examples
1705 --> 18
1900 --> 19
1601 --> 17
2000 --> 20
'''
import math 
def century(year):
    # Finish this :)
    return math.ceil(year/100)
# + (int((year%100)/10)==0)*-1
print('the century is :' + str(century(1805)))  # --> the century is :19


#  another solutions 
#  1
import math
def century(year):
    # Finish this :)
    new_year = int(year) / 100
    
    return math.ceil(new_year)

# 2 

def century(year):
    if year % 100==0:
        return year//100
    else:
        return year//100+1
    
#  3
def century(year):
    return (year / 100) if year % 100 == 0 else year // 100 + 1