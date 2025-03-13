# to count the no. of characters (character frequency) in a string.

string = "summer is summering"
for char in string:
    print(f"{char}: {string.count(char)}")
