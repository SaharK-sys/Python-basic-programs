#6.6countno.of strings(stringlength is 2/more&first&last character are same)
SampleList = [(2,5), (1,2), (4,4), (2,3), (2,1)]
SortedList = sorted(SampleList , key = lambda tuple : tuple[-1])
print("list is ",SampleList)
print("Expected result after sorting is: ",SortedList)

