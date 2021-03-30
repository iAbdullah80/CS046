"""
HomeWork 03
Build a system that can manage students data
"""


class StudentsManagement:  # First we create a class

    # This is the constructor
    def __init__(self, student_name, student_id, student_major, student_course1, student_grade1, student_course2,
                 student_grade2, student_course3, student_grade3):  # We have 5 parameters
        self.student_name = student_name  # for the student name
        self.student_id = student_id  # for the student ID number
        self.student_major = student_major  # for the student major
        self.student_course1 = student_course1  # for the student first course
        self.student_grade1 = student_grade1  # for the student first grade
        self.student_course2 = student_course2  # for the student second course
        self.student_grade2 = student_grade2  # for the student second grade
        self.student_course3 = student_course3  # for the student third course
        self.student_grade3 = student_grade3  # for the student third grade

    # Here we have a display function with one parameter which is every i in range(list.__len__()
    def display_student(self, student):
        print("\nStudent name: ", student.student_name)  # display student name
        print("ID: ", student.student_id)  # display student ID number
        print("Major: ", student.student_major)  # display student major
        print(" 1. First Course: ", student.student_course1)  # display student first course
        print(" Grade: ", student.student_grade1)  # display student first grade
        print(" 2. Second Course: ", student.student_course2)  # display student second course
        print(" Grade: ", student.student_grade2)  # display student second grade
        print(" 3. Third Course: ", student.student_course3)  # display student third course
        print(" Grade: ", student.student_grade3)  # display student third grade
        print("")

    # Here we have an add function and it includes 9 parameters its the student name, id, major, courses and grades
    def add(self, student_name, student_id, student_major, student_course1, student_grade1, student_course2,
            student_grade2, student_course3, student_grade3):
        # We store the new student information here in (student_info)
        student_info = StudentsManagement(student_name, student_id, student_major, student_course1, student_grade1,
                                          student_course2, student_grade2, student_course3, student_grade3)
        list.append(student_info)  # after storing the new student information, we add it to the list by .append

    # Here we have the search function it has one parameter which is the student ID because its unique
    def search(self, id_of_student):
        for i in range(list.__len__()):  # we search for every value in the list range
            if list[i].student_id == id_of_student:  # if the student id that we passed in the parameter exist
                return i  # we store its place so we can passe it to the display func

    # Here we have a function that has 2 parameters to update a student name
    def update_name(self, student_id, new_student):
        stud = obj.search(student_id)  # We search for the student by his student id
        list[stud].student_name = new_student  # after finding the student we replace his old name with a new one

    # Here we have a function that has 2 parameters to update a student id
    def update_id(self, student_id, new_id):
        stud = obj.search(student_id)  # We search for the student by his student id
        list[stud].student_id = new_id  # after finding the student we replace his old id with a new one

    # Here we have a function that has 2 parameters to update a student id
    def update_major(self, student_id, new_major):
        stud = obj.search(student_id)  # We search for the student by his student id
        list[stud].student_major = new_major  # after finding the student we replace his old major with a new one

    # Here we have a function that has 2 parameters to update a student first course
    def update_course1(self, student_id, new_course1):
        stud = obj.search(student_id)  # We search for the student by his student id
        list[stud].student_course1 = new_course1  # after finding the student we replace his old course with a new one

    # Here we have a function that has 2 parameters to update a student first grade
    def update_grade1(self, student_id, new_grade1):
        stud = obj.search(student_id)  # We search for the student by his student id
        list[stud].student_grade1 = new_grade1  # after finding the student we replace his old grade with a new one

    # Here we have a function that has 2 parameters to update a student second course
    def update_course2(self, student_id, new_course2):
        stud = obj.search(student_id)  # We search for the student by his student id
        list[stud].student_course2 = new_course2  # after finding the student we replace his old course with a new one

    # Here we have a function that has 2 parameters to update a student second grade
    def update_grade2(self, student_id, new_grade2):
        stud = obj.search(student_id)  # We search for the student by his student id
        list[stud].student_grade2 = new_grade2  # after finding the student we replace his old grade with a new one

    # Here we have a function that has 2 parameters to update a student third course
    def update_course3(self, student_id, new_course3):
        stud = obj.search(student_id)  # We search for the student by his student id
        list[stud].student_course3 = new_course3  # after finding the student we replace his old course with a new one

    # Here we have a function that has 2 parameters to update a student third grade
    def update_grade3(self, student_id, new_grade3):
        stud = obj.search(student_id)  # We search for the student by his student id
        list[stud].student_grade3 = new_grade3  # after finding the student we replace his old grade with a new one

    # Here we have a function that accepts one parameter to delete a student from the list
    def delete(self, id_student):
        stud = obj.search(id_student)  # We search for the student by his student id
        del list[stud]  # after finding the student we delete all of his information


# Executing Functions!

# This function is for executing the display function
def show():
    print("\nList of the students: \n")
    for i in range(list.__len__()):  # for every value in the list
        obj.display_student(list[i])  # display all values
    ask()  # ask the user if he wants to continue or not


