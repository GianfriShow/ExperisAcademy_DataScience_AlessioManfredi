# decorators for checking input types in the constructor method (REMEMBER to skip the first argument 'self' and use raise instead of return for errors)

def init_check_string_inputs(function):
    def wrapper(*args, **kwargs):
        for arg in args[1:]:
            if not isinstance(arg, str):
                raise Exception(f"Error: {arg} is not a string.")
        for _, value in kwargs.items():
            if not isinstance(value, str):
                raise Exception(f"Error: {value} is not a string.")
        return function(*args, **kwargs)
    return wrapper

def init_check_numeric_inputs(function):
    def wrapper(*args, **kwargs):
        for arg in args[1:]:
            if not (isinstance(arg, int) or isinstance(arg, float)):
                raise Exception(f"Error: {arg} is not numeric.")
        for _, value in kwargs.items():
            if not (isinstance(value, int) or isinstance(value, float)):
                raise Exception(f"Error: {value} is not numeric.")
        return function(*args, **kwargs)
    return wrapper



# 1
# create a class "Point" with 2 attributes ('x' and 'y') representing its coordinates in a plane
# include a method "move" that takes movement inputs for x and y and modifies the old values BY those amounts
# finally, a method "distance_from_origin" that returns the distance between the point and the origin (0,0)

import math

class Point:

    @init_check_numeric_inputs
    def __init__(self, x, y):
        self.x = x
        self.y = y

    @init_check_numeric_inputs
    def move(self, delta_x, delta_y):
        self.x += delta_x
        self.y += delta_y

    def distance_from_origin(self):
        distance = math.sqrt(self.x**2 + self.y**2)
        return distance

point1 = Point(-4.5,7.2)
print(point1.x, point1.y)
print(point1.distance_from_origin())
point1.move(0.9,-3.12)
print(point1.x, point1.y)
print(point1.distance_from_origin())
print(type(point1))
print(isinstance(point1, Point))



# 2
# create a class "Book" with 3 attributes: 'title', 'author', and 'pages'
# write a method 'description' returning a string f"The book {title} was written by {author} and it's {pages} pages long"

def init_check_book_inputs(function):
    def wrapper(*args, **kwargs):
        if not (isinstance(args[3],int) and args[3]>0):
            raise Exception(f"Error: {args[3]} must be a positive integer")
        if not (isinstance(args[1],str) and isinstance(args[2],str)):
            raise Exception(f"Error: {args[1]} and {args[2]} must both be strings")
        return function(*args, **kwargs)
    return wrapper

class Book:

    text = ""

    @init_check_book_inputs
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    def description(self):
        print(f"The book '{self.title}' was written by '{self.author}' and it's {self.pages} pages long")

    @init_check_string_inputs
    def modify_text(self, text):
        self.text = text


book1 = Book('test_book','test_author',157)
book1.description()



# 3
# create a class Library that lets the user create a book and print it
# additionally, let the user create multiple books if they want

def init_check_book_class(function):
    def wrapper(*args, **kwargs):
        if not isinstance(args[1], Book):
            raise Exception(f"Error: '{args[1]}' must be an object of the class 'Book'")
        return function(*args, **kwargs)
    return wrapper

import os

class Library:
    
    @init_check_string_inputs
    def __init__(self, name):
        self.name = name
        self.book_count = 0
        try:
            os.mkdir(os.path.join('11_09',name))
        except:
            pass

    @init_check_book_class
    def add_book(self, book):
        with open(os.path.join('11_09',self.name, book.title), 'w') as temp_book:
            temp_book.write(f"""{book.title} ({book.pages} pages)\n\nWritten by "{book.author}"\n\n\n\n{book.text}""")
        self.book_count += 1
    
book1.modify_text("This is a test to check that everything works correctly.\nBye bye!")
my_library = Library("first_library")
my_library.add_book(book1)
print(my_library.book_count)



# 4
# create a class Restaurant with these requirements:
# - constructor can accept 2 parameters: name of restaurant and type of cuisine offered
# - attribute 'open' telling if the restaurant is open or not, False by default
# - a 'menu' dictionary with all dishes and corresponding prices
#
# class methods:
# - describe_restaurant() printing a sentence with info about name and cuisine
# - open_status() printing whether the restaurant is open
# - open_restaurant() opening the restaurant and printing that it is now open
# - close_restaurant() doing the opposite of open_restaurant()
# - add_to_menu() adding a dish to the menu
# - remove_from_menu() removing a dish from the menu
# - print_menu() printing the menu
#
# finally, create a test object and check that all methods work

class Restaurant:
    @init_check_string_inputs
    def __init__(self, name, cuisine):
        self.name = name
        self.cuisine = cuisine
        self.open = False
        self.menu = {}
    def describe_restaurant(self):
        print(f"The restaurant's name is '{self.name}', offering {self.cuisine} food")
    def open_status(self):
        print(f"The restaurant is {"open" if self.open else "closed"}")
    def open_restaurant(self):
        self.open = True
        print(f"The restaurant is now open")
    def close_restaurant(self):
        self.open = False
        print(f"The restaurant is now closed")
    @init_check_string_inputs
    def add_to_menu(self, dish, price):
        self.menu[dish] = price
    @init_check_string_inputs
    def remove_from_menu(self, dish):
        del self.menu[dish]
    def print_menu(self):
        for dish,price in self.menu.items():
            print(f"{dish}:    {price}")

