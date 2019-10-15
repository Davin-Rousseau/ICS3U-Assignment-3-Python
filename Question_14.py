#!/usr/bin/env python3

# Created by: Davin Rousseau
# Created on October 2019
# This program asks user to pick a number from 0-9
# and tells them if they got it right or wrong


def main():
    # This function makes the user guess a number from 0-9

    # input
    number = input("Enter first integer (0-100): ")
    number2 = input("Enter second integer (0-100) ")
    number3 = input("Enter third integer (0-100) ")
    print("")

    # process
    try:
        integer = int(number)
        integer2 = int(number2)
        integer3 = int(number3)
        if (int(number) > 100):
            print("Could not calculate function")

        elif (int(number) < 0):
            # output
            print("Could not calculate function")

        elif (int(number2) > 100):
            # output
            print("Could not calculate function")

        elif (int(number2) < 0):
            # output
            print("Could not calculate function")

        elif (int(number3) > 100):
            # output
            print("Could not calculate function")

        elif (int(number3) < 0):
            # output
            print("Could not calculate function")

        else:
            # Calculation
            average = (int(number) + int(number2) + int(number3))/3
            # output
            print("The average of the 3 numbers is:{} ".format(average))

    except ValueError:
        print("Could not calculate function")


if __name__ == "__main__":
    main()
