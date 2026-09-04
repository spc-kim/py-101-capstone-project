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

# Repeatedly prompt until a valid name is entered, then return it in sentence case
def get_valid_name(prompt):
    while True:
        value = input(prompt)
        if is_valid_name(value):
            return to_sentence_case(value)
        print("Invalid input, try again")

# Prompt the user through a guided menu to select a rank
def get_rank_selection():
    while True:
        category = input("Choose category:\n1. Enlisted\n2. Officer\n> ")
        if category == '1' or category == '2':
            break
        print("Invalid input, try again")
    if category == '1':
        ranks = ('Spc1', 'Spc2', 'Spc3', 'Spc4', 'Sgt', 'TSgt', 'MSgt', 'SMSgt', 'CMSgt')
    else:
        ranks = ('2d Lt', 'Lt', 'Capt', 'Maj', 'Lt Col', 'Col', 'BGen', 'Maj Gen', 'Lt Gen', 'Gen')
    while True:
        print("Choose rank:")
        index = 1
        for rank in ranks:
            print(str(index) + ". " + rank)
            index = index + 1
        choice = input("> ")
        if choice.isdigit() and 1 <= int(choice) <= len(ranks):
            selected_rank = ranks[int(choice) - 1]
            confirm = input("You selected " + selected_rank + ". Confirm? (Y/N): ")
            if confirm.upper() == 'Y':
                return selected_rank
        else:
            print("Invalid input, try again")

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

# Repeatedly prompt until a valid grade is entered, then return it uppercase
def get_valid_grade(prompt):
    while True:
        value = input(prompt)
        if is_valid_grade(value):
            return value.upper()
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
    if not (domain.endswith('.mil') or domain.endswith('.gov')):
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

# Check whether a year is exactly four digits
def is_valid_year(year):
    if len(year) != 4:
        return False
    if not year.isdigit():
        return False
    return True

# Repeatedly prompt until a valid year is entered
def get_valid_year(prompt):
    while True:
        value = input(prompt)
        if is_valid_year(value):
            return value
        print("Invalid input, try again")

# Check whether a month is a number from 1 to 12
def is_valid_month(month):
    if not month.isdigit():
        return False
    month_num = int(month)
    return 1 <= month_num <= 12

# Repeatedly prompt until a valid month is entered
def get_valid_month(prompt):
    while True:
        value = input(prompt)
        if is_valid_month(value):
            return value
        print("Invalid input, try again")

# Check whether a day is valid for the given month
def is_valid_day(day, month):
    if not day.isdigit():
        return False
    day_num = int(day)
    month_num = int(month)
    if month_num in (4, 6, 9, 11):
        return 1 <= day_num <= 30
    elif month_num == 2:
        return 1 <= day_num <= 29
    else:
        return 1 <= day_num <= 31

# Repeatedly prompt until a valid day is entered for the given month
def get_valid_day(prompt, month):
    while True:
        value = input(prompt)
        if is_valid_day(value, month):
            return value
        print("Invalid input, try again")

# Check whether an hour is valid military time (00-23)
def is_valid_hour(hour):
    if len(hour) != 2:
        return False
    if not hour.isdigit():
        return False
    first = hour[0]
    second = hour[1]
    if first not in ('0', '1', '2'):
        return False
    if first == '2' and second not in ('0', '1', '2', '3'):
        return False
    return True

# Repeatedly prompt until a valid hour is entered
def get_valid_hour(prompt):
    while True:
        value = input(prompt)
        if is_valid_hour(value):
            return value
        print("Invalid input, try again")

# Check whether a minute is valid (00-59)
def is_valid_minute(minute):
    if len(minute) != 2:
        return False
    if not minute.isdigit():
        return False
    first = minute[0]
    second = minute[1]
    if first not in ('0', '1', '2', '3', '4', '5'):
        return False
    if second not in ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9'):
        return False
    return True

# Repeatedly prompt until a valid minute is entered
def get_valid_minute(prompt):
    while True:
        value = input(prompt)
        if is_valid_minute(value):
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
    # Gather information about the member
    member_last_name = get_valid_name("Enter last name: ")
    member_first_name = get_valid_name("Enter first name: ")
    member_middle_initial = get_valid_name("Enter middle initial: ")
    member_rank = get_rank_selection()
    member_grade = get_valid_grade("Enter grade (e.g. E-3): ")
    member_email = get_valid_email("Enter email: ")
    member_phone = get_valid_phone("Enter phone number: ")
    # Gather information about the shift
    shift_start_year = get_valid_year("Enter shift start year (YYYY): ")
    shift_start_month = get_valid_month("Enter shift start month: ")
    shift_start_day = get_valid_day("Enter shift start day: ", shift_start_month)
    shift_start_hour = get_valid_hour("Enter shift start hour (HH, 24-hour): ")
    shift_start_minute = get_valid_minute("Enter shift start minute (MM): ")
    shift_end_year = get_valid_year("Enter shift end year (YYYY): ")
    shift_end_month = get_valid_month("Enter shift end month: ")
    shift_end_day = get_valid_day("Enter shift end day: ", shift_end_month)
    shift_end_hour = get_valid_hour("Enter shift end hour (HH, 24-hour): ")
    shift_end_minute = get_valid_minute("Enter shift end minute (MM): ")
    # Gather information about the tasks
    task_assigned = get_non_empty("Enter tasks assigned: ")
    task_completed = get_non_empty("Enter tasks completed: ")
    task_remaining = get_non_empty("Enter tasks remaining: ")
    task_remarks = get_non_empty("Enter tasks remarks: ")
