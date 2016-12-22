def inputNum():
    num = int(input("Enter a number: "))
    mod = num % 2
    if(mod>0):
        print("Odd Number! you Idiot!")
    else:
        print("Even Number! a wise choice!")

def inputNumExtras():
    num = int(input("Enter a number: "))
    checkNum = int(input("Enter a number to divide by: "))

    if num % 4 == 0:
        print(num, " is a multiple of 4")
    elif num %2 == 0:
        print(num, " is an even number")
    else:
        print(num, " is an odd number")

    if num % checkNum == 0:
        print(num, " is divisible by ", checkNum)
    else:
        print(num, " is not divisible by ", checkNum)


#inputNum()
inputNumExtras()
