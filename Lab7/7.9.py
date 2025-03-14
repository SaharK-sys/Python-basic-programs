# program to find repeated items of a tuple
tuple1 = (1,2,3,4,5,2,2,5,5,1,1,1,1,8,10)
set1 = set(item for item in tuple1 if(tuple1.count(item)>1))
print(set1)