# This function is for executing the add function
def new():
    print("Enter the following values")
    try:  # use try to make sure no runtime errors happen
        name = (input("Full name: "))  # ask the user for the student name
        ID = int(input("Student ID: "))  # ask the user for the student id
        major = input("Student major: ")  # ask the user for the student major
        course1 = input("First Course: ")  # ask the user for the student first course
        grade1 = int(input("Course grade: "))  # ask the user for the student first grade
        course2 = input("Second Course: ")  # ask the user for the student second course
        grade2 = int(input("Course grade: "))  # ask the user for the student second grade
        course3 = input("Third Course: ")  # ask the user for the student third course
        grade3 = int(input("Course grade: "))  # ask the user for the student third grade
    except ValueError:  # if an error happens
        print("Wrong value")
        new()  # run he fun again
    else:
        # passe the variables to the add function as actual parameters (coupling) to add as a new student
        obj.add(name, ID, major, course1, grade1, course2, grade2, course3, grade3)
        for i in range(list.__len__()):  # for every value in the list
            obj.display_student(list[i])  # show the students list after adding
        ask()  # ask the user if he wants to continue or not


# This function is for executing the update function
def updateStudent():
    while True:
        # ask the user what he wants to update
        print("""
        What do you want to update?
        1. Update the full name
        2. Update the ID number
        3. Update the major
        4. Update the courses
        5. Update the grades
        6. Go back
        
        """)
        try:  # if user input dose not exist we use try to make sure we don't have any runtime errors
            num = int(input("Enter a number: "))  # ask the user to enter a number

            # if the user chooses 1 that means (Update the full name)
            if num == 1:
                print("To find the student you want to change his name, enter the following value")
                studentID = int(input("Student ID number: "))  # ask for the id
                look = obj.search(studentID)  # search for the student by the id
                obj.display_student(list[look])  # show the user the student that he wants to update
                name = input("New student name: ")  # ask the user to write the new student name
                obj.update_name(studentID, name)  # passe the variables to the update_name function as actual parameters
                for i in range(list.__len__()):  # for every value in the list
                    obj.display_student(list[i])  # show the students list after the update
                print("Updated successfully!")
                updateStudent()  # run the function again to see if the user want to update more

            # if the user chooses 2 that means (Update the ID number)
            elif num == 2:
                print("To find the student you want to change his ID number, enter the following value")
                studentID = int(input("Student ID number: "))  # ask for the id
                look = obj.search(studentID)  # search for the student by the id
                obj.display_student(list[look])  # show the user the student that he wants to update
                id = int(input("New ID number: "))  # ask the user to write the new student id
                obj.update_id(studentID, id)  # passe the variables to the update_id function as actual parameters
                for i in range(list.__len__()):  # for every value in the list
                    obj.display_student(list[i])  # show the students list after the update
                print("Updated successfully!")
                updateStudent()  # run the function again to see if the user want to update more

            # if the user chooses 3 that means (Update the major)
            elif num == 3:
                print("To find the student you want to change his major, enter the following value")
                studentID = int(input("Student ID number: "))  # ask for the id
                look = obj.search(studentID)  # search for the student by the id
                obj.display_student(list[look])  # show the user the student that he wants to update
                major = input("New major: ")  # ask the user to write the new major
                obj.update_major(studentID, major)  # passe the variables to the update_major func
                for i in range(list.__len__()):  # for every value in the list
                    obj.display_student(list[i])  # show the students list after the update
                print("Updated successfully!")
                updateStudent()  # run the function again to see if the user want to update more

            # if the user chooses 4 that means (Update the courses)
            elif num == 4:
                print("To find the student you want to change his courses, enter the following value")
                studentID = int(input("Student ID number: "))  # ask for the id
                look = obj.search(studentID)  # search for the student by the id
                obj.display_student(list[look])  # show the user the student that he wants to update
                print("What course do you want to update?")  # the courses are numbered so the user has to pick one
                course = int(input("choose a number: "))  # ask the user to pick a course to change
                if course == 1:  # if the user chooses 1 update the first course
                    course1 = input("Enter new course name: ")  # ask to write the new course
                    obj.update_course1(studentID, course1)  # passe the variables to the update_course1 func
                    for i in range(list.__len__()):  # for every value in the list
                        obj.display_student(list[i])  # show the students list after the update
                    print("Updated successfully!")
                    updateStudent()
                elif course == 2:  # if the user chooses 2 update the second course
                    course2 = input("Enter new course name: ")  # ask to write new course
                    obj.update_course2(studentID, course2)  # passe the variables to the update_course2 func
                    for i in range(list.__len__()):  # for every value in the list
                        obj.display_student(list[i])  # show the students list after the update
                    print("Updated successfully!")
                    updateStudent()
                elif course == 3:  # if the user chooses 3 update the third course
                    course3 = input("Enter new course name: ")  # ask to write the new course
                    obj.update_course3(studentID, course3)  # passe the variables to the update_course3 func
                    for i in range(list.__len__()):  # for every value in the list
                        obj.display_student(list[i])  # show the students list after the update
                    print("Updated successfully!")
                    updateStudent()
                else:  # if the user didn't choose a number between 1-3
                    print("Wrong value!")
                    updateStudent()  # run the updateStudent func

            # if the user chooses 5 that means (Update the grades)
            elif num == 5:
                print("To find the student you want to change his grades, enter the following value")
                studentID = int(input("Student ID number: "))  # ask for the id
                look = obj.search(studentID)  # search for the student by the id
                obj.display_student(list[look])  # show the user the student that he wants to update
                print(
                    "What course grade do you want to update?")  # the courses are numbered so the user has to pick one
                grade = int(input("choose a number: "))  # ask the user to pick a course grade to change
                if grade == 1:  # if the user chooses 1 update the first course grade
                    grade1 = int(input("Enter new grade: "))  # ask to write the new course grade
                    obj.update_grade1(studentID, grade1)  # passe the variables to the update_grade1 func
                    for i in range(list.__len__()):  # for every value in the list
                        obj.display_student(list[i])  # show the students list after the update
                    print("Updated successfully!")
                    updateStudent()
                elif grade == 2:  # if the user chooses 2 update the second course grade
                    grade2 = int(input("Enter new grade: "))  # ask to write the new course grade
                    obj.update_grade2(studentID, grade2)  # passe the variables to the update_grade2 func
                    for i in range(list.__len__()):  # for every value in the list
                        obj.display_student(list[i])  # show the students list after the update
                    print("Updated successfully!")
                    updateStudent()
                elif grade == 3:  # if the user chooses 3 update the third course grade
                    grade3 = int(input("Enter new grade: "))  # ask to write the new course grade
                    obj.update_grade3(studentID, grade3)  # passe the variables to the update_grade3 func
                    for i in range(list.__len__()):  # for every value in the list
                        obj.display_student(list[i])  # show the students list after the update
                    print("Updated successfully!")
                    updateStudent()
                else:  # if the user didn't choose a number between 1-3
                    print("Wrong value!")
                    updateStudent()  # run the updateStudent func

            # if the user chooses 6
            elif num == 6:
                main()  # go back to the main()

        except ValueError:  # if the user encounters value error
            print("Wrong ID number")
            updateStudent()
        except TypeError:  # if the user encounters type error
            print("Wrong ID number")
            updateStudent()


