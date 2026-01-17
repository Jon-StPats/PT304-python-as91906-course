"""06 — Input Validation

Goal: Make programs robust (Excellence pathway).
"""

def read_int(prompt: str) -> int:
    """Keep asking until the user enters a valid integer."""
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Please enter a whole number.")

# Example
n = read_int("Enter a number: ")
print("Twice is", n * 2)

# --- TODO 1 ---
# Write a function read_choice(prompt, options) that:
# - asks the user
# - only accepts values inside options
# - returns the valid choice
# Example: choice = read_choice("Choose 1-3: ", ["1","2","3"])

# --- TODO 2 ---
# Add validation to a menu program:
# - user must choose a valid option
# - program should never crash on bad input

# --- EXTENSION ---
# Write read_priority() that only accepts 1, 2, or 3.
