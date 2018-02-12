#Autumn Franke (worked with Mandy)
#February 11th
#Part A


number = int(input('Enter a number: ' ))

def RecursionPractice():
    steps = 0

    while(number > 0):
        
        if number == 0:
            print(steps)
        elif number / 2:
            steps += 1
            print(steps)
        else:
            (number * 3) + 1
            steps += 1
            print(steps)

RecursionPractice()
