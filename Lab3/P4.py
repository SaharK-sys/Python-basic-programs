# to read three numbers and if any two variables are equal, print that number
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))
if((a==b) and (b==c)):
    print("all numbers are equal", a)
elif(a== b ):
    print("first number = second number", a)
elif(b==c):
    print("second number = third number", b)
elif(c==a):
    print("first number = third number", a)

else:
    print("none of the numbers is equal")
    
    








