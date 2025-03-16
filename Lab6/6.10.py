# to find list of words that are longer than n from a given list of words.  
List = ['towel','cup','umbrella','pigeon','parrot','tin','at']
longList = [ ]
n = 5
for word in List:
    if len(word)>n:
        longList.append(word)
print(List)
print(longList)

