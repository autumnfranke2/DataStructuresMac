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

#PartC

def fibDynamic(n):
    fibList = [0,1]
    time.clock()
    time.clock()

    if(n <= 1):
        return(fibList[n])
    else:
        fibList.append(fibList[n-1] + fibList[n-2])
    return fibList[n]
    

Dynamic = ("dynamic: ", fibDynamic(a), "runtime for Dynamic ", time.clock())


def timeComparison():
    nonRecursiveTime = nonRecursion[3:4]
    RecursiveTime = Recursion[3:4]
    DynamicTime = Dynamic[3:4]
    if (nonRecursiveTime > RecursiveTime and DynamicTime > RecursiveTime):
        return("Recursion was faster")
    elif (RecursiveTime > nonRecursiveTime and DynamicTime > nonRecursiveTime):
        return("non Recursion was faster")
    else:
        return("Dynamic programming was faster")


print(nonRecursion)
print(Recursion)
print(Dynamic)
print(timeComparison())





