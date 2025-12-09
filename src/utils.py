# --- src/utils.py ---

import os
import uuid
import re 

def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")

def input_non_empty(prompt):
    """Prompt until the user enters a non-empty string."""
    while True:
        value = input(prompt).strip()
        if value: return value
        print("❌ Input cannot be empty.")

def input_optional_id(prompt):

    """Prompt user for an ID; return None if left empty."""
=======
    """Prompt user for an ID"""
    value = input(prompt).strip()
    return value if value else str(uuid.uuid4())

def input_number(prompt):
    while True:
        value = input(prompt).strip()
        if value.isdigit(): return int(value)
        print("❌ Enter a valid number.")

def input_alpha_spaces(prompt):
    """Ensures input only contains letters and spaces."""
    pattern = re.compile(r'^[A-Za-z\s]+$')
    while True:
        value = input(prompt).strip()
        if not value:
            print("❌ Input cannot be empty. Try again!")
        elif not pattern.match(value):
            print("❌ Only letters and spaces allowed!")
        else:
            return value

def input_email(prompt):
    """Ensures input is a valid email format (contains '@' not at start/end)."""
    while True:
        # First, ensure it's not empty
        email = input_non_empty(prompt)
        # Email validation: must contain '@' and it cannot be the first or last character.
        if 1 <= email.find('@') < len(email) - 1:
            return email
        print("❌ Invalid email format. Email must contain '@' and be in a valid structure. Please try again!")