#!/usr/bin/env python3
# Created By: Fred
# Date: Feb 18 2008
# Check if an number is the correct guess or not

def main():

    import random

    random_variable = random.randint(1, 9)  # a number between 1 and 9

    # get the number from the user
    number = float(input("Enter a number between 0 and 10 \n"))

    # Check if the number is the correct guess
    if random_variable == number:
        print("\n The number is the correct guess")

    # If not, then tell the user the correct number
    else:
        print(
            "\n Sorry, you are wrong. The correct guess is {}".format( random_variable )
        )


if __name__ == "__main__":

    main()
