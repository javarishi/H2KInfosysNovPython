message = "Hello"
def say_hello():
    global message
    message = "Hola!"
    print(message)

say_hello()
print(message)

