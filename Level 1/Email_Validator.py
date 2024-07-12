import re

def is_valid_email(email):
    email_exp = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    if re.match(email_exp, email):
        return "Valid"
    else:
        return "Not valild"
email = input("Enter an email address to validate: ").strip()
print(f"{email}: {is_valid_email(email)}")