def lookFor():  # This function is for executing the search function
    global studentID
    print("Write the ID number of the student you are looking for")
    try:
        studentID = int(input("Student ID: "))  # ask the user for the student id that he is looking for
    except ValueError:
        print("Wrong ID number")
        lookFor()

    look = obj.search(studentID)  # passe it to the search function
    obj.display_student(list[look])  # we passe the value that we got from searching to the display function
    ask()  # ask the user if he wants to continue or not


def remove():  # This function is for executing the delete function
    global deleteStudent
    print("Write the ID number of the student you want to delete")
    try:
        deleteStudent = int(input("Student ID: "))  # ask the user for the student id that he is looking for
    except ValueError:
        print("Wrong ID number")
        remove()

    obj.delete(deleteStudent)  # passe the student id to the delete function
    print("list after deleting")
    for i in range(list.__len__()):
        obj.display_student(list[i])  # show the list after deleting
    ask()  # ask the user if he wants to continue or not


# This is the main function where we start from and choose what we want to do
def main():
    global choose
    print("""
    What would you like to do?
    1. Show all students and their information
    2. Add a new student
    3. Update an existing student
    4. Search for a student
    5. Delete a student
    6. Exit
    """)

    try:
        choose = int(input("Enter a number: "))
    except ValueError:
        print("Please choose a number between 1 and 6")
        main()

    if choose == 1:  # if the user chooses 1 (Show all students and their information)
        show()  # execute the show func

    elif choose == 2:  # if the user chooses 2 (Add a new student)
        new()  # execute the new func

    elif choose == 3:  # if the user chooses 3 (Update an existing student)
        updateStudent()  # execute the updateStudent func

    elif choose == 4:  # if the user chooses 4 (Search for a student)
        lookFor()  # execute the lookFor func

    elif choose == 5:  # if the user chooses 5 (Delete a student)
        remove()  # execute the remove func

    elif choose == 6:  # if the user chooses 6 (Exit)
        print("Thank you and goodbye!")
        exit()

    else:  # if the user chooses wrong number
        print("Please choose a number between 1 and 6")  # print this statement
        main()  # Run the main again


# This is the ask function to ask the user if he wants to continue or nor
def ask():
    while True:
        ask = input("Do you want to do another action? (yes or no): ")  # ask the user for yes or no
        if ask == "yes":  # if yes
            main()  # run the main again
        elif ask == "no":  # if no
            print("Thank you and goodbye!")
            exit()  # end the program


list = []  # create an empty list

obj = StudentsManagement("", 0, "", "", 0, "", 0, "", 0)

# add two students from the start
obj.add("Abdularhman Alsanad", 442017108, "Computer science", "Math", 99, "Geology", 88, "Biology", 90)
obj.add("Waleed Alali", 442017275, "Computer science", "Physics", 80, "English", 100, "CS046", 60)

main()  # EXECUTE!

"""
Writen by 
Abdullah Alahideb (442019225) عبدالله الاحيدب

"""
