from alu.addition import add
from alu.subtraction import subtract
from alu.multiplication import multiply
from alu.division import divide

import utils.get_number_input as get_number
import utils.get_user_choice as user_choice


def perform_calculation(choice, num1, num2):
    """
    Takes choice, num1, and num2 as arguments, and performs an arithmetic operation.

    :param num1: first number
    :param num2: second number
    :param choice: integer between 1 and 4  
    
    """
    if choice == '1':
        print(num1, "+", num2, "=", add(num1, num2))
    elif choice == '2':
        print(num1, "-", num2, "=", subtract(num1, num2))
    elif choice == '3':
        print(num1, "*", num2, "=", multiply(num1, num2))
    elif choice == '4':
        if num2 != 0:
            print(num1, "/", num2, "=", divide(num1, num2))
        else:
            print("Cannot divide by zero.")


def main():
    while True:
        choice = user_choice.get_user_choice()
        num1 = get_number.get_number_input("Enter first number: ")
        num2 = get_number.get_number_input("Enter second number: ")
        perform_calculation(choice, num1, num2)

        next_calculation = input("Do you want to perform another calculation? (yes/no): ")
        if next_calculation.lower() == "no":
            break


if __name__ == "__main__":
    main()

