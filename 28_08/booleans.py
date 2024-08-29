# the boolean type (bool) is binary: it can be either "True" or "False"
# True and False are CASE SENSITIVE

# to evaluate boolean expressions, Python supports logical operators
# the main logical operators are: "and", "or", "not"
x = 5
y = 10
z = 7
print(x < y and y > z)
print(x < y or z > y)
print(not(x < y))

# relational operators compare two values and return a boolean
x = 5
y = 10
print(x == y)
print(x != y)
print(x < y)