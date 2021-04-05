"""
HomeWork 04
Build a system can do some Physics
"""


def physics_cal():  # Create one function called physics_cal as required
    print("""
    What operation do you want to do?

    1. Speed Formula
    2. Time Formula
    3. Acceleration Formula
    4. Final Speed Formula
    5. Exit
    """)
    # while true is here to allow us to navigate between the 4 formulas
    while True:
        num = input("Enter a number: ")  # ask for a number

        # if user enters 1 calculate the Speed Formula
        if num == "1":

            # here we have a while true to ask the user in what measurement unit does he wants to calculate
            while True:
                try:
                    print(""" 
                            In what unit measurement do you want to calculate the Speed?
                            1. km/h
                            2. m/s """)
                    ask_measurement = input("Choose a number: ")  # ask to enter a value

                    # if the user enters 1 the result would by in km/h
                    if ask_measurement == "1":
                        distance = float(input("Enter Distance (in km): "))  # ask for the distance in km
                        time = float(input("Enter Time (in h): "))  # ask for the tim in h
                        speed = distance / time  # here we do the math! the speed formula is ( s = d/t )
                        print("The average speed is: ", speed, " km/h")  # show the result
                        break

                    # if the user enters 2 the result would by in m/s
                    elif ask_measurement == "2":
                        distance = float(input("Enter Distance (in m): "))  # ask for the distance in m
                        time = float(input("Enter Time (in s): "))  # ask for the tim in s
                        speed = distance / time  # here we do the math! the speed formula is ( s = d/t )
                        print("The average speed is: ", speed, " m/s")  # show the result
                        break
                    else:
                        print("Wrong value!")
                except ValueError:
                    print("Numbers only!")

            # we wrote while true here to ask the user if he wants to continue or not
            while True:
                print("\nDo you want to do another operation? ")
                ask = input("Choose (yes or no): ")
                if ask == "yes":  # if the user writes yes
                    physics_cal()  # run the function again
                elif ask == "no":  # if the user says no
                    exit()  # exit the program
                else:
                    print("Wong value!")

        # if user enters 2 calculate the Time Formula
        elif num == "2":

            # here we have a while true to ask the user in what measurement unit does he wants to calculate
            while True:
                try:
                    print(""" 
                            In what measurement unit do you want to calculate the Time?
                            1. h (Hour)
                            2. s (Second)""")
                    ask_measurement = input("Choose a number: ")  # ask to enter a value

                    # if the user enters 1 the result would by in h
                    if ask_measurement == "1":
                        distance = float(input("Enter Distance (in km): "))  # ask for the distance in km
                        speed = float(input("Enter Speed (km/h): "))  # ask for the speed in km/h
                        time = distance / speed  # here we do the math! the time formula is ( t = d/s )
                        print("The time is: ", time, " h")  # show the result
                        break

                    # if the user enters 2 the result would by in s
                    elif ask_measurement == "2":
                        distance = float(input("Enter Distance (in m): "))  # ask for the distance in m
                        speed = float(input("Enter Speed (m/s): "))  # ask for the speed in m/s
                        time = distance / speed  # here we do the math! the time formula is ( t = d/s )
                        print("The time is: ", time, " s")  # show the result
                        break
                    else:
                        print("Wrong value!")

                except ValueError:
                    print("Numbers only!")

            # we wrote while true here to ask the user if he wants to continue or not
            while True:
                print("\nDo you want to do another operation? ")
                ask = input("Choose (yes or no): ")
                if ask == "yes":  # if the user writes yes
                    physics_cal()  # run the function again
                elif ask == "no":  # if the user says no
                    exit()  # exit the program
                else:
                    print("Wong value!")

        # if user enters 3 calculate the Acceleration Formula
        elif num == "3":

            # here we have a while true to ask the user in what measurement unit does he wants to calculate
            while True:
                try:
                    print(""" 
                            In what measurement unit do you want to calculate the Acceleration?
                            1. km/h^2
                            2. m/s^2""")
                    ask_measurement = input("Choose a number: ")  # ask to enter a value

                    # if the user enters 1 the result would by in km/h^2
                    if ask_measurement == "1":
                        final_speed = float(input("Enter the final velocity (in km/h): "))  # in km/h
                        initial_speed = float(input("Enter the initial velocity (in km/h): "))  # in km/h
                        time = float(input("Enter the total time taken (in h): "))  # ask the user for time in h
                        acceleration = (final_speed - initial_speed) / time  # the formula is (a = vf - vi /t)
                        print("The acceleration is:", acceleration, " km/h^2")  # show the result in km/h^2
                        break

                    # if the user enters 2 the result would by in m/s^2
                    elif ask_measurement == "2":
                        final_speed = float(input("Enter the final velocity (in m/s): "))  # in m/s
                        initial_speed = float(input("Enter the initial velocity (in m/s): "))  # in m/s
                        time = float(input("Enter the total time taken (in s): "))  # ask the user for time in s
                        acceleration = (final_speed - initial_speed) / time  # the formula is (a = vf - vi /t)
                        print("The acceleration is:", acceleration, " m/s^2")  # show the result in m/s^2
                        break

                    else:
                        print("Wrong value!")

                except ValueError:
                    print("Numbers only!")

            # we wrote while true here to ask the user if he wants to continue or not
            while True:
                print("\nDo you want to do another operation? ")
                ask = input("Choose (yes or no): ")
                if ask == "yes":  # if the user writes yes
                    physics_cal()  # run the function again
                elif ask == "no":  # if the user says no
                    exit()  # exit the program
                else:
                    print("Wong value!")

        # if user enters 4 calculate the Final Speed Formula
        elif num == "4":

            # here we have a while true to ask the user in what measurement unit does he wants to calculate
            while True:
                try:  # try here to make sure no errors happen
                    print(""" 
                            In what measurement unit do you want to calculate the Final Speed?
                            1. km/h
                            2. m/s""")
                    ask_measurement = input("Choose a number: ")  # ask to enter a value

                    # if the user enters 1 the result would by in km/h
                    if ask_measurement == "1":
                        acceleration = float(input("Enter acceleration (in km/h^2"))  # ask for acceleration in km/h^2
                        time = float(input("Enter the total time taken (in h): "))  # ask the user for time in h
                        initial_speed = float(input("Enter the initial velocity (in km/h): "))  # initial speed in km/h
                        final_speed = (acceleration * time) + initial_speed  # final speed formula is (vf = (a * t)+vi)
                        print("The Final Speed is:", final_speed, " km/h")  # show the result
                        break

                    # if the user enters 2 the result would by in m/s
                    elif ask_measurement == "2":
                        acceleration = float(input("Enter acceleration (in m/s^2"))  # ask for acceleration in m/s^2
                        time = float(input("Enter the total time taken (in s): "))  # ask the user for time in s
                        initial_speed = float(input("Enter the initial velocity (in m/s): "))  # initial speed in m/s
                        final_speed = (acceleration * time) + initial_speed  # final speed formula is (vf = (a * t)+vi)
                        print("The Final Speed is:", final_speed, " m/s")  # show the result
                        break
                    else:
                        print("Wrong value!")

                except ValueError:  # when error happens
                    print("Numbers only!")  # print this statement and go back to the while loop above

            # we wrote while true here to ask the user if he wants to continue or not
            while True:
                print("\nDo you want to do another operation? ")
                ask = input("Choose (yes or no): ")
                if ask == "yes":  # if the user writes yes
                    physics_cal()  # run the function again
                elif ask == "no":  # if the user says no
                    exit()  # exit the program
                else:
                    print("Wong value!")

        # if the user chooses 5 then exit the program
        elif num == "5":
            break # break the while loop and end program

        # if the user enters wrong value go back throw the while loop
        else:
            print("Wrong value!")

# EXECUTE!!!
physics_cal()

"""
Writen by 
Abdullah Alahideb (442019225) عبدالله الاحيدب

Practice makes perfect (;
"""
