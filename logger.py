def is_valid_name(name):
    if name == '':
        return False
    for char in name:
        if not (char.isalpha() or char == '-' or char == "'"):
            return False
    return True

def get_valid_name(prompt):
    while True:
        value = input(prompt)
        if is_valid_name(value):
            return value
        print("Invalid input, try again.")

def log_new_shift():
    member_last_name = get_valid_name("Enter last name: ")
    member_first_name = get_valid_name("Enter first name: ")
    member_middle_initial = get_valid_name("Enter middle initial: ")
    member_rank = input("Enter rank: ")
    member_grade = input("Enter grade (e.g. E-3): ")
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
