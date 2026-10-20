# Bug report

## Problem
The original `average()` function divides by `len(numbers)`. If the list is empty, its length is zero, so Python raises `ZeroDivisionError`.

## Fix
The fixed version checks whether the list is empty before dividing. It returns `None` for empty input, and the example handles that case with a helpful message.

## Try it
1. Run `buggy.py` and observe the exception.
2. Run `fixed.py` and observe the normal result.
3. If you use Cursor AI for your assignment, record the prompt you actually used and review its suggestion rather than claiming a tool was used when it wasn't.
