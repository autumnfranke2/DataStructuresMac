# FizzBuzz
#Autumn (worked with Mandy)

import math

# divisable by 3 = fizz
# divisable by 5 = buzz

for x in range(1,101):

    if x % 3 == 0 and x % 5 == 0:
        print (x,"FizzBuzz")
        
    elif x % 3 == 0:
        print (x,"Fizz")
        
    elif x % 5 == 0:
        print (x,"Buzz")
        
    else:
        print (x)


