import re

class User:
    def __init__(self, user_name=None, phone_number=None, user_email=None, first_name=None, last_name=None, user_dob=None):
        self.user_name = user_name
        self.phone_number = phone_number
        self.user_email = user_email
        self.first_name = first_name
        self.last_name = last_name
        self.user_dob = user_dob

    def input_err_av(self):
        '''
        Validate all user inputs and collect any invalid data.
        Returns a tuple (validation_passed: bool, errors: dict).
        '''
        errors = {}

        def validate_user_name(user_name):
            if not user_name or not re.match(r"^\w{3,20}$", user_name):
                return "Invalid user name"
            return None

        def validate_phone_number(phone_number):
            if not phone_number or not re.match(r"^\d{10}$", phone_number):
                return "Invalid phone number"
            return None

        def validate_user_email(user_email):
            if not user_email or not re.match(r"[^@]+@[^@]+\.[^@]+", user_email):
                return "Invalid email address"
            return None

        def validate_first_name(first_name):
            if not first_name or not re.match(r"^[A-Za-z]{1,50}$", first_name):
                return "Invalid first name"
            return None

        def validate_last_name(last_name):
            if not last_name or not re.match(r"^[A-Za-z]{1,50}$", last_name):
                return "Invalid last name"
            return None

        def validate_user_dob(user_dob):
            if not user_dob or not re.match(r"^\d{4}-\d{2}-\d{2}$", user_dob):
                return "Invalid date of birth"
            return None
        
        # Validate each field and collect errors
        errors['user_name'] = validate_user_name(self.user_name)
        errors['phone_number'] = validate_phone_number(self.phone_number)
        errors['user_email'] = validate_user_email(self.user_email)
        errors['first_name'] = validate_first_name(self.first_name)
        errors['last_name'] = validate_last_name(self.last_name)
        errors['user_dob'] = validate_user_dob(self.user_dob)

        # Remove None values from errors dictionary
        errors = {key: value for key, value in errors.items() if value}

        # Return validation status and errors dictionary
        return not errors, errors
    