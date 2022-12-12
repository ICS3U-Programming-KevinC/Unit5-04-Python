# !/user/bin/env python3

# Created by Kevin Csiffary
# Date: Dec. 5, 2022
# This program is a calculator

# math for pi
import math

# calculates result with given sign and numbers
def calculate(sign, first_number, second_number):
    match sign:
        case "+":
            return first_number + second_number
        case "-":
            return first_number - second_number
        case "*":
            return first_number * second_number
        case "/":
            return first_number / second_number
        case "%":
            return first_number % second_number
        case _:
            # returns pi if there is an error because it is irrational and cant be entered by the user
            return math.pi


def main():
    try:
        # gets user input and casts numbers to floats
        sign = input("Enter the operation you want to preform (+, -, *, /, %): ")
        user_first_num = float(input("Enter the first number: "))
        user_second_num = float(input("Enter the second number: "))
    except:
        print("Please input a valid number")
    else:
        # checks if user is trying to divide by zero
        if (user_second_num == 0) & (sign == "/"):
            print("You cant divide by zero")
        else:
            # calls calculate and stores the result
            result = calculate(sign, user_first_num, user_second_num)
            # checks if the sign was invalid
            if result == math.pi:
                print(f"'{sign}' is not a valid sign")
            else:
                # display the result
                print(
                    f"The result of {user_first_num} {sign} {user_second_num} is {result}"
                )


if __name__ == "__main__":
    main()
