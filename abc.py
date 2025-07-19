
list = []
for i in range(4):
    num = int(input("enter a list of number"))
    list.append(num)

print(list[0])
print(list[-1])

for x in list:
    print(x)
print(list[::-1])