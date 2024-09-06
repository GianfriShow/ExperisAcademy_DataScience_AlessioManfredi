# I don't use functions here because I was asked not to for the time being

correct_username = "admin"
correct_password = "12345"
username = input("Please insert your username:\n")
password = input("Please insert your password:\n")

if username != correct_username or password != correct_password:
    print("Username or password are wrong, please try again.")
else:
    choice = int(input("Login was successful, welcome. Please choose what you would like to do:\n    1) Modify username\n    2) Modify password\n    3) Add secret question\n"))
    if choice == 1:
        correct_username = input("Please type your new username:\n")
    elif choice == 2:
        correct_password = input("Please type your new password:\n")
    else:
        question_choice = int(input("Please choose your secret question:\n    1) What's your favourite colour?\n    2) What's your favourite animal?\n"))
        index = question_choice - 1
        global secret_question
        global secret_answer
        secret_question = ("What's your favourite colour?", "What's your favourite animal?")[index]
        secret_answer = input("Please type your secret answer:\n")