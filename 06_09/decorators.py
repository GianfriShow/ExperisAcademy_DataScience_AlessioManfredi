# decorators are functions that modify the behaviour of other functions without actually changing their code
def decorator(function_to_wrap):
    def wrapper():
        print("Before the execution of the function")
        function_to_wrap()
        print("After the execution of the function")
    return wrapper

@decorator
def greetings():
    print("Hello!")

greetings()


# *args and **kwargs are used to pass a variable number of arguments to a function
# they allow wrappers to accept any combination of positional (args) and keyword (kwargs) arguments
# args collects all extra positional arguments into a tuple, kwargs collects all extra keyword arguments into a dictionary
def decorator_with_arguments(function):
    def wrapper(*args, **kwargs):
        print("Before")
        result = function(*args, **kwargs)
        print("After")
        return result
    return wrapper

@decorator_with_arguments
def sum(a,b):
    return a+b

print(sum(3,4))


# Some concepts:
# - functions can be passed as arguments, returned by other functions or assigned to variables; this allows decorators to work
# - decorators often use nested functions
# - decorators return a new function replacing the original (wrapped) one, allowing us to modify its behaviour without touching the original code
# - *args and **kwargs guarantee that the decorator can handle functions of any type, with any number of parameters
# - the syntax '@decorator' is equivalent to writing 'function = decorator(function)


def logger(function):
    def wrapper(*args, **kwargs):
        print(f'Call to "{function.__name__}()" with arguments: {args} and {kwargs}')
        result = function(*args, **kwargs)
        print(f'Result of "{function.__name__}()": {result}')
        return result
    return wrapper

@logger
def multiply(a,b):
    return a*b

# call to the decorated function
multiply(3,4)


# example: how to calculate the running time of the wrapper
import time

def run_time(function):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = function(*args, **kwargs)
        end_time = time.time()
        print(f"Execution time: {end_time - start_time} seconds")
        return result
    return wrapper

@run_time
def slow_test():
    time.sleep(2)
    print("Function completed")

slow_test()