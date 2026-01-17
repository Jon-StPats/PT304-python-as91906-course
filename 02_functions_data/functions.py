"""02 — Functions

Goal: Use functions to organise code (Merit/Excellence pathway).
"""

# --- Example ---
def greet(name: str) -> None:
    print(f"Hello {name}!")

greet("Sam")

# --- TODO 1 ---
# Write a function called add(a, b) that RETURNS the sum.

# --- TODO 2 ---
# Write a function called is_even(n) that returns True if n is even else False.

# --- TODO 3 ---
# Write a function called clamp(n, low, high) that:
# - returns low if n < low
# - returns high if n > high
# - otherwise returns n

# --- EXTENSION ---
# Write a function called safe_int(text) that:
# - returns an int if possible
# - returns None if it can't convert
