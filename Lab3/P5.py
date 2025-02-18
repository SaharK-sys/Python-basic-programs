# to read three numbers and find the smallest among them
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))
if((a<b) and (a<c)):
    print("First number is smallest", a)
elif((b<a) and (b<c)):
    print("Second number is smallest", b)
elif((c<a) and (c<b)):
    print("Third number is smallest", c)
else:
    print("numbers are equal")
    
    








