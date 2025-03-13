# to get single string from two given strings,
# separated by a space and swap the first two characters of each string
string1 = input()
string2 = input()
def swap_2chars(string):
    return string[1] + string[0] + string[2:]

string3= swap_2chars(string1) + " " + swap_2chars(string2)
print(string3)


    


