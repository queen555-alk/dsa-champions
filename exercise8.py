def has_duplicates(numbers):
    seen = set()
    for n in numbers:
        if n in seen:
            return True
        seen.add(n)
    return False

print(has_duplicates([1, 2, 3, 2]))