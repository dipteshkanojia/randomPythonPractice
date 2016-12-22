def charInput():
    import time
    name = input("What is your name: ")
    age = int(input("How old are you: "))
    year = str((int(time.strftime("%Y"))-age)+100)
    print(name + " will be 100 years old in the year " + year)

charInput()
