n = int(input("Enter the Number:"))
number = [1,1]
for i in range(2,n):
    f= number[i-1]+number[i-2]
    number.append(f)
    print(number)
