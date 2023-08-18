def get_user_choice():
    """
    Prompt the user to enter a string between 1 and 4 to select the arithmetic operation.

    """

    print("Select operation.")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")

    while True:
        choice = input("Enter choice (1/2/3/4): ")
        if choice in ('1', '2', '3', '4'):
            return choice
        else:
            print("Invalid choice. Please enter a valid option.")

