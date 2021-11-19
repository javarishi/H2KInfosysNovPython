sample = [1,2,3,4,5, 'A', 34,1,3,2,4]

total = 0
# break statement - breaks the loop at current iteration
# skip iteration - continue
for eachValue in sample:
    if str(eachValue).isnumeric():
        total  = total + eachValue
    else:
        print("Wrong Value received ", eachValue)
        continue

print(" Total till wrong value ", total)