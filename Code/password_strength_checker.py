import getpass
import string
import time


# The password variable is set to GLOBAL for easier access by EVERY function.
password = ''


# Takes the user-given password to start the procedure
def user_input():
    global password
    # Hides input for security.
    password = getpass.getpass("Enter your password: ")
    print("Password received. Strength checking procedure has begun . . .")  


# Checks each character that the password contains
def analyze_password():
    # List containing all UPPERCASE letters
    uppercase_letters_list = list(string.ascii_uppercase)
    # List containing all LOWERCASE letters
    lowercase_letters_list = list(string.ascii_lowercase)
    # List containing SPECIAL characters
    special_characters_list = list(string.punctuation)
    # List containing all NUMBERS
    numbers_list = list(string.digits)

    has_special = False  # Flag for special character.
    has_upper = False    # Flag for uppercase letter.
    has_lower = False    # Flag for lowercase letter.
    has_number = False   # Flag for number.

    # Looping through the password to change flags.
    for char in password:
        if char in uppercase_letters_list:
            has_upper = True
        
        if char in lowercase_letters_list:
            has_lower = True
        
        if char in numbers_list:
            has_number = True
        
        if char in special_characters_list:
            has_special = True
    
    return has_upper, has_lower, has_special, has_number

    # Checking if the password meets the conditions
    #if has_upper and has_lower and has_special and has_number:
        #print("System message: The password is correct!")
    #elif has_upper == False:
        #print("System message: No uppercase letter!")
    #elif has_lower == False:
        #print("System message: No lowercase letter!")
    #elif has_number == False:
        #print("System message: No number!")
    #elif has_special == False:
        #print("System message: No special character!")


# Checks the password's length and returns True if length is acceptable
def length_checking():
    # Get the password's length
    length = len(password)

    # Get character type presence flags
    has_upper, has_lower, has_special, has_number = analyze_password()

    # Checks the length of the password.
    if length < 8:
        print("System Message: The password is too short!")
        # Stop the process if the password is too short
        return False  
    
    elif 8 <= length < 15:
        if has_upper and has_lower and has_number and has_special:
            print("System Message: The password is correct!")
        else:
            print("System Message: The password is incorrect!")
        return True    
    
    else:
        print("ARE YOU WRITING AN ESSAY OR A PASSWORD?")
        # Stop checking the password if it's sufficiently long
        return False


# Starts the visually loading process
def loading():
    for i in range(0, 101, 10):
        print(f"{i}%", end=" ", flush=True)
        # To slow down the printing, simulating loading
        time.sleep(0.5)  
    print()
    print("Loading Complete")


# Main
if __name__ == "__main__":
    print("============================================================")
    print("For security reasons, your password will NOT be displayed!")
    user_input()
    loading()
    length_checking()
    print("============================================================")