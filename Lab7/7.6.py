# program to convert a tuple to a string
# without separator
tuple1 = (1,2,3,4,5)
string1 = ' '.join(map(str,tuple1))
print(tuple1)
print(string1)
# with separator
string2 = ', '.join(map(str,tuple1))
print(string2)
