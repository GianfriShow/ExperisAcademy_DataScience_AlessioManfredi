# the "while" loop executes a block of code as long as its condition returns True
count = 0
while count < 5:
    print(count)
    count += 1

# the "for" loop iterates over a sequence of elements or, in general, over an 'iterable', and repeats the block of code for each one of them
'''
for element in sequence:
    block of code to run
'''
numbers = [1,2,3,4,5]
for number in numbers:
    print(number)