restaurant1 = Restaurant('test_restaurant','test_cuisine')
print(type(restaurant1))
print(restaurant1.name, restaurant1.cuisine,restaurant1.open,restaurant1.menu)
restaurant1.describe_restaurant()
restaurant1.open_status()
restaurant1.open_restaurant()
restaurant1.open_status()
restaurant1.close_restaurant()
restaurant1.open_status()
restaurant1.add_to_menu('dish 1','25 dollars')
restaurant1.add_to_menu('dish 2','30 dollars')
restaurant1.print_menu()
restaurant1.remove_from_menu('dish 1')
restaurant1.print_menu()



# 5
# create a management system for a factory selling several products
# create at least 2 classes for products such as Clothing or Electronics, with specific attributes such as material or warranty respectively
# these classes should also have the attributes: name of product, production costs, selling price
# furthermore, write a method calculate_profit() that returns the difference between selling price and production costs
# create also a class for factories, with attribute 'inventory' (dictionary keeping track of products and number in stock), and methods:
# add_product() that adds a product to inventory, sell_product() that sells a certain number of units of a product and modifies inventory accordingly
# and prints the profits from this sale, return_product() increasing the units in stock for a given product by an amount
# and modifying inventory accordingly

class Clothing:
    def __init__(self, name, material, production_cost, selling_price):
        self.name = name
        self.material = material
        self.production_cost = production_cost
        self.selling_price = selling_price
    def calculate_profit(self):
        return self.selling_price-self.production_cost
class Electronics:
    def __init__(self, name, warranty, production_cost, selling_price):
        self.name = name
        self.warranty = warranty
        self.production_cost = production_cost
        self.selling_price = selling_price
    def calculate_profit(self):
        return self.selling_price-self.production_cost
class Factory:
    def __init__(self, inventory = {}):
        self.inventory = inventory
    def add_product(self, product, units):
        self.inventory[product.name] = units if product not in self.inventory else self.inventory[product.name] + units
    def sell_product(self, product, units):
        if units<=self.inventory[product.name]:
            self.inventory[product.name] -= units
            profits = product.calculate_profit()*units
            if not profits<0:
                profits = '+'+str(profits)
            print(f"Result from this sale:    {profits}")
        else:
            print("Error: not enough units in stock")
    def return_product(self, product, units):
        self.inventory[product.name] += units

dress1 = Clothing('t-shirt','cotton',5,15)
print(dress1.name,dress1.material,dress1.production_cost,dress1.selling_price,dress1.calculate_profit())
phone1 = Electronics('my_phone','5 years',1000,699)
print(phone1.name,phone1.warranty,phone1.production_cost,phone1.selling_price,phone1.calculate_profit())
my_factory = Factory()
print(my_factory.inventory)
my_factory.add_product(dress1,143)
print(my_factory.inventory)
my_factory.add_product(phone1,58)
print(my_factory.inventory)
my_factory.sell_product(dress1,32)
my_factory.sell_product(phone1,89)
my_factory.sell_product(phone1,12)
print(my_factory.inventory)
my_factory.return_product(dress1,6)
my_factory.return_product(phone1,3)
print(my_factory.inventory)

# EXTRA: create a superclass Product that takes the attributes 'name', 'production_cost', 'selling_price' and the method 'calculate_profit()'
# instead of the subclasses (clothing,etc.): the latter maintain their specific attribute(s) only and inherit the rest from the superclass Product

class Product:
    def __init__(self, name, production_cost, selling_price):
        self.name = name
        self.production_cost = production_cost
        self.selling_price = selling_price
    def calculate_profit(self):
        return self.selling_price-self.production_cost
class Clothing(Product):
    def __init__(self, name, material, production_cost, selling_price):
        Product.__init__(self, name, production_cost, selling_price)
        self.material = material
class Electronics(Product):
    def __init__(self, name, warranty, production_cost, selling_price):
        Product.__init__(self, name, production_cost, selling_price)
        self.warranty = warranty
class Factory:
    def __init__(self, inventory = {}):
        self.inventory = inventory
    def add_product(self, product, units):
        self.inventory[product.name] = units if product not in self.inventory else self.inventory[product.name] + units
    def sell_product(self, product, units):
        if units<=self.inventory[product.name]:
            self.inventory[product.name] -= units
            profits = product.calculate_profit()*units
            if not profits<0:
                profits = '+'+str(profits)
            print(f"Result from this sale:    {profits}")
        else:
            print("Error: not enough units in stock")
    def return_product(self, product, units):
        self.inventory[product.name] += units

dress1 = Clothing('t-shirt','cotton',5,15)

print(type(dress1), dress1.__class__)  # show the direct class (lowest in the hierarchy)
print(isinstance(dress1, (Clothing)))  # check if an object is an instance of a given class
print(isinstance(dress1, (Product)))  # same thing but we can also check for superclasses
print(issubclass(Clothing, Product))  # check if first class is a subclass of the second class
print(dress1.__class__.__mro__)  # show the complete inheritance hierarchy, including all superclasses (from lowest to highest, most specific to most general)