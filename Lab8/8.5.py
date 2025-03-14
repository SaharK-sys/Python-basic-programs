# Update first set with items that don’t exist in the second set
set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}
item_to_add = set2 - (set1&set2)
set1.update(item_to_add)
print(set1)

