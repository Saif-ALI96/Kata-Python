
# Beginner Series #2 Clock 

'''
Clock shows h hours, m minutes and s seconds after midnight.

Your task is to write a function which returns the time since midnight in milliseconds.

Example:
h = 0
m = 1
s = 1

result = 61000
Input constraints:

0 <= h <= 23
0 <= m <= 59
0 <= s <= 59
'''

def past(hour, minutes, second):
    return hour * 60 * 60 * 1000 + minutes * 60 * 1000 + second * 1000

print(past(1,1,1))   # sortie ----> 3661000


