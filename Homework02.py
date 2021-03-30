"""
Abdullah Abdulrahman Alahideb (249) (CS046)

A script that outputs first name, last name and calculates the grade average of three university courses
"""


def start():
    # try and except are used here to make sure we do not face errors if the user did not enter a number
    try:
        print("Please enter the following values")
        first_name = input("First name: ")                      # user input for the first name
        last_name = input("Last name: ")                        # user input for the last name
        course1 = float(input("Math grade: "))                  # user input for the math grade
        course2 = float(input("English grade: "))               # user input for the english grade
        course3 = float(input("Computer Science grade: "))      # user input for the Computer Science grade
        average_of3courses = (course1 + course2 + course3) / 3  # the average of three values formula ( (x + y + z)/3 )

        # show the user first name in a row and the last name in a row under it
        print(f"First name: {first_name}\nLast name: {last_name}")
        # Here we show the grade average grade
        print("The average grade is:", average_of3courses)

        # if statement is used here to but a letter grade on the average
        if average_of3courses >= 90:
            print("The letter grade is: A")
        elif average_of3courses >= 80:
            print("The letter grade is: B")
        elif average_of3courses >= 70:
            print("The letter grade is: C")
        elif average_of3courses >= 60:
            print("The letter grade is: D")
        else:
            print("The letter grade is: F")
    # when user does not type a number
    except ValueError:
        print("Please choose a number!")   # 1. we print this message
        start()                            # 2. we run the function again

start()
