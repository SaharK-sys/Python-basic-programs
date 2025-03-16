# takes two lists and returns True if they have at least one common member.
def common(List,Listt):
    for word in List:
        if word in Listt:
            return True
    return False
List = ['towel','cup','umbrella','pigeon','parrot','tin','at']
Listt = ['umbrella', 'tin', 'brass' , 'copper']
print(common(List,Listt))

