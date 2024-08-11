import re

def find_strength(password):
    strength_score = 0
    
    if len(password) >= 8:
        strength_score += 1
    else:
        print("Password is too short. It should be at least 8 characters long.")

    if re.search(r'[A-Z]', password):
        strength_score += 1
    else:
        print("Password should contain at least one uppercase letter.")

    if re.search(r'[a-z]', password):
        strength_score += 1
    else:
        print("Password should contain at least one lowercase letter.")

    if re.search(r'[0-9]', password):
        strength_score += 1
    else:
        print("Password should contain at least one digit.")

    if re.search(r'[!@#$%^&*(),.?":{}|<>]', password):
        strength_score += 1
    else:
        print("Password should contain at least one special character (e.g., !, @, #, $).")
    
    if strength_score == 5:
        return "Strong password."
    elif 3 <= strength_score < 5:
        return "Moderate password."
    else:
        return "Weak password."

password = input("Enter your password: ")
strength = find_strength(password)
print(strength)
