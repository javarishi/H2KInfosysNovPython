sampleList = ['A', 'B', 1, 15, True, 45.55]

print(sampleList)
print(sampleList[0])
print(sampleList[0:5]) # Sub List
# Add Element: sampleList.append("newItem")
sampleList.append("newItem")
sampleList.append("newItem")
print(sampleList)
# Add Indexed Element: sampleList.insert(1, "fruits")
sampleList.insert(1, "fruits")
print(sampleList)
# Allows Duplicates
# Remove Element: sampleList.remove("item")
sampleList.remove(15)
print(sampleList)
# Remove Indexed Element: sampleList.pop(1)
sampleList.pop(4)
print(sampleList)
# Using Delete function: del sampleList[0]
del sampleList[0]
print(sampleList)
# Check the Length: len(sampleList)
print(len(sampleList))

if 45.55 in sampleList:
    print("45.55 exists")

for eachValue in sampleList:
    print(eachValue)

list_to_sort = [1,23,45,67,12,44,78]
list_to_sort.sort()
print(list_to_sort)

# Reverse List : sampleList.reverse()
list_to_sort.reverse()
print(list_to_sort)

# Clear List: sampleList.clear()
sampleSet = set(sampleList)
print("Sample Set" , sampleSet)

sampleList.clear()
print(sampleList)