# 🔐 Password Hash Checker

## 📋 Problem Statement
You want to be safe online and use different passwords for different websites. However, you are forgetful at times and want to make a program that can match which password belongs to which website **without storing the actual password**! 😅

## 💡 Program Description
This program allows a user to attempt to log in by providing an email and a password. The password is hashed using SHA256, and matched against a dictionary of stored hashed passwords. ✅

The main function `login(...)` checks if the email exists and the hashed password matches.

## ▶️ How to Run the Program
1. Run the script in any Python environment (like IDLE, VS Code, Jupyter Notebook, or Google Colab).
2. Input your email and password when prompted.
3. The program will tell you if the login is successful or not.

---

## Code Implementation
```python
import hashlib

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def login(email, password_to_check, stored_logins):
    # Check if the email exists in the stored_logins dictionary
    if email in stored_logins:
        # Hash the entered password
        hashed_password = hash_password(password_to_check)
        # Compare the stored hash with the hashed input
        return hashed_password == stored_logins[email]
    return False

def main():
    stored_logins = {
        "user1@example.com": hash_password("apple123"),
        "user2@example.com": hash_password("banana456"),
        "user3@example.com": hash_password("cherry789")
    }

    email = input("Enter your email: ")
    password = input("Enter your password: ")

    if login(email, password, stored_logins):
        print("Login successful!")
    else:
        print("Login failed! Incorrect email or password.")

if __name__ == '__main__':
    main()
    
```
---
## 📂 Example Output
```
Enter your email: user2@example.com
Enter your password: banana456
Login successful!
```

```
Enter your email: user3@example.com
Enter your password: wrongpass
Login failed! Incorrect email or password.
```

## 📎 Google Colab Link
[🔗 Open in Colab](https://colab.research.google.com/drive/1-vJtwpHx7ynwUTKNncDgmYD8oe4No2k3?usp=sharing)

---
### Happy Coding
