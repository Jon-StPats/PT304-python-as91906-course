"""02 — Dictionaries

Goal: Group related data (similar to JS objects).
"""

student = {
    "name": "Alex",
    "year": 13,
    "is_student": True
}

print(student["name"], student["year"], student["is_student"])

# --- TODO 1 ---
# Add a new key called "favourite" (ask the user).

# --- TODO 2 ---
# Print every key/value pair.
# Hint: for k, v in student.items():

# --- TODO 3 ---
# Create a list of dictionaries called tasks, each with:
# - name (str)
# - priority (int)
# Print only tasks with priority >= 2.

# --- EXTENSION ---
# Add input validation: priority must be 1, 2, or 3.
