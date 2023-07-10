# Strategy: If the counter for each successful character match >= minimum,
# the word passes the trait/requirement-type test

# Case 1: no minimum requirement for a password trait
# Regex = .*    (dot represents any character)
# Strategy: If minimum = 0, automatically accept the word

# Case 2: at least 1 character of the password should have the trait
# Examples:
# 1 uppercase minimum -> Regex = .*[A-Z].*
# 2 uppercase minimum -> Regex = .*[A-Z].*[A-Z].*
# 3 uppercase minimum -> Regex = .*[A-Z].*[A-Z].*[A-Z].*
# Any character is allowed surrounding the trait (shown by the ".*")

# Thus we may use a for loop which neglects the random characters and
# counts only the applicable characters to the trait and then returns
# the accept or unaccepting state of the word as a True or False value.

def check_word(word, req, alphabet):
    accept = False  # default word to unaccepted state/reject
    counter = 0  # default counter to 0

    for index in range(len(word)):  # for loop iterates through characters of word
        if counter == req:  # if minimum criteria is met,
            accept = True  # set accept to "True" and break the loop
            break
        if word[index] in alphabet:  # if character in alphabet fulfills trait
            counter += 1  # increment the counter
        else:
            continue  # otherwise continue to the loop's next iteration

    return accept  # return True or False depending on the accept state
