# to check if number is prime or not
num = int(input("Enter a number :"))
flag = False
if num == 0 or num == 1:
    print(num, "is not prime")
elif num > 1:
    for i in range(2,num):
        if(num%i) == 0 :
            flag = True
            break
if flag:
    print(num, " is not a prime number ")
else:
    print(num, " is a prime number")

    
