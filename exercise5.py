def count_occurrences(numbers, target):
    count = 0
    for number in numbers:
        if number == target:
            count += 1
    return count

numbers = [2, 5, 2, 8, 2]
target = 2
print(count_occurrences(numbers, target))