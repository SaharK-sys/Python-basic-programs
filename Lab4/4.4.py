# to capitalize the first and last character of each word in a string.
string = input("Enter a string")
words = string.split()
result = []
for word in words:
    word = word[0].upper() + word[1:-1] + word[-1].upper()
    result.append(word)
print(' '.join(result))


      


