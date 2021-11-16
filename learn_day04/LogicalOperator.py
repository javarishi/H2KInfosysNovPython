# and or not
# between boolean results
first = 100
second = 10
third = 2000

c1 = first > second
c2 = first > third
print("first > second  ", c1)
print("first > third  ", c2)

# and
print(c1 and c2)

# and truth table
'''
R = S1 and S2
S1  S2  R
T   T   T
T   F   F
F   T   F
F   F   F

S1 and S2 and S3 and S4 and S5 and S6
'''

# or truth table
'''
R = S1 or S2
S1  S2  R
T   T   T
T   F   T
F   T   T
F   F   F
S1 or S2 or S3 or S4 
'''

print("not True :: " , not True)
print("not False :: " , not False)

