# 1
# create a class "Point" with 2 attributes ('x' and 'y') representing its coordinates in a plane
# include a method "move" that takes movement inputs for x and y and modifies the old values BY those amounts
# finally, a method "distance_from_origin" that returns the distance between the point and the origin (0,0)

import math

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

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

class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages
    def description(self):
        print(f"The book '{self.title}' was written by '{self.author}' and it's {self.pages} pages long")

book1 = Book('test_book','test_author','157')
book1.description()