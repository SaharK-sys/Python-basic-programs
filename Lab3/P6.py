# to read three numbers and print them in ascending order 
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))
if(((a<b) and (a<c)) and (b<c)):
    print( a, b, c)
elif(((b<a) and (b<c)) and (a<c)):
    print(b, a, c)
elif(((c<a) and (c<b)) and (b<a)):
    print(c, b, a)
elif(((a<b) and (a<c)) and (c<b)):
    print(a, c, b)
elif(((b<a) and (b<c)) and (c<a)):
    print(b, c, a)
elif(((c<a) and (c<b)) and (a<b)):
    print(c, a, b)
else:
    print("2 or all numbers are equal")

    

    
    








