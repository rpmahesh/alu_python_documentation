def get_number_input(prompt):
    """
    Prompt the user to enter a number and check it's a numerical value.

    :param prompt: Prompt the user to enter a number
    :return value (float): Validated floating point number
    :raises: ValueError : Error raised when user input cannot be converted to a float.

    """

    while True:
        try:
            value = float(input(prompt))
            return value
        except ValueError:
            print("Invalid input. Please enter a number.")
