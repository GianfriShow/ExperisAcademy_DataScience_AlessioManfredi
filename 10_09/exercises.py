# ask the user for a string and return a dictionary representing the frequency of each character inside the string

def check_string_input(function):
    def wrapper(*args, **kwargs):
        for i in args:
            if not isinstance(i, str):
                return f"Error: {i} is not a string."
        for _, value in kwargs.items():
            if not isinstance(value, str):
                return f"Error: {value} is not a string."
        return function(*args, **kwargs)
    return wrapper

@check_string_input
def character_distribution(string):
    ordered_distinct_characters = sorted(set(string))
    distribution = {}
    for unique_character in ordered_distinct_characters:
        distribution[unique_character] = string.count(unique_character)
    return distribution

print(character_distribution("hello, this is a test string."))
print(character_distribution(453))


# ask the user for a positive integer and return a dictionary containing its square, its parity, and its number of digits

def check_positive_integer_input(function):
    def wrapper(*args, **kwargs):
        for i in args:
            if not isinstance(i, int):
                return f"Error: {i} is not an integer."
            if i<=0:
                return f"Error: {i} is not positive."
        for _, value in kwargs.items():
            if not isinstance(value, int):
                return f"Error: {value} is not an integer."
            if value<=0:
                return f"Error: {value} is not positive."
        return function(*args, **kwargs)
    return wrapper

@check_positive_integer_input
def int_stats(integer = int(input("Please type a positive integer (>0):\n"))):
    output = {}
    output['square'] = integer**2
    output['parity'] = 'odd' if integer%2 != 0 else 'even'
    output['digit_count'] = len(str(integer))
    return output

print(int_stats())
print(int_stats(784214))
print(int_stats('hello'))
print(int_stats(-245))
print(int_stats(42.78))


# ask the user for a list of student names and their marks (potentially multiple per student), then return a dictionary with name and average for each student

def student_averages(student_list = None, mark_list = None):
    if student_list is None:
        student_list = input("Type a list of names, separated by a single comma only:\n")
        student_list = student_list.split(',')
    if mark_list is None:
        mark_list = input("Type a list of ONLY MARKS for each student, where the marks are separated by a single comma only, and the students are separated by a space:\n")
        mark_list = [sub_list.split(',') for sub_list in mark_list.split()]
        for sub_list_index in range(len(mark_list)):
            mark_list[sub_list_index] = [float(grade) for grade in mark_list[sub_list_index]]
    base_dictionary = {student:marks for student,marks in zip(student_list, mark_list)}
    avg_dictionary = {student:sum(marks)/len(marks) for student,marks in base_dictionary.items()}
    return avg_dictionary

print(student_averages(student_list=['name1 surname1','name2 surname2', 'name3 surname3', 'name4 surname4'], mark_list=[[8,9,6.5,4],[10,9,10,9.5],[5.5,6,7,4.5],[7.5,8.5,8,9]]))


# write a function that accepts as input a string and returns if it's a palindrome or not

@check_string_input
def palindrome_check(candidate):
    normal = [char.lower() for char in candidate if char.isalnum()]  # use .isalpha() if we don't want to include numbers
    reversed = normal[::-1]
    return True if normal == reversed else False

print(palindrome_check("I TOPI, non avevano nipoti!!"))
print(palindrome_check(3548238))


# write a function for Caesar ciphering, either encoding or decoding

alphabet = 'abcdefghijklmnopqrstuvwxyz'  # 26 letters in the alphabet

def caesar_encoding_letter(decoded, key):  # input a single letter
    check_lower = True
    if decoded.isupper():
        check_lower = False
        decoded = decoded.lower()
    surplus = key%len(alphabet)
    current_position = alphabet.index(decoded)
    left_until_end = len(alphabet)-1-current_position
    if surplus > left_until_end:
        remainder = surplus - left_until_end
        final_index = remainder-1
        return alphabet[final_index] if check_lower else alphabet[final_index].upper()
    else:
        final_index = current_position + surplus
        return alphabet[final_index] if check_lower else alphabet[final_index].upper()
    
def caesar_decoding_letter(encoded, key):  # input a single letter
    check_lower = True
    if encoded.isupper():
        check_lower = False
        encoded = encoded.lower()
    surplus = abs(key)%len(alphabet)
    current_position = alphabet.index(encoded)
    left_until_beginning = current_position
    if surplus > left_until_beginning:
        remainder = surplus - left_until_beginning
        final_index = len(alphabet)-remainder
        return alphabet[final_index] if check_lower else alphabet[final_index].upper()
    else:
        final_index = current_position - surplus
        return alphabet[final_index] if check_lower else alphabet[final_index].upper()

def caesar_ciphering(string, mode, key):
    if mode == 'encode':
        translated = [caesar_encoding_letter(letter, key) if letter.isalpha() else letter for letter in string]
        return ''.join(translated)
    else:
        translated = [caesar_decoding_letter(letter, key) if letter.isalpha() else letter for letter in string]
        return ''.join(translated)

encoding = caesar_ciphering('Hello, world!','encode',1298)
decoding = caesar_ciphering(encoding,'decode',1298)
print(f'{encoding}\n{decoding}')