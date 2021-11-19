'''
while (condition) :
    block of code executed till condition is true
    condition modifier
'''

# Problem Statement - Add 1 to 10
i = 1
total = 0
while i <= 10:
    total = total + i
    print("Value of i ", i)
    i += 1

print("Sum of 1 to 10 is ", total)