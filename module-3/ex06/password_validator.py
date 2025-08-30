import string

def is_valid_password(password: str) -> bool:
    """Checks if a password meets the required validation criteria."""
    if len(password) < 8 or len(password) > 16:
        return False
    if not any(c.isupper() for c in password):
        return False
    if not any(c.islower() for c in password):
        return False
    if not any(c.isdigit() for c in password):
        return False
    if not any(c in string.punctuation for c in password):
        return False
    if any(c.isspace() for c in password):
        return False
    return True
   
