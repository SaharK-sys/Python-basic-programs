#6.5countno.of strings(stringlength is 2/more&first&last character are same)
string = ['mum', ' yummy', 'tummy', 'gum', '5555', '6']
count = 0
for term in string:
    if len(term)>=2 and term[0]==term[-1]:
        count += 1
print("list is ",string)
print("count of strings with first& last character same is",count)

