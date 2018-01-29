# read files with numbered lines
#Autumn (worked with Mandy)

counter = 0

infile = open((input("Name of file (include extension): ")),"r")
for line in infile.readlines():
    print(counter, line)
    counter = counter + 1
