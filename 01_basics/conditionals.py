"""01 — Conditionals (if / elif / else)

Goal: Use selection to make decisions.
"""

# --- Example ---
score = 85

if score >= 80:
    print("High score")
elif score >= 50:
    print("Pass")
else:
    print("Not yet")

# --- TODO 1 ---
# Ask the user for a test mark (0–100).
# Print:
# - "Excellence" for 80–100
# - "Merit" for 50–79
# - "Achieved" for 0–49
# Also handle invalid marks (<0 or >100) with "Invalid mark".

# --- TODO 2 ---
# Ask the user for a password.
# If it equals "python" print "Access granted" else print "Access denied".

# --- EXTENSION ---
# Add a second factor: also ask for a PIN (number).
# Only grant access if BOTH are correct.
