# swap 2 no.s without using third variable
print("Enter 2 numbers")
a = int(input())
b = int(input())
a = a + b
b = a - b
a = a - b
print("No.s after swapping")
print(a)
print(b)

