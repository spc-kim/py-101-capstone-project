import logger

def main():
    while True:
        choice = input("1. Log new shift\n2. View saved reports\n3. Quit\n> ")
        if choice == '1':
            logger.log_new_shift()
        elif choice == '2':
            logger.view_reports()
        elif choice == '3':
            break
        else:
            print("Invalid input, try again")

if __name__ == "__main__":
    main()
