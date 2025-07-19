list []
for i in range(4):
    num = int(input("enter a numbers"))
    list.append(num)

tuple = tuple(list)
for x in tuple:
    print(x)
