"""
All errors will be documented and thrown in this python file
"""

import re

def validate_user_name(user_name):
    # Add appropriate validation logic for user_name
    if user_name and re.match(r"^\w{3,20}$", user_name):  # example: username between 3 to 20 alphanumeric characters
        return True
    return False

def validate_phone_number(phone_number):
    # Example: Validate phone number (assuming 10 digits)
    if phone_number and re.match(r"^\d{10}$", phone_number):
        return True
    return False

def validate_user_email(user_email):
    # Validate email address
    if user_email and re.match(r"[^@]+@[^@]+\.[^@]+", user_email):
        return True
    return False

def validate_first_name(first_name):
    # Example: Validate first name (only letters and between 1 to 50 characters)
    if first_name and re.match(r"^[A-Za-z]{1,50}$", first_name):
        return True
    return False

def validate_last_name(last_name):
    # Example: Validate last name (only letters and between 1 to 50 characters)
    if last_name and re.match(r"^[A-Za-z]{1,50}$", last_name):
        return True
    return False

def validate_user_dob(user_dob):
    # Example: Validate date of birth (YYYY-MM-DD format)
    if user_dob and re.match(r"^\d{4}-\d{2}-\d{2}$", user_dob):
        return True
    return False
