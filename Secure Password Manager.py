# ---------------------------------------------
# Secure Password Manager Application
# ---------------------------------------------
# This program allows users to:
# 1. Add a new account: Store the account name, username, and password.
# 2. View all stored accounts: Display all stored account names (but NOT passwords).
# 3. Retrieve a password: Retrieve the username and password for a specific account.
# 4. Update an account's password: Change the password for an account.
# 5. Remove an account: Delete an account from the manager.
# 6. Quit the program: Exit the app.
# ---------------------------------------------

import json

# Dictionary to store accounts
accounts = {}

# ---------------------------------------------
# Function to Add a New Account
# ---------------------------------------------

def add_account():
    """
    Adds a new account with a username and password.
    """
    while True:
        username = input("Enter a username: ").strip()
        
        if not username:
            print("Error: Username cannot be empty. Please try again.")
            continue

        if username in accounts:
            print("This username already exists! Please choose another.")
            continue

        password = input("Enter a password: ").strip()
        if not password:
            print("Error: Password cannot be empty. Please try again.")
            continue

        accounts[username] = password
        print(f"Account '{username}' has been stored successfully!")
        break

# ---------------------------------------------
# Function to View Stored Accounts
# ---------------------------------------------

def view_accounts():
    """
    Displays all stored account names.
    """
    if not accounts:
        print("\nNo accounts stored.")
    else:
        print("\nStored Accounts:")
        print("-" * 20)
        for i, username in enumerate(accounts.keys(), start=1):
            print(f"{i}. {username}")
        print("-" * 20)

# ---------------------------------------------
# Function to Retrieve a Password
# ---------------------------------------------

def retrieve_password():
    """
    Retrieves the password for a specific account.
    """
    try:
        if not accounts:
            print("No accounts available to retrieve.")

        username = input("Enter the account name: ").strip()

        if username not in accounts:
            raise KeyError("This account does not exist.")

        print("\nAccount Details:")
        print("*" * 20)
        print(f"Username: {username}")
        print(f"Password: {accounts[username]}")
        print("*" * 20)

    except Exception as e:
        print(f"Error: {e}")

# ---------------------------------------------
# Function to Update an Account's Password
# ---------------------------------------------

def update_password():
    """
    Updates the password for an existing account.
    """
    if not accounts:
        print("No passwords to update.")
        return

    username = input("Enter the username for which you want to update the password: ").strip()

    if username in accounts:
        new_password = input("Enter the new password: ").strip()
        accounts[username] = new_password
        print(f"Password for '{username}' has been updated successfully!")
    else:
        print("Account not found!")

# ---------------------------------------------
# Function to Remove an Account
# ---------------------------------------------

def remove_account():
    """
    Removes an account from the password manager.
    """
    if not accounts:
        print("No accounts to remove!")
        return

    username = input("Enter the username you want to remove: ").strip()

    if username in accounts:
        confirmation = input(f"Are you sure you want to delete the account '{username}'? (Y/N): ").strip().lower()
        if confirmation == "y":
            accounts.pop(username)
            print(f"Account '{username}' has been deleted!")
        else:
            print("Returning to the menu...")
    else:
        print("Account not found!")

# ---------------------------------------------
# Function to Save Accounts to a File (Optional)
# ---------------------------------------------

def save_accounts():
    """
    Saves the current accounts to a JSON file for persistence.
    """
    with open("accounts.json", "w") as file:
        json.dump(accounts, file)
    print("Accounts saved successfully!")

# ---------------------------------------------
# Function to Load Accounts from a File (Optional)
# ---------------------------------------------

def load_accounts():
    """
    Loads stored accounts from a JSON file.
    """
    global accounts
    try:
        with open("accounts.json", "r") as file:
            accounts = json.load(file)
        print("Stored accounts loaded successfully!")
    except FileNotFoundError:
        print("No saved accounts found. Starting fresh.")

# ---------------------------------------------
# Function to Handle User Menu Choices
# ---------------------------------------------

def menu():
    """
    Provides an interactive menu for managing accounts.
    """
    load_accounts()  # Load accounts at program start

    while True:
        try:
            print("\n--- Password Manager Menu ---")
            print("1. Add a New Account")
            print("2. View All Stored Accounts")
            print("3. Retrieve a Password")
            print("4. Update an Account's Password")
            print("5. Remove an Account")
            print("6. Save & Quit")

            choice = int(input("Enter your choice (1-6): "))

            if choice == 1:
                add_account()
            elif choice == 2:
                view_accounts()
            elif choice == 3:
                retrieve_password()
            elif choice == 4:
                update_password()
            elif choice == 5:
                remove_account()
            elif choice == 6:
                save_accounts()
                confirm = input("Are you sure you want to quit? (Y/N): ").strip().lower()
                if confirm == "y":
                    print("Thank you for using the Password Manager! Goodbye! 👋")
                    break
                else:
                    print("Returning to the menu...")
            else:
                print("Invalid option! Please enter a number between 1 and 6.")

        except ValueError:
            print("Invalid input! Please enter a number between 1 and 6.")

# ---------------------------------------------
# Program Entry Point
# ---------------------------------------------

if __name__ == "__main__":
    print("\nWelcome to the Secure Password Manager App!")
    menu()
