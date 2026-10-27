def has_duplicates(numbers):
    seen = set()
    for n in numbers:
        if n in seen:
            return True
        seen.add(n)
