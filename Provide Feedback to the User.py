def check_password():
    password = input("Enter your password: ")
    feedback = assess_password_strength(password)
    print(feedback)

check_password()
