# Welcome to this simple calculator
# I have not commented this that much in an effort to
# write clear code. I hope its clearly understandable.
# Thank you.
# Application Icon by Freepik
import math


def method():
    x = int(input("Enter first number: "))
    if x != int(x):
        print("Invalid Integer . Try again.")
    print("Enter your Operators as follows:")
    print("1. Addition: 1")
    print("2. Subtraction: 2")
    print("3. Multiplication: 3")
    print("4. Division: 4")
    print("5. Exponent / Power: 5")
    print("6. Modulus / Remainder: 6")
    operator = input("Now, Enter your operator: ")
    y = int(input("Enter second number: "))
    if y != int(y):
        print("Invalid Integer. Try again.")
    if operator == "1":
        z = x + y
        print(z)
    elif operator == "2":
        z = x - y
        print(z)
    elif operator == "3":
        z = x * y
        print(z)
    elif operator == "4":
        z = x / y
        print(z)
    elif operator == "5":
        z = math.pow(x, y)
        print(z)
    elif operator == "6":
        z = x % y
        print(z)
    else:
        print("Invalid try again")
        method()


def ask():
    a = input("Do you want to continue ? ([Y]es / [N]o): ").lower()

    if a == "yes" or a == "ye" or a == "y":
        print("Okay... Continuing.")
    elif a == "no" or a == "n":
        print("Exiting....")
        quit()
    else:
        print("Invalid choice. Continuing....")


loop_counter = 1  # This is static to always repeat it

while loop_counter == 1:
    method()
    ask()

