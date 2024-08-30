# 'break' allows to preemptively and completely interrupt a loop under a given condition
numbers = [1,2,3,4,5]
for number in numbers:
    if number == 3:
        break
    print(number)

# 'continue' is similar to break, but it only skips ONE iteration (from where it is in the block) instead of interrupting all future ones
numbers = [1,2,3,4,5]
for number in numbers:
    if number == 3:
        continue
    print(number)

# 'pass' is usually a placeholder for future edits since it doesn't effectively do anything
for i in range(5):
    if i == 3:
        pass
    print(i)