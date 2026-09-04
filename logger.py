# Check whether a name contains only letters, hyphens, and apostrophes
def is_valid_name(name):
    if name == '':
        return False
    for char in name:
        if not (char.isalpha() or char == '-' or char == "'"):
            return False
    return True

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

# Repeatedly prompt until a valid name is entered, then returns it in sentence case
def get_valid_name(prompt):
    while True:
        value = input(prompt)
        if is_valid_name(value):
            return to_sentence_case(value)
        print("Invalid input, try again.")

# Check whether a grade starts with E or O followed by digits (hyphen optional)
def is_valid_grade(grade):
    if grade == '':
        return False
    prefix = grade[0].upper()
    if prefix != 'E' and prefix != 'O':
        return False
    rest = grade[1:]
    if rest.startswith('-'):
        rest = rest[1:]
    if rest == '':
        return False
    if not rest.isdigit():
        return False
    return True

# Repeatedly prompt until a valid grade is entered, then returns it uppercase
def get_valid_grade(prompt):
    while True:
        value = input(prompt)
        if is_valid_grade(value):
            return value.upper()
        print("Invalid input, try again.")

# Gather all shift report fields from the user
def log_new_shift():
    member_last_name = get_valid_name("Enter last name: ")
    member_first_name = get_valid_name("Enter first name: ")
    member_middle_initial = get_valid_name("Enter middle initial: ")
    member_rank = input("Enter rank: ")
    member_grade = get_valid_grade("Enter grade (e.g. E-3): ")
    member_email = input("Enter email: ")
    member_phone = input("Enter phone number: ")
    shift_start_year = input("Enter shift start year (YYYY): ")
    shift_start_month = input("Enter shift start month: ")
    shift_start_day = input("Enter shift start day: ")
    shift_start_hour = input("Enter shift start hour (HH, 24-hour): ")
    shift_start_minute = input("Enter shift start minute (MM): ")
    shift_end_year = input("Enter shift end year (YYYY): ")
    shift_end_month = input("Enter shift end month: ")
    shift_end_day = input("Enter shift end day: ")
    shift_end_hour = input("Enter shift end hour (HH, 24-hour): ")
    shift_end_minute = input("Enter shift end minute (MM): ")
    task_assigned = input("Enter tasks assigned: ")
    task_completed = input("Enter tasks completed: ")
    task_remaining = input("Enter tasks remaining: ")
    task_remarks = input("Enter tasks remarks: ")
