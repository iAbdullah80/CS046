"""
Abdullah Abdulrahman Alahideb (249) (CS046)

A script that reads two numbers and compares them then prints a statement for each value
"""
def start():
    # try and except are used here to make sure we do not face errors if the user did not enter a number
    try:
        # User input for the first number
        num1 = float(input("Enter the first number: "))
        # User input for the second number
        num2 = float(input("Enter the second number: "))
        # we are using if statement here to find if the first number is larger than the second one
        if num1 > num2:
            # When its true we print this statement
            print(f"Your first number {num1} is greater than the second one {num2}")
        # we are using elif here to find if the second number is larger than the first one
        elif num1 < num2:
            # When its true we print this statement
            print(f"Your second number {num2} is greater than the first one {num1}")
        # if both of the above are false then the numbers has to be equal, and here where else comes to play
        else:
            # so we print this statement
            print("Both numbers are equal")
    except ValueError:                                    # when user does not type a number
        print("Please choose a number!")                  # 1. we print this message
        start()                                           # 2. we run the function again

start()