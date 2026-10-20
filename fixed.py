"""Fixed average function with an explicit empty-input check."""


def average(numbers):
    if not numbers:
        return None
    return sum(numbers) / len(numbers)


values = [10, 20, 30]
result = average(values)
if result is None:
    print("No average available: the list is empty.")
else:
    print(f"Average: {result:g}")
