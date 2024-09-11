# the inheritance property allows a class (called subclass) to inherit attributes and methods from another class (called superclass)

# super() is a function used to recall the constructor of the superclass, allowing the subclass to extend or modify the superclass's behaviour
# super() is also used to access methods from the superclass that might have been overwritten in the subclass

# the subclass can overwrite methods from the superclass to make them behave differently for that specific subclass

# multiple inheritance: a subclass can inherit from several superclasses

class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
    def show_info(self):
        print(f'The brand is {self.brand} and the model is {self.model}')
class SpecialPerks:
    def __init__(self, perks):
        self.perks = perks
    def show_perks(self):
        print(f'Special perks: {', '.join(self.perks)}')

class SportsVehicle(Vehicle, SpecialPerks):  # create subclass inheriting from the previously-defined superclasses
    def __init__(self, brand, model, perks, horsepower):
        Vehicle.__init__(self, brand, model)  # alternative to using super() for the inheritance
        SpecialPerks.__init__(self, perks)
        self.horsepower = horsepower
    def show_info(self):
        super().show_info()  # call the method of the first superclass
        print(f'Power: {self.horsepower} HP')
        self.show_perks()  # we can call methods from multiple superclasses

sports_vehicle = SportsVehicle("Ferrari","F8",["ABS","Traction control","Side airbags"],720)
sports_vehicle.show_info()