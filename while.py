i = 0
number = []
while i<4:
    print("At first i is: ", i)
    number.append(i)
    print(number)
    i += 1
    print("i at bottom is :", i)

print("Number contains: ", end = " ")
for num in number:
    print (num, end = " ")