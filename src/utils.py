# utils.py

from datetime import datetime

def get_timestamp():
    """Returns the current timestamp in seconds"""
    return int(datetime.now().timestamp())

def generate_uuid():
    """Generates a random UUID"""
    import uuid
    return str(uuid.uuid4())

def is_valid_email(email: str) -> bool:
    """Checks if an email is valid"""
    import re
    return bool(re.match(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$', email))

def is_valid_password(password: str) -> bool:
    """Checks if a password is valid (at least 8 characters, 1 digit, 1 lowercase, 1 uppercase)"""
    import re
    return bool(re.match(r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d).{8,}$', password))