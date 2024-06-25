tdef assess_password_strength(password):
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
