import os  # Module for interacting with the operating system
import time  # Module for time-related functions
from random import randint  # Function to generate random integers

class StudentManagementSystem:
    # Directory and file paths for storing student data
    DATA_DIR = "student_data"
    STUDENT_FILE = os.path.join(DATA_DIR, "students.txt")
    PASSWORD_FILE = os.path.join(DATA_DIR, "passwords.txt")
    SUBJECTS_FILE = os.path.join(DATA_DIR, "subjects.txt")
    SPORTS_FILE = os.path.join(DATA_DIR, "sports.txt")

    @classmethod
    def buildup(cls):
        """
        Create the data directory and necessary files if they do not already exist.
        """
        if not os.path.exists(cls.DATA_DIR):  # Check if the data directory exists
            os.makedirs(cls.DATA_DIR)  # Create the data directory if it does not exist
        # Create each file if it does not already exist
        for file in [cls.STUDENT_FILE, cls.PASSWORD_FILE, cls.SUBJECTS_FILE, cls.SPORTS_FILE]:
            if not os.path.exists(file):  # Check if the file exists
                with open(file, 'w') as f:  # Create the file
                    pass  # Do nothing, just ensure the file exists

    @classmethod
    def menu(cls):
        """
        Display the main menu and handle user input for navigating between Admin and Student options.
        """
        while True:  # Infinite loop to keep the menu running
            print("\nMain Menu")
            print("---------")
            print("1. Admin")
            print("2. Student")
            print("3. Exit")
            choice = input("Choose from above: ")  # Get user choice
            if choice == "1":  # If the user chooses Admin
                cls.admin()
            elif choice == "2":  # If the user chooses Student
                cls.student()
            elif choice == "3":  # If the user chooses Exit
                print("Exiting...")
                break  # Exit the loop and end the program
            else:
                print("Invalid choice, please try again.")  # Handle invalid input

    @classmethod
    def student(cls):
        """
        Display the student menu and handle user input for login, registration, and going back to the main menu.
        """
        while True:  # Infinite loop to keep the menu running
            print("\nStudent Menu")
            print("------------")
            print("1. Login")
            print("2. Register")
            print("3. Back to Main Menu")
            choice = input("Choose from above: ")  # Get user choice
            if choice == "1":  # If the user chooses Login
                cls.student_login()
            elif choice == "2":  # If the user chooses Register
                cls.student_register()
            elif choice == "3":  # If the user chooses to go back to the main menu
                break  # Exit the loop and return to the main menu
            else:
                print("Invalid choice, please try again.")  # Handle invalid input

    @classmethod
    def student_login(cls):
        """
        Handle student login by verifying credentials.
        """
        print("\nStudent Login")
        fname = input("Firstname: ")  # Get the student's first name
        student_id = input("ID: ")  # Get the student's ID
        password = input("Password: ")  # Get the student's password
        if cls.verify_student_login(student_id, password):  # Verify the login credentials
            cls.student_dashboard(fname, student_id)  # If valid, show the student dashboard
        else:
            print("Invalid details!")  # If invalid, show an error message

    @classmethod
    def student_register(cls):
        """
        Handle student registration by collecting details and saving them to the files.
        """
        print("\nStudent Registration")
        fname = input("Firstname: ")  # Get the student's first name
        lname = input("Lastname: ")  # Get the student's last name
        age = input("Age: ")  # Get the student's age
        gender = input("Gender: ")  # Get the student's gender
        subjects = input("Subjects (comma-separated): ")  # Get the subjects the student is taking
        student_id = str(randint(1000000, 9000000))  # Generate a random student ID
        password = input("Password: ")  # Get the student's password
        if all([fname, lname, age, gender, subjects, password]):  # Check if all fields are filled
            with open(cls.STUDENT_FILE, "a") as f:  # Append the student details to the student file
                f.write(f"{fname},{lname},{age},{gender},{student_id}\n")
            with open(cls.PASSWORD_FILE, "a") as f:  # Append the student ID and password to the password file
                f.write(f"{student_id},{password}\n")
            with open(cls.SUBJECTS_FILE, "a") as f:  # Append the student ID and subjects to the subjects file
                f.write(f"{student_id},{subjects}\n")
            print("Registration successful! Your ID is:", student_id)  # Confirm registration
        else:
            print("All fields are required!")  # Show an error message if any field is empty

    @classmethod
    def verify_student_login(cls, student_id, password):
        """
        Verify the student's login credentials.
        """
        with open(cls.PASSWORD_FILE, "r") as f:  # Open the password file for reading
            for line in f:  # Iterate through each line
                stored_id, stored_password = line.strip().split(',')  # Split the line into ID and password
                if stored_id == student_id and stored_password == password:  # Check if the credentials match
                    return True  # Return True if the credentials are valid
        return False  # Return False if the credentials are invalid

    @classmethod
    def student_dashboard(cls, fname, student_id):
        """
        Display the student dashboard with options to view details, add sports details, or logout.
        """
        while True:  # Infinite loop to keep the dashboard running
            print("\nStudent Dashboard")
            print("-----------------")
            print("1. View My Details")
            print("2. Add Sports Details")
            print("3. Logout")
            choice = input("Choose from above: ")  # Get user choice
            if choice == "1":  # If the user chooses to view details
                cls.show_student_details(student_id)
            elif choice == "2":  # If the user chooses to add sports details
                cls.add_sports_details(student_id)
            elif choice == "3":  # If the user chooses to logout
                break  # Exit the loop and return to the student menu
            else:
                print("Invalid choice, please try again.")  # Handle invalid input

    @classmethod
    def show_student_details(cls, student_id):
        """
        Display the student's details, including subjects and sports.
        """
        found = False  # Flag to check if the student is found
        with open(cls.STUDENT_FILE, "r") as f:  # Open the student file for reading
            for line in f:  # Iterate through each line
                details = line.strip().split(',')  # Split the line into details
                if details[4] == student_id:  # Check if the ID matches
                    print(f"\nFirstname: {details[0]}\nLastname: {details[1]}\nAge: {details[2]}\nGender: {details[3]}\nID: {details[4]}")
                    found = True  # Set the flag to True if the student is found
                    break  # Exit the loop
        if not found:  # If the student is not found
            print("Student could not be found!")  # Show an error message
        print("\nSubjects:")
        with open(cls.SUBJECTS_FILE, "r") as f:  # Open the subjects file for reading
            for line in f:  # Iterate through each line
                if line.startswith(student_id):  # Check if the line starts with the student ID
                    print(line.strip().split(',', 1)[1])  # Print the subjects
        print("\nSports:")
        with open(cls.SPORTS_FILE, "r") as f:  # Open the sports file for reading
            for line in f:  # Iterate through each line
                if line.startswith(student_id):  # Check if the line starts with the student ID
                    print(line.strip().split(',', 1)[1])  # Print the sports details

    @classmethod
    def add_sports_details(cls, student_id):
        """
        Add sports details for the student.
        """
        sports = input("Enter sports and time (e.g., Football 3-4 PM): ")  # Get sports details from the user
        with open(cls.SPORTS_FILE, "a") as f:  # Append the sports details to the sports file
            f.write(f"{student_id},{sports}\n")
        print("Sports details added!")  # Confirm the addition

    @classmethod
    def admin(cls):
        """
        Handle admin login by verifying credentials.
        """
        print("\nAdmin Login")
        username = input("Username: ")  # Get the admin username
        password = input("Password: ")  # Get the admin password
        if username == "Sujal" and password == "********":  # Check if the credentials are correct


            cls.admin_dashboard()  # If valid, show the admin dashboard
        else:
            print("Invalid admin details!")  # If invalid, show an error message

    @classmethod
    def admin_dashboard(cls):
        """
        Display the admin dashboard with options to view all students, add a new student, delete a student, or logout.
        """
        while True:  # Infinite loop to keep the dashboard running
            print("\nAdmin Dashboard")
            print("----------------")
            print("1. View All Students")
            print("2. Add New Student")
            print("3. Delete Student")
            print("4. Logout")
            choice = input("Choose from above: ")  # Get user choice
            if choice == "1":  # If the user chooses to view all students
                cls.view_all_students()
            elif choice == "2":  # If the user chooses to add a new student
                cls.add_new_student()
            elif choice == "3":  # If the user chooses to delete a student
                cls.delete_student()
            elif choice == "4":  # If the user chooses to logout
                break  # Exit the loop and return to the main menu
            else:
                print("Invalid choice, please try again.")  # Handle invalid input

    @classmethod
    def view_all_students(cls):
        """
        Display details of all students, including subjects and sports.
        """
        print("\nAll Students:")
        with open(cls.STUDENT_FILE, "r") as f:  # Open the student file for reading
            for line in f:  # Iterate through each line
                print(line.strip())  # Print the student details
        print("\nSubjects:")
        with open(cls.SUBJECTS_FILE, "r") as f:  # Open the subjects file for reading
            for line in f:  # Iterate through each line
                print(line.strip())  # Print the subjects
        print("\nSports:")
        with open(cls.SPORTS_FILE, "r") as f:  # Open the sports file for reading
            for line in f:  # Iterate through each line
                print(line.strip())  # Print the sports details

    @classmethod
    def add_new_student(cls):
        """
        Add a new student using the registration method.
        """
        cls.student_register()  # Call the student registration method

    @classmethod
    def delete_student(cls):
        """
        Delete a student by removing their details from all files.
        """
        student_id = input("Enter the ID of the student to delete: ")  # Get the student ID to delete
        cls._update_file(cls.STUDENT_FILE, student_id, exclude=True)  # Remove student details from student file
        cls._update_file(cls.PASSWORD_FILE, student_id, exclude=True)  # Remove student details from password file
        cls._update_file(cls.SUBJECTS_FILE, student_id, exclude=True)  # Remove student details from subjects file
        cls._update_file(cls.SPORTS_FILE, student_id, exclude=True)  # Remove student details from sports file
        print("Deleting student account...")  # Inform user about deletion
        time.sleep(2)  # Wait for 2 seconds to simulate processing time
        print("Student account deleted successfully!")  # Confirm deletion

    @classmethod
    def _update_file(cls, file_path, student_id, exclude=False):
        """
        Update a file by including or excluding lines that start with the given student ID.
        """
        with open(file_path, "r") as f:  # Open the file for reading
            lines = f.readlines()  # Read all lines into a list
        with open(file_path, "w") as f:  # Open the file for writing
            for line in lines:  # Iterate through each line
                if exclude:  # If excluding lines
                    if not line.startswith(student_id):  # Write the line if it does not start with the student ID
                        f.write(line)
                else:  # If including lines
                    f.write(line)  # Write the line

# Initialize the directories and files
StudentManagementSystem.buildup()
# Display the main menu
StudentManagementSystem.menu()