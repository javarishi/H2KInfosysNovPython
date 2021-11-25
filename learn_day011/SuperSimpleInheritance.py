class Simple:
    def __init__(self):
        print("Simple Parent Class")


class SuperSimple(Simple):
    def __init__(self):
        #super(SuperSimple, self).__init__()
        super().__init__() # this statement is exactly same as above
        print("SuperSimple Child Class")

superSimple = SuperSimple()