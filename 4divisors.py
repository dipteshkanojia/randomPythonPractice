__author__ = 'dipteshkanojia'

askNumber = int(input("Please enter a number: "))
for i in range(2, int(askNumber/2)):
    if(int(askNumber) % i == 0):
        print(i)
