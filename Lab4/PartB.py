#Autumn Franke
# class work 
# part B
import time

a = int(input("enter number: "))

def fib(n):
    time.clock()
    time.clock()
    
    x = 1
    y = 1
    z = 0
    
    for i in range(n-2):
        z = x + y
        x = y
        y = z
    return(y)

nonRecursion = ("non-recursion: ", fib(a), "runtime for non-recursion ", time.clock())

def fibRecursive(n):
    time.clock()
    time.clock()

    if(n <= 1):
        return(n)
    else:
        return (fibRecursive(n-1) + fibRecursive(n-2))

Recursion = ("recursion: ", fibRecursive(a), "runtime for recursion ", time.clock())


nonRecursiveTime = nonRecursion[3:4]
RecursiveTime = Recursion[3:4]



def timeComparison():
    if nonRecursiveTime > RecursiveTime:
        return("Recursion was faster")
    else:
        return("non Recursion was faster")



print(nonRecursion)
print(Recursion)
print(timeComparison())
