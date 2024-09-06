# 1
# write a function called triangle_area() that takes as input base and height of a triangle and returns its area
# do the same with a square and a rectangle and make this repeatable, saving all results in a list

def area_game():

    def triangle_area(base, height):
        area = base*height/2
        return area

    def square_area(side):
        area = side**2
        return area

    def rectangle_area(base, height):
        area = base*height
        return area

    results = []
    continue_game = True

    while continue_game:
        choice = int(input("What would you like to find the area of? (type number)\n    1) Triangle\n    2) Square\n    3) Rectangle\n    4) Print results and exit\n"))
        if choice==4:
            print(results)
            continue_game = False
        elif choice==1:
            argument1 = float(input("Type the base of the triangle:\n"))
            argument2 = float(input("Type the height of the triangle:\n"))
            results.append(triangle_area(argument1,argument2))
        elif choice==2:
            argument1 = float(input("Type the side of the square:\n"))
            results.append(square_area(argument1))
        else:
            argument1 = float(input("Type the base of the rectangle:\n"))
            argument2 = float(input("Type the height of the rectangle:\n"))
            results.append(rectangle_area(argument1,argument2))

area_game()


# 2
# ask for the user name and a number, then apply a decorator to check if the number is prime_or_not: if it is, save it in a list and ask for another number,
# if it isn't, DON'T save the number but print its lowest factor, and ask for another number
# the user can stop the cycle if they choose to do so, and this will return the user's name with the list of all prime numbers found

def prime_or_not(candidate_generator):
    def wrapper(*args, **kwargs):
        candidate = candidate_generator(*args, **kwargs)
        sequence = range(2,(candidate//2)+1)
        prime = True
        lowest_factor = 1
        for i in sequence:
            if (candidate%i) == 0:
                prime = False
                lowest_factor = i
                break
        return candidate, prime, lowest_factor
    return wrapper

@prime_or_not
def ask_number():
    number = int(input("Type an integer greater than 1:\n"))
    return number

def prime_game():
    username = input("Please type your username:\n")
    continue_game = True
    prime_numbers = []
    while continue_game:
        candidate, prime, lowest_factor = ask_number()
        prime_numbers.append(candidate) if prime else print("That number is NOT prime.")
        choice = int(input("Would you like to continue? (type number)\n    1) No, print results and exit\n    2) Yes\n"))-1
        if choice:
            continue
        print(f"{username}'s list:\n{prime_numbers}")
        break

prime_game()


# 3
# write a function called compress_string that takes as input a string and returns its compressed version
# the compression should work this way: for each group of consecutive identical characters, return the character followed by the number of instances
# for example, 'aaabbc' would be compressed into 'a3b2c1'
# if the final string has the same original length, return the original string instead

def compress_string(function):
    def wrapper(*args, **kwargs):
        long = function(*args, **kwargs)

        temp_char = long[0]
        counter = 1
        temp_index = 0

        final_string = ""

        while temp_index < (len(long)-1):
            if long[temp_index+1]==temp_char:
                counter += 1
                temp_index += 1
            else:
                final_string += temp_char+str(counter)
                temp_index +=1
                temp_char = long[temp_index]
                counter = 1
        
        final_string += temp_char+str(counter)

        return final_string if len(final_string)<len(long) else long
    return wrapper

@compress_string
def ask_string():
    temp_string = input("Type your string:\n")
    return temp_string

def compress_game():
    print(ask_string())
            
compress_game()