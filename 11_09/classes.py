# classes are fundamental for OOP programming
# it is standard practice to use lowercase names for variables but an uppercase first letter for classes
# classes are a non-basic type, defined by the programmer

# classes are structures containing a set of data (attributes) and behaviours (methods) specific to objects of that type
# an object is an INSTANCE of a class, inheriting its attributes and methods

# attributes are variables associated to a given class, representing the properties of an object of that class
# methods are functions associated to a given class, representing the behaviours of an object of that class

class Car:

    wheel_number = 4  # attribute of the class

    def __init__(self, brand, model):  # constructor method
        self.brand = brand  # instance attribute
        self.model = model  # instance attribute
    
    def print_info(self):  # instance method
        print(f"The car is a {self.brand} {self.model}")

car1 = Car("Fiat", "500")
car2 = Car("BMW", "X3")
    
car1.print_info()
car2.print_info()