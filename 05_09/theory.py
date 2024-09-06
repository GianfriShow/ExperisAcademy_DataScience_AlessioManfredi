# scientific notation: 'e' stands for '10 to the power of'
print(8.4e100)
print(8.4e-10)


# f strings
name = "Thomas"
age = 35
print(f'My friend {name} is {age} years old.')


# ternary operator
licence = True
print("Driving is allowed.") if licence else print("Driving is NOT allowed.")

my_list = ['string', 9, 9.9, [1,2,3]]  # we can have as many different types for the elements inside a list
print(my_list[-1])  # return last element of a list (backward indexing starts from -1 and decreases by 1 as we move leftwards)
print(my_list[-1][-1])  # return last element of the last element inside the list


# slicing (behaves similarly to range())
my_list = [0,1,2,3,4,5,6,7,8,9]
print(my_list[1:5])  # return elements from index 1 (included) to index 5 (excluded): first bound is always included, last bound is always excluded
print(my_list[:3])  # return all elements from the beginning until index 3 (excluded)
print(my_list[3:])  # return all elements from index 3 (included) until the end (the end is included in this special case)
print(my_list[3:7:2])  # just like range() notation, print from index 3 (included) to index 7 (excluded), jumping by 2 indices each time instead of 1
print(my_list[::-1])  # print whole list backwards


# some list methods
my_list = [0,1,2,3,4,5,6,7,8,9]
addition = [10,11,12,13,14,15]
my_list.append(addition)  # append adds the argument as a single element
print(my_list)

my_list = [0,1,2,3,4,5,6,7,8,9]
my_list.extend(addition)  # extend unpacks the argument and adds each element separately
print(my_list)

my_list = [0,1,2,3,4,5,6,7,8,9]
my_list.insert(4, addition)  # insert the second argument in the list at index equal to the first argument
print(my_list)

my_list = [4,7,6,2,5,3,1,9,8]
my_list.sort(reverse=True)  # sort the original list, default is ascending
print(my_list)

my_list = [4,7,6,2,5,3,1,5,9,8]
print(my_list.index(5))  # return index of first instance of the argument

my_list.remove(5)  # remove first instance of the argument
print(my_list)

my_list = [0,1,2,3,4,5,6,7,8,9]
print(my_list.pop(7))  # remove element at specified index and return it
print(my_list.pop())  # by default, the element removed is the last one in the sequence
del my_list[3]  # delete element at specific index
print(my_list)

my_list = [0,1,2,3,4,5,6,7,8,9]
my_list[5] = "Hello"  # replace a specific value
print(my_list)


# some string methods
my_string = "Hello, how is it going?"
print(my_string.startswith('Hel'))  # returns a boolean to check if a string starts a certain way (case sensitive since it's a string)
print(my_string.endswith('world'))  # check the end instead

my_string = "hello23world"
print(my_string.isalnum())  # check if the string is composed by alpha-numeric characters only
print(my_string.isdecimal())  # check if string contains numbers only

my_string = "what's up, everyone?"
my_string.replace('everyone', 'no one')  # returns a COPY of the string, replacing all instances of the first argument with the second argument
my_string = my_string.replace('everyone', 'no one')
print(my_string)

my_string = "you make it look like it's magic, because I see nobody but you"
print(my_string.count("you"))  # count the number of instances of the argument inside the string

my_string = "hello,this,is,a,test,string,to,split,apart,and,join,back,together"
print(my_string.split(','))  # splits based on a delimiter; by default, it will split on any whitespace character (including \n \r \t \f and spaces)
                             # and will discard empty strings from the result
split_string = my_string.split(',')
joined_string = ' '.join(split_string)  # joins a list of elements in a string where they are separated by the specified delimiter (before the method)
print(joined_string)


# list comprehension
my_list = ['hello', 'everybody', 'goodbye', 'red', 'blue', 'one', 'two', 'salty']

filtered_list = [word for word in my_list if "e" not in word]  # return a list based on a condition (e.g. words without the letter 'e')
print(filtered_list)


# list vs tuple
my_list = [1,2,3,4,5]
my_tuple = (1,2,3,4,5)
my_list[2] = "hello"  # lists are mutable
#my_tuple[2] = "hello"  # tuples are immutable


# sets
my_set = {1,2,3,4,5}  # sets are UNORDERED collections of UNIQUE elements
print(my_set)
my_set.add(3)  # this is pointless because the set doesn't allow duplicates, so it will be unchanged
print(my_set)

my_list = [1,2,3,4,2,3,4,5]
my_set = set(my_list)  # we can convert a list to a set (and viceversa), but duplicate entries will be eliminated
print(my_set)
print(list(my_set))  # reverse operation, but now the list will have lost the original duplicates


# dictionaries
my_dic = {'name':'Mark', 'surname':'Wilson'}  # dictionaries have keys and values
print(my_dic['name'])  # return the value of a given key

my_dic = {1:{'name':'Mark', 'age':'22'}, 2:{'name':'Ross', 'age':'43'}}  # we can nest dictionaries
print(my_dic[2]['name'])  # and also do multiple indexing when nested

my_dic = {'name':'Mark', 'surname':'Wilson'}
my_dic['age'] = '17'  # we can quickly add a new key and its corresponding value to a dictionary using indexing
print(my_dic)

for key in my_dic:  # iterating through a dictionary returns its keys
    print(key)

for value in my_dic.values():  # to iterate through the values instead, we use the method values()
    print(value)

for item in my_dic.items():  # the method items() returns a list of tuples, each with a key and its corresponding value
    print(item)

print(my_dic.get('address',"address not available"))  # try to return the value of a key (first argument), if not present, return the second argument

my_dic.setdefault('address','Fake Street')  # similarly to get(), try to return the value of the key, but if not present, ADD it to the dictionary
print(my_dic)


# enumerate
my_list = ['hello','everyone','good','morning']
print(list(enumerate(my_list)))  # enumerate() returns a list of tuples, with the index of each element in the list and the element itself