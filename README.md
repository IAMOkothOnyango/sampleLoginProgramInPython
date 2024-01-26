# SampleLogIn Program (Python)

The **SampleLogIn** program is a simple Python script that enables users to register new accounts with a username and password or log in to existing accounts. User credentials are stored in a text file (`users.txt`). The program utilizes basic file I/O operations to manage user registration and authentication.

## Features

- **Registration:** Users can register by providing a unique username and a password.
- **Login:** Existing users can log in by entering their username and password.
- **Data Storage:** User credentials are stored in a text file (`users.txt`) separated by commas.

## Usage

1. **Run the Program:**
   - Execute the Python script:
     ```bash
     python SampleLogIn.py
     ```

2. **Follow the Menu:**
   - Upon running the program, users are presented with a menu offering three options:
     - **1. Register:** Allows users to create a new account.
     - **2. Login:** Allows existing users to log in.
     - **3. Exit:** Terminates the program.

3. **Registration:**
   - Choose option `1` to register a new account.
   - Enter a unique username when prompted.
   - If the chosen username is available, enter a password.

4. **Login:**
   - Choose option `2` to log in with an existing account.
   - Enter your username and password when prompted.

5. **Exiting:**
   - Choose option `3` to exit the program.

## File Structure

- **users.txt:** The file used to store user credentials. Each line contains a username and password separated by a comma.

## Error Handling

- The program provides basic error handling for file I/O operations.
- Error messages are displayed if issues occur during user registration, login, or file creation.

## Notes

- Ensure that Python is installed on your system to run the program.
- The script can be executed in any Python environment.

## Sample Execution

Here's a sample execution of the program:

```
Welcome to the LogIn program!
Please choose an option:
1. Register
2. Login
3. Exit

1
Please enter a username: user123
Please enter a password: pass123
You have successfully registered!

Welcome to the LogIn program!
Please choose an option:
1. Register
2. Login
3. Exit

2
Please enter your username: user123
Please enter your password: pass123
You have successfully logged in!
```

Feel free to explore and modify the script to suit your needs. If you encounter any issues or have suggestions for improvement, please refer to the error messages or check the source code for guidance.
