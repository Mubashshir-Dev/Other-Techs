class Self_Demo:
    def __init__(self):
        id(self)

obj1 = Self_Demo()
print(id(obj1))
obj2 = Self_Demo()
print(id(obj1))

#self is nothing but the address of object which calls the constructor method 