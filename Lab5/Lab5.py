#Autumn Franke
#Searches and Algorithms
#Worked with Mandy


import time
import wordlist

wordInput = input("Enter the word you want to search for: ")

Wordfile = wordlist.word

def LinearSearch():
    count = 0
    time.clock()
    
    for i in range(len(Wordfile)):
        if Wordfile[i] == wordInput:
            return(i, wordInput, time.clock())
        else:
            if Wordfile[i] != wordInput:
                count += 1
                print(count)
          

def RecursiveBinarySearch():
    pass
    #for i in range(len(Wordfile)):
    #if the midpoint == wordInput:
        #print index and word
    #else:
        #check the midpoint
        #drop half that the word isnt in



print(LinearSearch())
