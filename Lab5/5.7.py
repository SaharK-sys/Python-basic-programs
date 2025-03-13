# to get a string made of first 2 and last 2 chars from a given string.
# If the string length is less than 2, return instead of the empty string
string = input("Enter string")
if len(string)<2:
    print(string)
else:
    string2 = string[0:2]+string[-2:]
    print(string2)
    

    


