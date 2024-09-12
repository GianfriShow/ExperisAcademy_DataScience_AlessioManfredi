a,b = 10,'hello'

try:
    print(a/b)
    print("Code successfully executed")
except ZeroDivisionError as e:
    print(f'Error: {e}')
except TypeError as e:
    print(f'Error: {e}')
except:  # any other unaccounted error type if we don't specify it
    print('Unknown error')


# with open('test.txt','r') as my_file:  # if the file we try to open doesn't exist, we'll raise a FileNotFoundError
#     content = my_file.read()

def read_file(file_path):
    with open(file_path,'r') as my_file:
        content = my_file.read()
        return content  # in this case, return is inside the with statement, since as soon as we close it 'content' will go away

path = '12_09/test.txt'
print(read_file(path))

def append_file(file_path,text_to_append):
    with open(file_path,'a') as my_file:
        my_file.write(text_to_append)

addend = '\nHello again!'
append_file(path,addend)
print(read_file(path))


path = '12_09/test.csv'
with open(path,'w') as my_file:
    my_file.write('name,surname,age\nthomas,bellington,21\nrobert,janish,34')

def csv_to_rows(path,separator='\n'):
    return read_file(path).split(separator)

rows = csv_to_rows(path)
print(rows)

def csv_rows_to_lists(rows,variable_names=True):
    return [row.split(',') for row in rows[variable_names:len(rows)]]

print(csv_rows_to_lists(rows,variable_names=True))

new_name = 'alfred'
new_surname = 'green'
new_age = '46'
new_row = f'\n{new_name},{new_surname},{new_age}'

path = '12_09/test.csv'
append_file(path,new_row)
print(read_file(path))
print(csv_rows_to_lists(csv_to_rows(path)))