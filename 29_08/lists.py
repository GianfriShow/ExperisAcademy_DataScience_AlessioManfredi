# lists (list) are ordered and mutable collections of elements
# they can contain elements of different types (e.g. integers, strings, booleans, other lists)
# they are enclosed within square brackets '[]', with elements separated by a comma
numbers = [1,2,3,4,5]
names = ['Alice', 'Bob', 'Charlie']
mixed = [1, 'two', True, 4.5]

# we can index lists to access their ordered elements, with 0 being the first index
numbers = [1,2,3,4,5]
print(numbers[0])
print(numbers[2])

# we can modify a specific element of a list using indices
numbers = [1,2,3,4,5]
numbers[2] = 10
print(numbers)

# we can use several methods with lists
numbers = [3,1,4,2,5]
print(len(numbers))
numbers.append(6)
print(numbers)
numbers.insert(2,10)
print(numbers)
numbers.remove(4)  #this removes the first specified ITEM
numbers.pop(1)  #this removes the element at the specified INDEX
print(numbers)
numbers.sort()
print(numbers)