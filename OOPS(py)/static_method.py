class Person:
    __counter = 1
    def __init__(self,name,cool):
        self.name=name
        self.cool=cool
        self.sno=self.get_counter()
        Person.__counter+=1
    @staticmethod
    def get_counter():
        return Person.__counter
    
    @staticmethod
    def set_counter(new):
        if(type(new) == int):
            Person.__counter=new
        else:
            print("worng")

obj1 = Person('Mubashshir',True)
print(Person.get_counter())
obj2 = Person('Om',False)
print(Person.get_counter())
Person.set_counter(4)
print(Person.get_counter())