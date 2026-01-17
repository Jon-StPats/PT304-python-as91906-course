"""05 — Classes Intro

Goal: Model real-world 'things' as objects.
"""

class Task:
    def __init__(self, name: str, priority: int):
        self.name = name
        self.priority = priority

    def describe(self) -> str:
        return f"{self.name} (Priority {self.priority})"

# Example
example = Task("Math homework", 2)
print(example.describe())

# --- TODO 1 ---
# Create a Task from user input and print its description.

# --- TODO 2 ---
# Create a list of Task objects.
# Add 3 tasks, then print them with numbering.

# --- EXTENSION ---
# Add a method called is_high_priority() that returns True if priority >= 2.
