# to add 'ing' at end of given string (length should be at least 3).
# If given string already ends with 'ing' then add 'ly' instead.
# If string length of given string is less than 3, leave it unchanged.
string = input()
if len(string)<3:
    print(string)
elif string[-3:]=="ing":
    string2 = string +  "ly"
    print(string2)
else:
    string2= string + "ing"
    print(string2)
    


