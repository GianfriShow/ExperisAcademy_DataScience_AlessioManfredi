# numbers can mainly be integers (int) or floating-point (float)
x = 10 # integer
a = 3.14 # floating-point

# strings (str) are sequences of characters that can contain letters, numbers, special symbols, and empty spaces
# they can be enclosed in single/double quotes, or triple single/double quotes
name = 'Alessio'
greeting = """hello!"""

# we can index strings with "[]" (indexing starts from 0 in Python) and concatenate them with "+"
print(name[0], name[3])
message = name + ", " + greeting
print(message)

# strings have access to methods
s = "Hello, world!"
print(len(s)) # length of a string
print(s.upper()) # convert a string to uppercase
print(s.lower()) # convert a string to lowercase
print(s.split(',')) # split the string in sub-strings based on a divider
print(s.replace('world', 'universe')) # substitute the first argument of a string with the second