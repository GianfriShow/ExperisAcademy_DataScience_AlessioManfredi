# 1

import random
def feeling_lucky():
    if int(input("Guess a number from 1 to 2: ")) == random.randint(1,2):
        if int(input("Alright, first level passed, now try again but from 1 to 4: ")) == random.randint(1,4):
            if int(input("Good, now for the final level, try from 1 to 10: ")) == random.randint(1,10):
                print("Wow, you actually did it, congrats!")
            else:
                print("Damn, losing at the final boss, what a shame.")
        else:
            print("You're not worthy, go back to the start.")
    else:
        print("Lost to tutorial lol, don't even bother trying again.")

feeling_lucky()


# 2

def string_manager():
    main_string = input("Welcome to string manager, choose your temporary string:\n")
    choice = int(input("Great, now choose what you want to do with your string (type number):\n    1) Add\n    2) Replace\n    3) Delete\n"))
    if choice == 1:
        main_string += input("Type exactly what you would like to add to your string:\n")
        print(f"The final string is: {main_string}")
    elif choice == 2:
        main_string = input("Alright, let's change things around. Choose your new string:\n")
        print(f"The final string is: {main_string}")
    else:
        main_string = ""
        print(f"I see, you're the destructive type... The final string is... wait, there is no final string, what did you do!?")

string_manager()


# 3

names = []
passwords = []
ids = []
index = 0
def login_signup():
    global index
    name = input("Type your username:\n")
    password = input("Type your password:\n")
    if name not in names:
        names.append(name)
        passwords.append(password)
        ids.append(index)
        index += 1
    else:
        temp_index = names.index(name)
        if password != passwords[temp_index]:
            print("Password is wrong")
            login_signup()
        choice = int(input("Welcome, what would you like to do with your account? (type number)\n    1) Modify credentials\n    2) Delete account\n"))
        if choice == 1:
            new_name = input("Type your new username:\n")
            while new_name in names:
                print("That username is already taken")
                new_name = input("Type a UNIQUE new username:\n")
            new_password = input("Type your new password:\n")
            names[temp_index] = new_name
            passwords[temp_index] = new_password
        else:
            names.remove(names[temp_index])
            passwords.remove(passwords[temp_index])
            ids.remove(ids[temp_index])
            index -= 1
            print("You have succesfully removed your account")
            
login_signup()