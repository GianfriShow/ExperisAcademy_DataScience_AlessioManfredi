# 1
# ask for the user's age: if less than 18, print that they can't watch it, otherwise print the opposite

if int(input("Please insert your age:\n")) < 18:
    print("Sorry, you cannot access this movie")
else:
    print("You can access this movie")


# 2
# ask the user to insert 2 numbers and choose an operation among addition, subtraction, multiplication, and division
# then, compute and print the result
# if the user tries to divide by zero, print the corresponding error
# if they choose a different operation, print the corresponding error

first_number = float(input("Please type the first number:\n"))
second_number = float(input("Please type the second number:\n"))
choice = int(input("Please choose the operation to compute:\n    1) Addition\n    2) Subtraction\n    3) Multiplication\n    4) Division\n"))
if choice == 1:
    print(first_number + second_number)
elif choice == 2:
    print(first_number - second_number)
elif choice == 3:
    print(first_number * second_number)
elif choice == 4:
    if second_number == 0:
        print("Error: Division by Zero")
    else:
        print(first_number / second_number)
else:
    print("Error: Not a Valid Operation")