while True:

    print("\n===== STUDENT DATA ORGANIZER =====")
    print("1. Add Student")
    print("2. Display Students")
    print("3. Update Student Age")
    print("4. Delete Student")
    print("5. Display Subjects")
    print("6. Exit")

    choice = input("Enter Choice : ")

    # Add Student
    if choice == "1":

        sid = input("Enter Student ID : ")
        dob = input("Enter DOB : ")

        details = (sid, dob)   # Tuple

        name = input("Enter Name : ")
        age = int(input("Enter Age : "))   # Type Casting
        grade = input("Enter Grade : ")

        subject_input = input("Enter Subjects : ")
        subjects = subject_input.split(",")

        # Set
        for sub in subjects:
            subjects_set.add(sub)

        # Dictionary
        student = {
            "details": details,
            "name": name,
            "age": age,
            "grade": grade,
            "subjects": subjects
        }

        # List
        students.append(student)

        print("Student Added Successfully.")

    # Display Students
    elif choice == "2":

        if len(students) == 0:
            print("No Student Found.")

        else:
            for student in students:

                print("\n-----------------------")
                print("Student ID :", student["details"][0])
                print("DOB        :", student["details"][1])
                print("Name       :", student["name"])
                print("Age        :", student["age"])
                print("Grade      :", student["grade"])
                print("Subjects   :", student["subjects"])

    # Update Age
    elif choice == "3":

        sid = input("Enter Student ID : ")

        for student in students:

            if student["details"][0] == sid:

                new_age = int(input("Enter New Age : "))
                student["age"] = new_age

                print("Age Updated Successfully.")

    # Delete Student
    elif choice == "4":

        sid = input("Enter Student ID : ")

        for i in range(len(students)):

            if students[i]["details"][0] == sid:

                del students[i]   # del keyword

                print("Student Deleted.")
                break

    # Display Subjects
    elif choice == "5":

        print("\nSubjects Offered :")

        for sub in subjects_set:
            print(sub)

    # Exit
    elif choice == "6":

        print("Thank You For Using Student Data Organizer.")
        break

    else:
        print("Invalid Choice.")
