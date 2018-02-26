#List Sorts
#Autumn Franke
#Class


listofN = [7,5,4,1,9,0,3,-2,21,-6,13]
sortedlist = sorted(listofN)


#Bubble Sort

def bubbleSort(list):
    for i in range(len(list)-1):
        for i in range (len(list)-1):
            first = list[i]
            second = list[i+1]
            

            if (first > second):
                swap = first
                list[i] = second
                list[i+1] = swap
                

    return list

print(listofN)
print(sortedlist)
print(listofN == sortedlist)
print(bubbleSort(listofN))
print(bubbleSort(listofN) == sortedlist)
