# to accept two strings from the user and display the common words
string1 = input("Enter first string")
string2 = input("Enter second string")
set1 = set(string1.split())
set2 = set(string2.split())
set3 = set1.intersection(set2)
print(set3)


      


