sampleSet = {'A',4, 'B', 1, 15, 45.55}
setB = {'A', 'Z', 'AZ'}
print(sampleSet)
# Add Element: sampleSet.add("mango")
sampleSet.add("mango")
print(sampleSet)
sampleSet.add("mango")
print(sampleSet)

# Iterate: for eachItem in sampleSet:


# Element Exists? : if "apple" in sampleSet:


# Update(setB)
sampleSet.update(setB)
print(sampleSet)

# Check Length: len(sampleSet)


# Remove Element: sampleSet.remove("banana")

# Discard (No Error) : sampleSet.discard("apple")
sampleSet.discard("banana")

# Clear Set: sampleSet.clear()

print(type(sampleSet))
