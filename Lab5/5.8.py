# to get string from given string where all occurrences
# of its first char have been changed to '$', except the first char itself.
string = input("Enter string")
string2 = string[0] + string[1:].replace(string[0],'$')
print(string2)

    


