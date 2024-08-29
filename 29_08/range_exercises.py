# 1
# ask the user for a number
# the program will count down from that number to zero, printing the number each time
# at the end, ask if the user wants to repeat the whole thing

import time

def countdown():

    top = int(input("Please choose a starting integer:\n"))
    sequence = []

    if top > 0:
        sequence = range(top,-1,-1)
    elif top < 0:
        sequence = range(top,1,1)
    else:
        print("Error: cannot choose 0 as starting number")
        countdown()
    
    for num in sequence:
        print(num)
        time.sleep(1)
    
    restart = int(input("Time's up!\nWould you like to go again?\n    1) No\n    2) Yes\n"))
    restart -= 1
    
    if restart:
        countdown()

countdown()


# 2
# ask for a number
# check if it's prime or not: if so, save it and print that it's a prime number, otherwise print that it's not
# the program ends when it has collected 5 prime numbers (does not specify they need to be different)

def check_prime(candidate):
    seq = range(2,(candidate//2)+1)
    prime = True
    for i in seq:
        if (candidate%i) == 0:
            prime = False
            break
    return prime

def prime_collection():
    collection = []
    while len(collection) < 5:
        number = input("Type a number:\n")
        try:
            convert = int(number)
        except:
            print("Error: not an integer")
            continue
        if convert <= 1:
            print("Error: integer must be greater than 1")
            continue
        if check_prime(convert):
            collection.append(convert)
            print("That number is prime")
        else:
            print("That number is NOT prime")

prime_collection()