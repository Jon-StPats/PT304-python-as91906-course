"""04 — Persistence Task (JSON)

TASK:
Create a program that stores a list of tasks and remembers them between runs.

REQUIREMENTS:
- Use JSON save/load
- Menu options:
  1. Add task
  2. View tasks
  3. Save & Exit
- Handle missing file (first run)
- Validate user input (no blank task name)

HINT:
Use:
import json
json.dump(data, file)
json.load(file)

EXTENSION:
- Store tasks as dictionaries with a priority
- Add an option to delete a task
"""
