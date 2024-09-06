# 1
# Sample a random number between 1 and 100 (included). The user must guess what it is, and after each try the program reports if the real value is
# higher or lower than the guess. The game ends when the user guesses correctly or when they decide to end the game.

import random
def guessing_game():
    truth = random.randint(1, 100)
    guess = input("Guess an integer from 1 to 100 (included):\n")
    continue_game = True
    while continue_game:
        wrong_input = True
        while wrong_input:
            try:
                assert guess.isdigit()
                guess = int(guess)
                assert guess > 0 and guess < 101
                wrong_input = False
            except:
                guess = input("You must guess a positive integer between 1 and 100, these bounds being included:\n")
        if guess < truth:
            print("Real number is higher.")
        elif guess > truth:
            print("Real number is lower.")
        else:
            continue_asking = True
            choice = input("Congratulations, you found it! Would you like to play again? (type number)\n    1) No\n    2) Yes\n")
            while continue_asking:
                try:
                    choice = int(choice)-1
                    assert choice == 0 or choice == 1
                    continue_asking = False
                except:
                    choice = input("Wrong input. Please type the NUMBER corresponding to your choice:\n    1) No\n    2) Yes\n")
            if choice:
                guessing_game()
            break
        continue_asking = True
        choice = input("Would you like to try again? (type number)\n    1) No\n    2) Yes\n")
        while continue_asking:
            try:
                choice = int(choice)-1
                assert choice == 0 or choice == 1
                continue_asking = False
            except:
                choice = input("Wrong input. Please type the NUMBER corresponding to your choice:\n    1) No\n    2) Yes\n")
        if choice:
            guess = input("Guess an integer from 1 to 100 (included):\n")
            continue
        continue_game = False
                
guessing_game()


# 2
# ask the user for a number N, then print Fibonacci's sequence until the first output greater than N (excluded)
# NO ERROR HANDLING FROM NOW ON BECAUSE IT TAKES UP TOO MUCH TIME AND I CAN NEVER FINISH EXERCISES BECAUSE OF IT

def fibonacci_bounded(bound):
    temp1, temp2 = 0, 1
    sequence = [temp1, temp2]
    while sequence[-1] < bound:
        temp1, temp2 = temp2, temp1+temp2
        sequence.append(temp2)
    if sequence[-1]>bound:
        sequence.pop()
    print(sequence)

fibonacci_bounded(1000)