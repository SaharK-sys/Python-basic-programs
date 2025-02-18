# to read number and print its square if it is even and cube if it's odd
num = int(input("Enter a number"))
square = num ** 2
cube =  num ** 3
if(num%2 == 0):
    print("Square is:")
    print(square)
else:
    print("Cube is:")
    print(cube)
