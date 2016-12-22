mylist = [1, 5, 6, 10, 11, 112, 1235, 2, 2345]

num = int(input("Choose a number: "))

new_list = []

for i in mylist:
    if i < num:
        new_list.append(i)

print(new_list)

new_list = []
#OneLiner
new_list = list(filter((lambda x:x<num),[1, 5, 6, 10, 11, 112, 1235, 2, 2345]))

print(new_list)
