from datetime import datetime, timezone

# Check whether a name contains only letters, hyphens, and apostrophes, and at least one letter
def is_valid_name(name):
    if name == '':
        return False
    has_letter = False
    for char in name:
        if char.isalpha():
            has_letter = True
        elif char != '-' and char != "'":
            return False
    return has_letter

# Capitalize the first letter of a name and the first letter after any hyphen or apostrophe
def to_sentence_case(name):
    result = ''
    capitalize_next = True
    for char in name:
        if capitalize_next and char.isalpha():
            result = result + char.upper()
            capitalize_next = False
        else:
            result = result + char.lower()
        if char == '-' or char == "'":
            capitalize_next = True
    return result

# Repeatedly prompt until a valid name is entered, then return it in sentence case
def get_valid_name(prompt):
    while True:
        value = input(prompt)
        if is_valid_name(value):
            return to_sentence_case(value)
        print("Invalid input, try again")

# Prompt the user through a guided menu to select a rank and grade
def get_rank_and_grade_selection():
    while True:
        category = input("Select your rank category:\n1. Enlisted\n2. Officer\n> ")
        if category == '1' or category == '2':
            break
        print("Invalid input, try again")
    if category == '1':
        rank_options = ('E-1\tSpc1', 'E-2\tSpc2', 'E-3\tSpc3', 'E-4\tSpc4', 'E-5\tSgt', 'E-6\tTSgt', 'E-7\tMSgt', 'E-8\tSMSgt', 'E-9\tCMSgt')
    else:
        rank_options = ('O-1\t2d Lt', 'O-2\tLt', 'O-3\tCapt', 'O-4\tMaj', 'O-5\tLt Col', 'O-6\tCol', 'O-7\tBGen', 'O-8\tMaj Gen', 'O-9\tLt Gen', 'O-10\tGen')
    while True:
        print("Choose rank and grade:")
        index = 1
        for rank_option in rank_options:
            option_grade, option_title = rank_option.split('\t')
            print(str(index) + ". " + option_title + " (" + option_grade + ")")
            index = index + 1
        choice = input("> ")
        if choice.isdigit() and 1 <= int(choice) <= len(rank_options):
            selected_grade, selected_title = rank_options[int(choice) - 1].split('\t')
            confirm = input("You selected " + selected_title + " (" + selected_grade + "). Confirm? (Y/N): ")
            if confirm.upper() == 'Y':
                return selected_grade, selected_title
        else:
            print("Invalid input, try again")

# Check whether an email is in the form username@domain.mil or .gov
def is_valid_email(email):
    if email == '':
        return False
    if email.count('@') != 1:
        return False
    username, domain = email.split('@')
    if username == '':
        return False
    if domain == '':
        return False
    domain_lower = domain.lower()
    if not (domain_lower.endswith('.mil') or domain_lower.endswith('.gov')):
        return False
    return True

# Repeatedly prompt until a valid email is entered
def get_valid_email(prompt):
    while True:
        value = input(prompt)
        if is_valid_email(value):
            return value
        print("Invalid input, try again")

# Check whether a phone number is exactly 10 digits
def is_valid_phone(phone):
    if len(phone) != 10:
        return False
    if not phone.isdigit():
        return False
    return True

# Repeatedly prompt until a valid phone number is entered
def get_valid_phone(prompt):
    while True:
        value = input(prompt)
        if is_valid_phone(value):
            return value
        print("Invalid input, try again")

# Check whether the input is not empty
def is_not_empty(text):
    return text != ''

# Repeatedly prompt until a non-empty value is entered
def get_non_empty(prompt):
    while True:
        value = input(prompt)
        if is_not_empty(value):
            return value
        print("Invalid input, try again")

# Gather all shift report fields from the user
def log_new_shift():
    entry_started_timestamp = datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%SZ')
    print("Starting your shift...")
    # Gather information about the member
    member_last_name = get_valid_name("Enter last name: ")
    member_first_name = get_valid_name("Enter first name: ")
    member_middle_initial = get_valid_name("Enter middle initial: ")
    member_grade, member_rank = get_rank_and_grade_selection()
    member_email = get_valid_email("Enter email: ")
    member_phone = get_valid_phone("Enter phone number: ")
    # Gather information about the tasks
    task_assigned = get_non_empty("Enter tasks assigned: ")
    task_completed = get_non_empty("Enter tasks completed: ")
    task_remaining = get_non_empty("Enter tasks remaining: ")
    task_remarks = get_non_empty("Enter tasks remarks: ")
    # Get confirmation of shift ending
    input("Press Enter to confirm your shift is complete (Enter): ")
    confirmed_complete_timestamp = datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%SZ')
