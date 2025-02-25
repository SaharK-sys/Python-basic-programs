# to accept a string and count the frequency of each vowel.
string = input("Enter a string")
n = 0

for char in string:
    if (char == 'a' or char == 'e' or char == 'i' or char == 'o' or char == 'u'
or char == 'A' or char == 'E' or char == 'I' or char == 'O' or char == 'U'):
        n +=1
print("frequency of vowels in given string is: ",n)

    
