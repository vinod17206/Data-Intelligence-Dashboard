
import re

def validate_name(name):
    return bool(re.match(r"^[A-Za-z ]{2,50}$", name))

def validate_email(email):
    return bool(re.match(r"^[\w\.-]+@[\w\.-]+\.\w+$",email))

def validate_phone(phone):
    return bool(re.match(r"^[6-9]\d{9}$",phone))

def validate_password(password):
    return bool(re.match(r"^(?=.*[A-Z])(?=.*\d).{6,}$",password))
