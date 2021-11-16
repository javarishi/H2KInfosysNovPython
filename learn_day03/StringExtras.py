hello = "Hello, This is H2K Python Training. Python is awesome"

print('H2K' in hello)
print('H2KInfosys' in hello)
hello = hello.replace('H2K', 'H2KInfosys')
print(hello)

example = 'PYTHON'
print("_".join(example))

print(''.join(reversed(example)))

str = "	Hello World   "

print(str)
print(str.strip())
print(hello.strip('H'))

# count
print(hello.count('H', 0, 5))
print(hello.count('is', 10))
print(hello.count('are'))

# find
print("**** FIND ****")
print(hello.find('H2K'))
index_first = hello.find('is', 10)
print("First is ", index_first)
index_second = hello.find("is", index_first + 1)
print("Second Index", index_second)
index_third = hello.find("is", index_second + 1)
print("Third Index", index_third)

print(hello.find('H', 0, 5))
print(hello.find('are')) # -1 is not found


name = "RISHI"
say_hello = "Hello, {}. Welcome to {} Training"
print(say_hello.format(name, 'Python'))
print(say_hello)

a = """Lorem ipsum dolor sit amet,
consectetur adipiscing elit,
sed do eiusmod tempor incididunt
ut labore et dolore magna aliqua."""

print(len(a))