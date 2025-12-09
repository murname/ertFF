import os
import uuid
import re

def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")

def input_non_empty(prompt):
    while True:
        value = input(prompt).strip()
        if value: return value
        print("❌ Input cannot be empty.")

def input_optional_id(prompt):
    value = input(prompt).strip()
    return value if value else str(uuid.uuid4())

def input_number(prompt):
    while True:
        value = input(prompt).strip()
        if value.isdigit(): return int(value)
        print("❌ Enter a valid number.")

def input_alpha_spaces(prompt):
    pattern = re.compile(r'^[A-Za-z\s]+$')
    while True:
        value = input(prompt).strip()
        if not value:
            print("❌ Input cannot be empty. Try again!")
        elif not pattern.match(value):
            print("❌ Only letters and spaces allowed!")
        else:
            return value

# --- EMAIL VALIDATION ---
def input_email(prompt):
    pattern = re.compile(r'^[^@\s]+@[^@\s]+\.[^@\s]+$')
    while True:
        email = input(prompt).strip()
        if not email:
            print("❌ Email cannot be empty. Try again!")
        elif not pattern.match(email):
            print("❌ Invalid email format. Must contain '@' and a domain.")
        else:
            return email
