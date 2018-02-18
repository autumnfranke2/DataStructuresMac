#Autumn Franke
# class work 
# Fib
import time

def fib(n):
    time.clock()
    time.clock()
    x = 1
    y = 1
    z = 0
    
    for i in range(n):
        z = x + y
        x = y
        y = z

    return(y, "runtime for non-recursion " ,time.clock())



def fibRecursive(n):
    time.clock()
    time.clock()

    if(n<1):
        return(1)
    else:
        return (fib(n-1) + fib(n-2))
    return ("runtime for recursion ", time.clock())

print(fib(50))
print(fibRecursive(50))
