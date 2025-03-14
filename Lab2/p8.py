# 1 1 2 3 5 8 13

n= 7
a = 1
b = 1
count = 0 
while count < n :
    print(a)
    fib = a + b
    a = b
    b = fib
    count += 1 
