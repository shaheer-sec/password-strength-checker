import re

def check_password_strength(password):
    length_error = len(password) < 8
    digit_error = re.search(r"\d", password) is None
    uppercase_error = re.search(r"[A-Z]", password) is None
    lowercase_error = re.search(r"[a-z]", password) is None
    symbol_error = re.search(r"[ !@#$%^&*()_+\-=\[\]{};':\"\\|,.<>\/?]", password) is None

    errors = [length_error, digit_error, uppercase_error, lowercase_error, symbol_error]
    score = 5 - sum(errors)

    if score == 5:
        return "Strong Password!"
    elif score >= 3:
        return "Moderate Password. Consider adding more characters/symbols."
    else:
        return "Weak Password! Please improve your password security."

if __name__ == "__main__":
    user_pass = input("Enter a password to test its strength: ")
    result = check_password_strength(user_pass)
    print("Result:", result)
