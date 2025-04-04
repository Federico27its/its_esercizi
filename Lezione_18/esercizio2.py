'''
Password Validation: Write a function validate_password(password) that checks if a password meets certain criteria
(i.e., minimum length of 20 characters, at least three uppercase characters, and at least four special characters). 
Raise a custom exception (e.g., InvalidPasswordError) for invalid passwords.
'''

class InvalidPasswordError(BaseException):
    """Invalid Password Error"""

def validate_password(password: str) -> None:
    upper = 0
    special = 0
    for char in password:
        if char.isupper():
            upper += 1
        elif not char.isalnum():
            special += 1

    if upper >= 3 and special >= 4 and len(password) >= 20:
        print("Valid")
    else:
        raise InvalidPasswordError("Invalid Password Error")
