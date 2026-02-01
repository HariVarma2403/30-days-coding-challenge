import os
import re
import getpass
import hashlib

FILE_NAME = "users.txt"


def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()


def load_users():
    if not os.path.exists(FILE_NAME):
        return {}
    users = {}
    with open(FILE_NAME, "r") as file:
        for line in file:
            username, password = line.strip().split(",")
            users[username] = password
    return users


def save_user(username, password):
    with open(FILE_NAME, "a") as file:
        file.write(f"{username},{password}\n")


def valid_username(username):
    return len(username) >= 5


def valid_password(password):
    has_letter = re.search(r"[A-Za-z]", password)
    has_number = re.search(r"[0-9]", password)
    has_symbol = re.search(r"[!@#$%^&*(),.?\":{}|<>]", password)
    return has_letter and has_number and has_symbol and len(password) >= 6


def register():
    users = load_users()

    username = input("Choose username: ")
    if not valid_username(username):
        print("Username must be at least 5 characters long.\n")
        return

    if username in users:
        print("Username already exists!\n")
        return

    password = getpass.getpass("Choose password: ")

    if not valid_password(password):
        print("Password must contain letters, numbers, and symbols.\n")
        return

    hashed = hash_password(password)
    save_user(username, hashed)
    print("Registration successful!\n")


def login():
    users = load_users()
    attempts = 3

    while attempts > 0:
        username = input("Username: ")
        password = getpass.getpass("Password: ")
        hashed = hash_password(password)

        if username in users and users[username] == hashed:
            print("Login successful! Welcome!\n")
            return
        else:
            attempts -= 1
            print(f"Invalid credentials. Attempts left: {attempts}\n")

    print("Account locked after 3 failed attempts.\n")


def main():
    while True:
        print("=== SECURE LOGIN SYSTEM ===")
        print("1. Register")
        print("2. Login")
        print("3. Exit")

        choice = input("Choose option: ")

        if choice == "1":
            register()
        elif choice == "2":
            login()
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid option\n")


if __name__ == "__main__":
    main()
