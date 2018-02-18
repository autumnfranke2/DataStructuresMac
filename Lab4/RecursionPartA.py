#Autumn Franke (worked with Mandy)
#February 11th
#Part A

def RecursionPractice(number):
    
    steps = 0

    while(number > 1):
        
        if number % 2 == 0:
            steps += 1
            number = number / 2
        else:
            number = (number * 3) + 1
            steps += 1
    print("total steps: ", steps)

RecursionPractice(number = int(input('Enter a number: ' )))
