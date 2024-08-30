# take as input a word and add it to a list, ask if the user wants to repeat this by adding another word, then print all elements in the list at the end

def print_list():

    # preparation and first input
    sequence = []
    word = input("Please type a string to add to your list:    ")
    keep_going = True
    sequence.append(word)
    
    # core loop
    while keep_going:
        word = input("Type another string if you want to keep going, otherwise press 'Enter' if you want to print your current list:    ")
        if word == '':
            keep_going = False
        else:
            sequence.append(word)

    # print final output
    print("Here's your list:\n")
    for element in sequence:
        print(element)

print_list()