import os

# A constant for the name of the file that stores the user credentials
FILE_NAME = "users.txt"

def create_file_if_not_exists():
    try:
        # Create the file if it doesn't exist
        if not os.path.exists(FILE_NAME):
            with open(FILE_NAME, 'w'):
                pass
            print("File 'users.txt' created.")
    except IOError as e:
        # Print the details of the exception
        print(f"An error occurred while creating the file 'users.txt': {e}")

def register():
    # Ask the user for a username
    username = input("Please enter a username: ")

    # Check if the username already exists in the file
    if check_username(username):
        # Username already exists, ask the user to choose another one
        print("Sorry, this username is already taken. Please choose another one.")
        register()
    else:
        # Username is available, ask the user for a password
        password = input("Please enter a password: ")

        # Store the username and password in the file, separated by a comma
        try:
            with open(FILE_NAME, 'a') as file:
                # Write the username and password to the file, followed by a new line
                file.write(f"{username},{password}\n")
            # Display a success message
            print("You have successfully registered!")
        except IOError as e:
            # Print the details of the exception
            print(f"An error occurred while registering: {e}")
            # An error occurred while writing to the file
            print("An error occurred while registering. Please try again.")

def login():
    # Ask the user for a username
    username = input("Please enter your username: ")

    # Check if the username exists in the file
    if check_username(username):
        # Username exists, ask the user for a password
        password = input("Please enter your password: ")

        # Check if the password matches the username in the file
        if check_password(username, password):
            # Password matches, display a success message
            print("You have successfully logged in!")
        else:
            # Password does not match, display an error message
            print("Incorrect password. Please try again.")
    else:
        # Username does not exist, display an error message
        print("This username does not exist. Please register first.")

def check_username(username):
    # Create a boolean variable to store the result
    exists = False

    try:
        # Open the file and check if the username exists
        with open(FILE_NAME, 'r') as file:
            # Read all lines from the file
            lines = file.readlines()
            # Check if the username exists in any line
            exists = any(line.split(',')[0] == username for line in lines)
    except IOError as e:
        # Print the details of the exception
        print(f"An error occurred while checking the username: {e}")
        # An error occurred while reading from the file
        print("An error occurred while checking the username. Please try again.")

    # Return the result
    return exists

def check_password(username, password):
    # Create a boolean variable to store the result
    matches = False

    try:
        # Open the file and check if the password matches
        with open(FILE_NAME, 'r') as file:
            # Read all lines from the file
            lines = file.readlines()
            # Check if the username and password match in any line
            matches = any(line.split(',')[0] == username and line.split(',')[1].strip() == password for line in lines)
    except IOError as e:
        # Print the details of the exception
        print(f"An error occurred while checking the password: {e}")
        # An error occurred while reading from the file
        print("An error occurred while checking the password. Please try again.")

    # Return the result
    return matches

def main():
    # Check if the users.txt file exists, create it if it doesn't
    create_file_if_not_exists()

    # Display a menu with two options: register or login
    print("Welcome to the LogIn program!")
    print("Please choose an option:")
    print("1. Register")
    print("2. Login")
    print("3. Exit")

    # Read the user's choice
    choice = int(input())

    # Perform the corresponding action based on the user's choice
    if choice == 1:
        # Register a new user
        register()
    elif choice == 2:
        # Login an existing user
        login()
    elif choice == 3:
        # Exit the program
        print("Thank you for using the LogIn program!")
    else:
        # Invalid choice
        print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()
