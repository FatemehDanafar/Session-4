n1 = int(input("Enter first Number: "))
n2 = int(input("Enter second Number: "))
if n1 > n2:
    kmm = n1
else:
    kmm = n2
while  kmm % n1 != 0 or kmm % n2 != 0:
         kmm +=1
print("kmm is: ",kmm)