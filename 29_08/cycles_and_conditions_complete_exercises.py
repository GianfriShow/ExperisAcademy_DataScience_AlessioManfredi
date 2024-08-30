# 1
# input a number and print if it's even or odd

def even_or_odd():
    number = int(input("Type an integer:\n"))
    if number%2==0:
        print("Even")
    else:
        print("Odd")

even_or_odd()


# 2
# take as input a positive integer n and print all numbers from n to 0 (included), decreasing by 1 each time
# allow infinite replayability

def go_down():
    n = int(input("Type a positive integer:\n"))
    for i in range(n,-1,-1):
        print(i)
    if (int(input("Want to go again?\n    1) No\n    2) Yes\n"))-1):
        go_down()

go_down()


# 3
# ask as input a list of numbers and print the square of each of them

def squares_list():
    temp_seq = input("Type a list of numbers separated ONLY by a comma:\n")
    seq = temp_seq.split(",")
    seq = [float(num) for num in seq]
    squared = [num**2 for num in seq]
    print(squared)

squares_list()


# 4
# take as input a list of integers and:
# - use a for loop to find the maximum number
# - use a while loop to count the list's length
# - use an if condition to print 'empty list' if it's empty, otherwise print the maximum number and the length of the list

import copy

def find_maximum_and_length_of_list():

    temp_seq = input("Type a list of integers separated only by a comma:\n")

    try:  # error handling if empty
        temp_seq[0]
    except:
        print("The list is empty")
        return
    
    seq = temp_seq.split(",")

    try:  # error handling for wrong types
        seq = [int(num) for num in seq]
    except:
        print("The list must contain INTEGERS only, separated by a SINGLE comma (,)")
        return
    
    seq_copy = copy.deepcopy(seq)
    max = []
    length = 0
    go = True
    
    while go:  # count
        try:
            seq_copy.pop()
            length += 1
        except:
            go = False

    for i in seq:  # find max
        if len(max) and i>max[0]:
            max[0]=i
        else:
            max.append(i)

    print(f"The list contains {length} integers, with the maximum being {max[0]}")

find_maximum_and_length_of_list()