# Intentionally buggy example: this raises ZeroDivisionError for an empty list.
def average(numbers):
    return sum(numbers) / len(numbers)


print("Average:", average([]))
