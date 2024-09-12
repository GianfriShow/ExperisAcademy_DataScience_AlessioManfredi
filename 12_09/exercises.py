# write 2 scripts:
# 1) generate 5 random numbers and save them in a file
# 2) game where the user should guess at least 2 of these numbers; if they lose, they can try again 3 more times or decide to give up at any time

import random

def rng(count,path):  # writes a csv file with the list of numbers
    truth = random.sample(range(1,11),count)
    truth = [str(element) for element in truth]
    truth_csv = ','.join(truth)
    with open(path,'w') as my_file:
        my_file.write(truth_csv)

def convert_file_to_list(file_path):  # outputs a list of integers from the csv file
    with open(file_path,'r') as my_file:
        content = my_file.read()
        string_list = content.split(',')
        return [int(element) for element in string_list]

def guessing_game(numbers_sampled = 5, lives = 4):
    rng(numbers_sampled,'12_09/rng.txt')
    true_list = convert_file_to_list('12_09/rng.txt')
    guessed_numbers = []
    while lives>0 and len(guessed_numbers)<2:
        guess = int(input("Type an integer between 1 and 10 (included):\n"))
        if guess in true_list:
            print("Correct")
            guessed_numbers.append(guess)
            true_list.remove(guess)
        else:
            print("Wrong")
            lives -= 1
        if lives == 0:
            print("You lost")
            exit()
        if len(guessed_numbers)==2:
            print("You won")
            exit()
        if int(input("Would you like to continue?\n    1) No\n    2) Yes\n"))-1:
            continue
        else:
            exit()

guessing_game()



# create a long .txt file
# write a programme reading the file that prints the number of words, rows, and characters

text = '''Lorem ipsum dolor sit amet, consectetur adipiscing elit. Duis mattis blandit mauris id facilisis. Sed in erat eu sem volutpat rhoncus quis a enim. Morbi et tempus erat. Morbi pretium, tortor vel iaculis sodales, risus odio volutpat mauris, ut elementum velit est quis tortor. Mauris ac convallis urna, ut fermentum ligula. Praesent sodales quam ut arcu sodales, sit amet condimentum dui volutpat. Aliquam fringilla vitae urna in rhoncus. Nullam porta sapien id faucibus venenatis. In vitae dapibus ligula, eget cursus urna. Nam at sapien nisl. Donec tristique erat dui, vitae malesuada diam tempor in. Nulla non est quam.

Etiam blandit id libero at pulvinar. Fusce at tempor lacus. Curabitur vel ultrices turpis. Mauris non dignissim eros. Sed ultricies diam sed dui luctus ultrices. Cras tincidunt vel massa sed mattis. Praesent lobortis ipsum mi, et condimentum turpis tempor id. Donec vel leo consequat, vehicula libero eget, dapibus erat. Duis quis ullamcorper orci, sed finibus eros. Mauris rutrum volutpat sem, quis viverra quam sodales quis. Donec ut sapien ipsum. Fusce ornare, tellus a luctus semper, elit nisi pretium libero, sed auctor nibh sem ut augue.

Aenean eu nisl et orci fermentum tincidunt nec et turpis. Phasellus eu efficitur mauris. Praesent justo tellus, consectetur a augue iaculis, finibus ultricies dolor. Maecenas in purus varius, blandit ipsum quis, mattis tellus. Cras sit amet dolor et risus pharetra elementum. Donec rutrum eu dolor a laoreet. Sed varius massa et odio vehicula vehicula.'''

with open('12_09/lorem_ipsum.txt','w') as my_file:
    my_file.write(text)

def file_stats(file):  # assume the rows are separated by '\n' only
    with open(file,'r') as my_file:
        content = my_file.read()
        list_of_rows = content.split('\n')
        row_number = len(list_of_rows)
        list_of_cleaned_rows = [''.join([character if character.isalpha() else " " for character in row]) for row in list_of_rows]  # replace non-alphabetical characters with spaces]
        list_of_words_per_row = [row.split() for row in list_of_cleaned_rows]
        word_number = 0
        for words in list_of_words_per_row:
            word_number += len(words)
        list_non_whitespace_characters_per_row = [''.join([character if character != " " else "" for character in row]) for row in list_of_rows]
        non_whitespace_character_count = 0
        for chars in list_non_whitespace_characters_per_row:
            non_whitespace_character_count += len(chars)
        return row_number, word_number, non_whitespace_character_count

print(file_stats('12_09/lorem_ipsum.txt'))



# create a management system for students
# if there's a database already, read it, otherwise create it
# the user can add students and grades in the db, or remove/modify entries
# STUDENT NAMES ARE UNIQUE for simplicity (primary key)

def dictionary_to_csv(dic):  # dictionary must be (student,vote) where 'vote' is a list of numbers
    final = """"""
    for key,value in dic.items():
        final += '\n' + key + ',' + '_'.join([str(i) for i in value])
    return final

def csv_to_dictionary(csv):  # take csv where first line has variable names and remove it
    with open(csv,'r') as database:
        content = database.read()
    rows = content.split('\n')  # variable names still in for now
    split_rows = [row.split(',') for row in rows]
    dic = {pair[0]:pair[1] for pair in split_rows[1:]}
    for key in dic:
        dic[key] = [float(i) for i in dic[key].split('_')]
    return dic

def student_database(path, new_data = 0, overwrite = False):  # new_data will accept a dictionary (student,vote)
    if not new_data:  # if we add nothing, we just read the existing database
        with open(path,'r') as database:
            content = database.read()
            print(content)
    elif not overwrite:  # append
        try:
            with open(path,'r') as database:
                if database.read().strip() == '':
                    with open(path,'w') as database:
                        database.write('name,votes')
                        addend = dictionary_to_csv(new_data)
                        database.write(addend)
                        print(database)
                else:
                    with open(path,'a') as database:
                        addend = dictionary_to_csv(new_data)
                        database.write(addend)
                        print(database)
        except:
            with open(path,'a') as database:
                database.write('name,votes')
                addend = dictionary_to_csv(new_data)
                database.write(addend)
                print(database)
    else:  # overwrite
        with open(path,'w') as database:
            database.write('name,votes')
            content = dictionary_to_csv(new_data)
            database.write(content)
            print(database)

path = '12_09/student_database.csv'
database = {'Kevin':[7,9,6,7.5],'Mark':[6,7,6,9],'Hannah':[8,8.5,7.5,9],'John':[5,6,6.5,4]}
student_database(path,database)

def modify_students(path, edit):  # specify existing database and provide a dictionary with students to modify and their modified list of votes
    dic = csv_to_dictionary(path)
    for student in edit:
        dic[student] = edit[student]
    csv = dictionary_to_csv(dic)
    with open(path,'w') as database:
        database.write('name,votes')
        database.write(csv)

def remove_students(path, black_list):  # black_list is a list of students to remove
    dic = csv_to_dictionary(path)
    for student in black_list:
        del dic[student]
    csv = dictionary_to_csv(dic)
    with open(path,'w') as database:
        database.write('name,votes')
        database.write(csv)

modify_students(path, {'Mark':[10,10,10,10]})
student_database(path)
remove_students(path, ['Mark','John'])
student_database(path)