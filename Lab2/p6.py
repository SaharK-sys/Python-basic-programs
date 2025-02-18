# to find factorial of a number
n = int(input(" Enter number whose factorial you want to find "))
fact = 1
for i in range (1, n+1):
    fact = fact * i
    print(fact)
    
