# tuples (tuple) are similar to lists, with the difference that they are IMMUTABLE
# they are enclosed in round brackets '()'
pixel = (3,4)
rgb_colour = (255,128,0)
information = ("Alice", 25, 'female')

# we can access a tuple's elements through indexing
pixel = (3,4)
print(pixel[0])
print(pixel[1])

# but we cannot modify it (immutability property), or we'll get an error
pixel = (3,4)
pixel[0] = 5  #this will raise a TypeError

# we can create in some cases a tuple without round brackets, known as 'tuple packing' or 'tuple unpacking'
pixel = 3,4  #tuple packing
x, y = pixel  #tuple unpacking
print(x,y)