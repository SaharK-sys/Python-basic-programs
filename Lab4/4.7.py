# to display the smallest word from the string
string = input("Enter a string")
words = string.split()
smallest_word = words[0]
for word in words:
    if len(word)< len(smallest_word):
         smallest_word = word
print("smallest word is: ",smallest_word)

    
