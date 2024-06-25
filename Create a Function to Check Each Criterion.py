def has_length(password, min_length=8):
    return len(password) >= min_length

def has_uppercase(password):
    return any(char.isupper() for char in password)

def has_lowercase(password):
    return any(char.islower() for char in password)

def has_digit(password):
    return any(char.isdigit() for char in password)

def has_special_char(password):
    special_characters = "!@#$%^&*()-_=+[]{}|;:,.<>?/"
    return any(char in special_characters for char in password)
