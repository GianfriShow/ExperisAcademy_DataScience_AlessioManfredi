# def my_sum(a=0, b):  # we cannot have a parameter without a default after one with a default
#     print(a+b)

def my_sum(a, b=0):  # this works instead
    print(a+b)

# therefore, all default parameters must be defined at the end of the parameter list

my_sum(3)

def sum(a):
    addend = 5
    result = a + addend

sum(6)
# print(result)  # this returns an error because 'result' was defined inside the function and not returned, so it remained in its local scope


def sum(a):
    addend = 5
    global result  # if we define a variable with 'global' in front of it, we will specify we want it in the global scope (out of the function)
    result = a + addend

sum(6)
print(result)  # now we can retrieve 'result' in the global scope


def sum(*args):  # with '*args' the function will unpack the arguments and we'll obtain a list of them
    print(args)

sum('hello','world','!')


def sum(**kwargs):  # with '**kwargs' the function will double unpack and we will get a dictionary from the list of arguments (each with assignment)
    print(kwargs)

sum(name='Mark', surname='Rober',address='test street',age='42')


my_list = [2,5,7,4,427,7,2342,6,578]
def check_even(candidate):
    return True if candidate%2 == 0 else False

even_nums = filter(check_even, my_list)  # return an iterator yielding those items of iterable for which function(item) is true; if function is None, return the items that are true
even_nums = list(even_nums)  # return the elements from the iterator that satisfied the function in the previous filter() argument
print(even_nums)  # in this case, we will get only the even numbers in the list


print(list(map(check_even, my_list)))  # map instead returns an iterator but with the output of the function, not the original elements that are True


# using other libraries/modules
import math
print(math.sqrt(30))

import math as m  # we can give an alias to imported modules
print(m.sqrt(47))

from math import sqrt as s  # or we can import a single method/function (and alias it too)
print(s(62))

from math import sqrt, pow  # or even import multiple methods at once

# additionally, we can import methods from a local module
from my_functions import my_sum,multiply
my_sum(5,3)
multiply(8,3)

# or the whole local module directly
import my_functions
my_functions.my_sum(6,84)
my_functions.multiply(753,23)


# pseudo-random numbers
import random

print(random.random())  # random floating number between 0 and 1
print(random.randint(5,90))  # random integer between bounds (both included)
print(random.randrange(3,13,2))  # random value from a range()
print(random.choice(['thomas','mark','robert','hannah']))  # random choice within a list of elements


# dates
import datetime

print(datetime.date(2024,9,10))  # print year, month, day in the proper datetime.date format
print(datetime.time(4,13,58))  # print hour, minute, second in the proper datetime.time format
print(datetime.datetime(2024,9,10,4,13,58))  # print year,month,day + hour,minute,second in the proper datetime.datetime format
print(datetime.datetime.now())  # print current date and time down to the microsecond


# error handling

# naive way
user_input = 'hello'
if user_input.isdecimal():
    print("Input is a number")
    user_input = float(user_input)
else:
    print("Input is not a number")

# proper way with TRY-EXCEPT
try:
    print(int(user_input))
except:
    print("Input is not a number")
    
# 'try' attempts the execution of its instructions; if it fails somewhere, it doesn't execute but runs the 'except' instructions instead

# we can specify different except statements based on the errors that might occur in the try statement
try:
    print(10/0)
except ZeroDivisionError as e:  # and we can even alias the error
    print(f'Error: {e}')



# opening files

# 'r' is for read, 'a' is for append, 'w' is for (over)write
with open("10_09/test.txt", "a") as my_file:  # when file doesn't exist yet, 'append' creates a new one, otherwise it just appends to the old one
    my_file.write("My first created file")

with open("10_09/test.txt", "w") as my_file:  # if the file already exists, 'write' will overwrite it (so BE CAREFUL)
    my_file.write("My first created file\nIt's a good day")

with open("10_09/test.txt", "r") as my_file:  # 'read' simply reads the content without modifying them
    whole_content = my_file.read()  # return the whole text file with .read()
    my_file.seek(0)  # after we read, we need to reset the pointer where Python is reading to the beginning (0) if we want to read again later
    lines = my_file.readlines()  # .readlines() returns a list of rows from the text (including the \n)
print(whole_content)
print(lines)
print([line.strip() for line in lines])  # we can .strip() each line in the list to remove the '\n' character