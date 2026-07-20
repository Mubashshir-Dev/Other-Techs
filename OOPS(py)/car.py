import random
class Car:
    color="white"
    model="nano"
    def no_plate():
        return random.choice(['Hr','De','Up','Jk'])+str(random.randrange(100000,1000000))
    num=no_plate()

my_car = Car()
my_car.color= "yellow"
my_car.model= "lambo"
print(my_car.model)
print(my_car.color)
print(my_car.num)