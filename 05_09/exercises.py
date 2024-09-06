# ask the user for a string and return all the vowels with their corresponding index
'''
def index_vowels():  # longer version
    seq = input("Please enter your string:\n").lower()
    vowel_list = []
    index_list = []
    counter = 0
    for character in seq:
        if character in 'aeiou':
            vowel_list.append(character)
            index_list.append(counter)
        counter += 1
    print(vowel_list, '\n', index_list, sep='')

index_vowels()

def index_vowels_2():  # shorter version
    seq = input("Please enter your string:\n").lower()
    vowel_list = [candidate for candidate in seq if candidate in 'aeiou']
    index_list = [index for index in range(len(seq)) if seq[index] in 'aeiou']
    print(vowel_list, '\n', index_list, sep='')

index_vowels_2()'''


# ask for a list of integers, then print a series of symbols, by taking the same symbol and repeating it as many times as the integer,
# as many times as the integers in the list

def symbol_madness(symbol = "-"):
    seq = input("Type a list of integers, separated only by a single comma:\n")
    try:
        seq = seq.split(',')
        seq = [abs(int(i)) for i in seq]
    except:
        print("List must contain integers only, separated by a SINGLE comma only. Try again.")
        symbol_madness()
    for number in seq:
        print(number*symbol)

symbol_madness(symbol='+')