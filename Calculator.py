def operator(cond, num1, num2):
    if cond=="-":
        return num1-num2
    elif cond=='*':
        return num1*num2
    elif cond=='/':
        return num1/num2
    elif cond=="+":
        return num1+num2
    else:
        print("You enter wrong input. Try Again")
        operator(cond, num1, num2)
cnt = 0
first_num = 0
while cnt<5:
    if cnt == 0:
        num_1 = input("Enter num1: ")
    data = input("enter choice: +, -, /, * => ")
    num_2 = input("Enter num2: ") 
    result = operator(data, int(num_1), int(num_2))
    print("current result on cnt: {}  is: {}".format(cnt, result))
    num_1 = result
    cnt += 1
print("\nfinal result is: ",result)

x = input("Are you Happy  Y / N ")
