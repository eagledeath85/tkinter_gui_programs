#################### POSITIONAL ARGUMENTS *args ####################
def add(*args):
    return sum(args)


print(add(10, 10, 10))


#################### KEY WORDS ARGUMENTS **kwargs ####################
def calculate(n, **kwargs):
    print(kwargs)
    n += kwargs["add"]
    n *= kwargs["multiply"]
    print(n)

calculate(3, add=2, multiply=5)


#################### CREATING A CLASS USING KEY WORDS ARGUMENTS **kwargs ####################
class Car:
    def __init__(self, **kwargs):
        # By using the get() method, it will return None if the key doesn't exist
        self.make = kwargs.get("make")
        self.model = kwargs.get("model")
        self.colour = kwargs.get("colour")
        self.seats = kwargs.get("seats")


# Creating an instance of Car using all the keyword arguments
my_car_1 = Car(make="nissan", model="almeira", colour="champagne", seats=5)
print(my_car_1.model)
print(my_car_1.make)
print(my_car_1.colour)


# Creating an instance of Car without using all the keyword arguments
my_car_2 = Car(make="renault")
print(my_car_2.model)   # return None
print(my_car_2.seats)   # return None

