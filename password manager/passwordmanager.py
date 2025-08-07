import re
import bcrypt
users = {}

def validatepass(password):
    if len(password) < 8:
        print(" !!!!Password must be at least 8 characters.")
        return False
    if not re.search(r"[A-Z]", password):
        print("!!!!Password must contain at least one uppercase letter.")
        return False
    if not re.search(r"[a-z]", password):
        print("!!!!!Password must contain at least one lowercase letter.")
        return False
    if not re.search(r"\d", password):
        print("!!!!Password must contain at least one digit.")
        return False
    if not re.search(r"[!@#$%^&*()_+=\-{}\[\]:;\"'<>,.?/\\|]", password):
        print("!!!!Password must contain at least one special character.")
        return False
    return True

def passwordtobcrypt(password):
    return bcrypt.hashpw(password.encode(), bcrypt.gensalt())

def createacc():
    username = input("Enter new username: ")
    if username in users:
        print("Username already exist.")
        return
    password = input("Create a password: ")
    if validatepass(password):
        hashed = passwordtobcrypt(password)
        users[username] = hashed
        print("Account created successfully!")

def login():
    username = input("Username: ")
    password = input("Password: ")
    hashed = users.get(username)
    if hashed and bcrypt.checkpw(password.encode(), hashed):
        print(f"Welcome back, {username}!")
    else:
        print("Invalid username or password.")

def main():
    while True:
        print("\n--- Password Manager ---")
        print("1. Login")
        print("2. Create Account")
        print("3. Exit")
        choice = input("Choose an option: ")
        if choice == '1':
            login()
        elif choice == '2':
            createacc()
        elif choice == '3':
            print("exiting.......")
            break
        else:
            print("enter a valid choice")

if __name__ == "__main__":
    main()

