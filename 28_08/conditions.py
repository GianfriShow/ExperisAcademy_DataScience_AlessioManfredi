# "if" executes if a condition is True
number = 10
if number > 0:
    print("the number is positive")

# "if-else" gives a plan b to execute if the condition happens to be False
number = 10
if number > 0:
    print("the number is positive")
else:
    print("the number is 0 or negative")

# "if-elif-else" specifies other conditions after the main one, and 'else' comes at the end in case they all return False
number = 10
if number > 0:
    print("the number is positive")
    if number == 100:
        print("wow")
elif number < 0:
    print("the number is negative")
else:
    print("the number is zero")