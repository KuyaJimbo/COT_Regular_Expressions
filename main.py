from min_requirements import get_min_reqs
from check_functions import check_word
import random

# Step 1 - Define the languages:
Upper_Alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
Lower_Alphabet = "abcdefghijklmnopqrstuvwxyz"
Special_Alphabet = "!@#$%^&*()_+=-[]{}|:;,.<>?`~"
Numerical_Alphabet = "0123456789"
Full_Alphabet = Upper_Alphabet + Lower_Alphabet + Numerical_Alphabet + Special_Alphabet

# Step 2: Enter the data
print("Password RegEx Options:\n"
      "1) Password Text File\n"
      "2) Password Checker\n"
      "3) Password Generator\n"
      "Choose an option by number: ", end='')

while True:  # Enter Valid Option:
    try:
        option = int(input())
        if (option < 1) or (option > 3):
            raise ValueError
        break
    except ValueError:
        print("Oops, select a valid option by number: ", end='')

# 1) Password Text File
if option == 1:
    # Get content from text file
    while True:
        try:
            file_name = input("Enter the text file name: ")
            # file_name = test_cases.txt
            with open(file_name, 'r') as file:
                content = file.read()
                break
        except FileNotFoundError:
            print("File does not exist.")
    words = content.split(' ')

    # Define what the requirements of our string should be
    min_uppercase, min_lowercase, min_numerical, min_special, min_length = get_min_reqs()
    # Create a list to store accepted words
    accepted_words = []
    for word in words:
        if (check_word(word, min_uppercase, Upper_Alphabet) and
                check_word(word, min_lowercase, Lower_Alphabet) and
                check_word(word, min_special, Special_Alphabet) and
                check_word(word, min_numerical, Numerical_Alphabet) and
                check_word(word, min_length, Full_Alphabet)):
            accepted_words.append(word)  # store all accepted words inside the list

    # Display all accepted words
    print("Accepted Words: ", end='')
    for word in accepted_words:
        print(word, end=' ')


# 2) Password Checker
elif 2 == option:
    content = input("Enter the password(s) you want to test: ")
    words = content.split(' ')

    # Define what the requirements of our string should be
    min_uppercase, min_lowercase, min_numerical, min_special, min_length = get_min_reqs()
    # Create a list to store accepted words
    accepted_words = []
    for word in words:
        if (check_word(word, min_uppercase, Upper_Alphabet) and
                check_word(word, min_lowercase, Lower_Alphabet) and
                check_word(word, min_special, Special_Alphabet) and
                check_word(word, min_numerical, Numerical_Alphabet) and
                check_word(word, min_length, Full_Alphabet)):
            accepted_words.append(word)  # store all accepted words inside the list

    # Display all accepted words
    print("Accepted Words: ", end='')
    for word in accepted_words:
        print(word, end=' ')

# 3) Password Generator
else:
    '''
    pw_gen_min_len = int(input("Enter the minimum desirable length of the password"))
    pw_gen_max_len = int(input("Enter the maximum desirable length of the password"))
    with open("test_cases.txt", "a") as file:
        for word in range(10):  # make 10 potential passwords
            pw_length = random.randint(pw_gen_min_len, pw_gen_max_len)
            pw = ''.join(random.choice(Full_Alphabet))
            break
    '''
    pass
