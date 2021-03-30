"""
A script to calculate swimming pool volume, area of square and circle
"""

def calculateSwimmingPoolVolume():
    try:      # try and except are used here to make sure we do not face errors if user did not enter a number
        print("To calculate your swimming pool volume please enter the following values")
        length = float(input("Length in m: "))    # user length input in centimeters
        width = float(input("Width in m: "))      # user width input in centimeters
        depth = float(input("Depth in m: "))      # user depth input in centimeters

        swimmingPoolVolume = length*width*depth      # Swimming pool formula ( L * W * D )
        volumeInLiters = swimmingPoolVolume * 1000   # To convert meters into liters we have to multiple by 1000
        print("This is how much water your swimming pool can take:", volumeInLiters, "L")
    except ValueError:
        print("Please choose a number!")
        calculateSwimmingPoolVolume()  # we call the def again because the user did not enter a number

def calculateAreaOfSquare():
    try:    # try and except are used here to make sure we do not face errors if user did not enter a number
        print("To calculate the area of a square please enter the following value")
        side = float(input(" Side of the square in cm: "))    # user input for the side of a square in centimeters
        area = side**2           # Formula of area of square is ( A=a**2 )
        areaInMeter = area/100   # To convert cm into meters we have to divide by 100
        print("The area of the square is:", areaInMeter, "m")
    except ValueError:
        print("Please choose a number!")
        calculateAreaOfSquare()    # we call the def again because the user did not enter a number

def calculateAreaOfCircle():
    try:   # try and except are used here to make sure we do not face errors if user did not enter a number
        print("To calculate the area of the circle please enter the following value")
        radius = float(input("Radius in cm: "))    # user input for the radius of a circle in centimeters
        area = 3.14 * radius**2  # Formula of the area of a circle is ( Pi * r**2 )
        areaInMeter = area/100   # To convert cm into meters we have to divide by 100
        print("the area of the circle is:", areaInMeter, "m")
    except ValueError:
        print("Please choose a number!")
        calculateAreaOfCircle()   # we call the def again because the user did not enter a number

def run():
    start = input("What type of calculation do you want?: ")
    if start == "1":                       # if user enters 1
        calculateSwimmingPoolVolume()      # we run the swimming pool formula
        runAgain()                         # after the calculation we ask if the user to run another task
    elif start == "2":                     # if user enters 2
        calculateAreaOfSquare()            # we run the area of square formula
        runAgain()                         # after the calculation we ask if the user to run another task
    elif start == "3":                     # if user enters 3
        calculateAreaOfCircle()            # we run the area of circle formula
        runAgain()                         # after the calculation we ask if the user to run another task
    else:
        print("Please enter a value between 1 and 3") # if user does not enter a correct value
        run()                                         # we ask again
def runAgain():
    # if statement to ask the user wants to calculation again
    again = input("Would you like to calculate another task? Yes or No: ").lower() # all input lower case
    if again == "yes":      # if user chooses yes
        run()               # we run() again "What type of calculation do you want?: "
    elif again == "no":     # if user chooses no
        print("Thank you and goodbye!")  # print and end
    else:                   # if user does not chooses yes or no
        runAgain()          # we ask again "Would you like to calculate another task? Yes or No: "
print("""
Choose one of the numbers below:

1. Calculate the water volume in a swimming pool
2. Calculate the area of a square
3. Calculate the area of a circle
""")
run()
