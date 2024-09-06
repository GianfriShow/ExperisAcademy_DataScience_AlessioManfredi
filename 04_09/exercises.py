# ask the user for 10 numbers, then return min, max, median without using built-in functions for them nor using sort for the median
def descriptive_stats():

    seq = input("Type a list of numbers, separated only by a single comma:\n")

    try:
        seq = seq.split(',')
        seq = [float(i) for i in seq]
    except:
        print("List must contain numbers only, separated by a SINGLE comma only. Try again.")
        descriptive_stats()
    
    def minimum(numbers):
        temp = numbers[0]
        if len(numbers) > 1:
            for num in numbers[1:]:
                if num < temp:
                    temp = num
        return temp
    
    def maximum(numbers):
        temp = numbers[0]
        if len(numbers) > 1:
            for num in numbers[1:]:
                if num > temp:
                    temp = num
        return temp
    
    def sort(numbers):  # only ascending for now
        temp = numbers[:]
        final = []
        for _ in range(len(numbers)):
            current = minimum(temp)
            final.append(current)
            temp.remove(current)
        return final

    def median_value(numbers):
        temp = sort(numbers)
        index = 0
        final = 0
        if len(temp)%2 != 0:
            index = int(len(temp)//2)
            final = temp[index]
        else:
            index = int(len(temp)/2 - 1)
            final = (temp[index]+temp[index+1])/2
        return final

    return print(f"The minimum is {minimum(seq)}, the maximum is {maximum(seq)}, and the median is {median_value(seq)}.")

descriptive_stats()