def find_largest(numbers):
    if not numbers:
        return none

    largest = numbers[0]
    for i in range(1, len(numbers)):
        if numbers[i] > largest:
            largest = numbers[i]
    return largest

print(find_largest([3, 41, 56, 21, 76, 9]))