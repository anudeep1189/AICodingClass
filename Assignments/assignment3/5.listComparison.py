# 5. Write a program that takes two lists and prints the common elements, elements unique to the first list, and elements unique to the second list.

list1 = [1, 2, 3, 4, 5, 6]
list2 = [4, 5, 6, 7, 8, 9]

set1 = set(list1)
set2 = set(list2)

commonElements = list(set1.intersection(set2))

uniqueElementsList1 = list(set1.difference(set2))

uniqueElementsList2 = list(set2.difference(set1))

print(f"Common elements: {commonElements}")
print(f"Elements unique to the first list: {uniqueElementsList1}")
print(f"Elements unique to the second list: {uniqueElementsList2}")