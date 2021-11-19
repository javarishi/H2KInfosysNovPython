from setuptools.command.easy_install import easy_install

sample = [1,2,3,4,5,6,7,8,9,10]

biggest = sample[0]
for eachValue in sample:
    if biggest < eachValue:
        biggest = eachValue
print("Biggest ", biggest)


'''
for eachValue in Collection:
    block code execute for each value in given collection

range function
range(N) -  generating values from 0 to (N-1)
range(S, E) - generating values from S to (E-1)
range(Start, End, Step) - Start to End with the step (increment)
'''
total = 0
for eachValue in range(21, 0, -1):
    total = total + eachValue
    print("Value from Sample Array ", eachValue)
print("Total ", total)

hello = "Hello World"
end = len(hello)
final_str = ""
for eachIndex in range(end, 0, -1):
    final_str = final_str + hello[eachIndex-1]
    print(final_str)

# H.W Find Biggest number out of an Array with the help of Loop
