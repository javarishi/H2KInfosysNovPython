first = 20
second = 18
third = 15

'''
if condition (Boolean expr):
    Block of code which executes when condition is true
else:
    Block of code which executes when condition is false
'''

result = " {} is greater than {} "

if first > second :
    print(result.format(first, second))
elif first > third:
    print(result.format(first, third))
else:
    print(result.format(third, first ))

'''
Variables are not equal 
1. first Variable - compare it with both second and third
2. both true - first is biggest number
3. if false - first is not biggest - second > third
4. if true biggest second
5. if false biggest is third

H.W - Any two or all Variables may be equal  
'''
first = 20
second = 20
third = 20

result = "Biggest number is {} "

if (first > second) and (first > third):
    print(result.format(first), " First ")
elif second > third:
    print(result.format(second), " Second ")
else:
    print(result.format(third), " Third ")

