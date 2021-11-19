# name = User --> named parameter, default parameter, keyed argument
def say_hello(age, address, name="User"):
    print("Hello ", name, age, address)


# if you want to pass null value use None
say_hello(age=37, address="Spring Hill Pkey" ,name="Rishi")
say_hello(address="Spring Hill Pkey", name="Ram", age="45")
say_hello(age=30,name="Laxman", address="Dashrath Lane")
say_hello("",'something', None)

