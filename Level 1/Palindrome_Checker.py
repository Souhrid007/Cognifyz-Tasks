def is_palindrome(s):
    s = s.replace(" ", "").lower()
    return s == s[::-1]

string = input("Enter a string: ")

if is_palindrome(string):
    print(string," is a palindrome.")
else:
    print(string," is not a palindrome.")
