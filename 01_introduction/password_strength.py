import re


def password_strength(password):
    # Initialize strength variable
    strength = 0

    # Check length of password
    if len(password) >= 8:
        strength += 1

    # Check for digits
    if re.search(r'\d', password):
        strength += 1

    # Check for uppercase letters
    if re.search(r'[A-Z]', password):
        strength += 1

    # Check for lowercase letters
    if re.search(r'[a-z]', password):
        strength += 1

    # Check for special characters
    if re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        strength += 1

    return strength


# Test the function with a sample password
pwd = "loveyo1!"
pwd_strength = password_strength(pwd)
print(f"The strength of the password '{pwd}' is: {pwd_strength}/5")
