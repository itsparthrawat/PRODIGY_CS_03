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

def assess_password_strength(password):
    criteria = [
        has_length(password),
        has_uppercase(password),
        has_lowercase(password),
        has_digit(password),
        has_special_char(password)
    ]
    
    strength = sum(criteria)
    
    feedback = ""
    if strength == 5:
        feedback = "Password is very strong."
    elif strength == 4:
        feedback = "Password is strong."
    elif strength == 3:
        feedback = "Password is moderate."
    elif strength == 2:
        feedback = "Password is weak."
    else:
        feedback = "Password is very weak."
    
    return feedback

def check_password():
    password = input("Enter your password: ")
    feedback = assess_password_strength(password)
    print(feedback)

check_password()
