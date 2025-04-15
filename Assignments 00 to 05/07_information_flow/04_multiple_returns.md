# 📝 User Data Collection Program

This is a simple Python program that collects a user's first name, last name, and email address using the console, and returns these values as a tuple. This example demonstrates how to collect and return multiple values from a function using tuple packing.

## 📌 Features
- Accepts user input for first name, last name, and email address
- Returns the collected information as a tuple
- Easy to understand and extend for beginners

## 📘 Sample Code
```python
def get_user_data():
    first_name = input("What is your first name?: ")
    last_name = input("What is your last name?: ")
    email = input("What is your email address?: ")
    return first_name, last_name, email

def main():
    user_data = get_user_data()
    print("Received the following user data:", user_data)

if __name__ == '__main__':
    main()
```
---
## Example Output
```
What is your first name?: Rimsha
What is your last name?: sultan
What is your email address?: rimshasultan098@gmail.com
Received the following user data: ('Rimsha', 'sultan', 'rimshasultan098@gmail.com')

```

## 🔗 Try It on Google Colab
Click the link below to open and try the code directly on Google Colab:

[Open in Google Colab](https://colab.research.google.com/drive/13orx_ZKsG4rdeUJw1dr6-KkTOmuAEBQz?usp=sharing)

---
Happy Coding

