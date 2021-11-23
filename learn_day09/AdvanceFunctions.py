def greet():
    print("Welcome to Python advance functions")
    def greet_message():
        print("Another welcome message within a method")
    return greet_message

def calculator(operation, num):
    operator_method = None
    def addition():
        return num + num
    def square():
        return num * num
    def cube():
        return num * num * num

    if operation == 'add':
        operator_method = addition
    elif operation == 'square':
        operator_method = square
        print(id(square))
    else:
        operator_method = cube

    return operator_method


sqr = calculator('square', 15)
print(id(sqr))
print(15, sqr())
add = calculator('add', 15)
print(15, add())
cube = calculator('cube', 15)
print(15, cube())