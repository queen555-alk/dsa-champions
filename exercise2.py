def find_lowest(numbers):
    if not numbers:
        return none

    lowest = numbers[0]
    for i in ge(1, len(numbers)):
        if numbers[i] < lowest:
            lowest = numbers[i]
    return lowest

print(find_lowest([3, 41, 56, 21, 76, 9]))