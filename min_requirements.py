# Typically, strong passwords are characterized by unique character and/or length requirements:
# This code allows the user to define the password requirements.

def get_min_reqs():
    # Number of uppercase letters
    while True:
        try:
            min_uppercase = int(input("Enter the minimum number of uppercase characters required: "))
            if min_uppercase < 0:
                raise ValueError
            break
        except ValueError:
            print("Oops, enter a valid Non-Negative Integer.")

    # Number of lowercase letters
    while True:
        try:
            min_lowercase = int(input("Enter the minimum number of lowercase characters required: "))
            if min_lowercase < 0:
                raise ValueError
            break
        except ValueError:
            print("Oops, enter a valid Non-Negative Integer.")

    # Number of numerical characters
    while True:
        try:
            min_numerical = int(input("Enter the minimum number of numerical characters required: "))
            if min_numerical < 0:
                raise ValueError
            break
        except ValueError:
            print("Oops, enter a valid Non-Negative Integer.")

    # Number of special characters
    while True:
        try:
            min_special = int(input("Enter the minimum number of special characters required: "))
            if min_special < 0:
                raise ValueError
            break
        except ValueError:
            print("Oops, enter a valid Non-Negative Integer.")

    # Password length
    while True:
        try:
            min_length = int(input("Enter the minimum password length required: "))
            if min_length < 0:
                raise ValueError
            break
        except ValueError:
            print("Oops, enter a valid Non-Negative Integer.")

    return min_uppercase, min_lowercase, min_numerical, min_special, min_length
