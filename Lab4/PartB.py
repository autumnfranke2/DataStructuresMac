#Autumn Franke
# class work 
# part B
import time

a = int(input("enter number: "))

def fib(n):
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

    if(n <= 1):
        return(n)
    else:
        return (fibRecursive(n-1) + fibRecursive(n-2))

Recursion = ("recursion: ", fibRecursive(a), "runtime for recursion ", time.clock())


#PartC
fibList = [1,1]
n = a
for i in range(n):
    fibList.append(0)

    time.clock()
def fibDynamic(x):

    if fibList[x] == 0:
        fibList[x] = (fibDynamic(x-1) + fibDynamic(x-2))
    return fibList[x]

Dynamic = ("dynamic: ", fibDynamic(n), "runtime for Dynamic ", time.clock())



# Comparisons
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





