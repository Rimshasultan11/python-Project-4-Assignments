# 📞 Phonebook Dictionary Program - Python

## 🔍 Problem Statement
This program demonstrates how to use dictionaries in Python to create a simple phonebook. Users can add contact names with their phone numbers.


## ⚙️ How It Works
1. A dictionary is initialized to store phonebook entries.
2. The user is prompted to enter contact names and their phone numbers.
3. The loop continues until the user presses Enter without input.

## ✍️ Code Implementation 
```python
def main():
    phonebook = {}  # create an empty dictionary

    while True:
        name = input("Enter a name (or press enter to finish): ")
        if name == "":
            break
        number = input(f"Enter a phone number for {name}: ")
        phonebook[name] = number  # add name and number to the dictionary

    print("\nPhonebook:")
    for name, number in phonebook.items():
        print(f"{name}: {number}")


if __name__ == '__main__':
    main()

```

## 📊 Example Output
```
Enter a name (or press enter to finish): Rimsha
Enter a phone number for Rimsha: 03401121563
Enter a name (or press enter to finish): 

Phonebook:
Rimsha: 03401121563

```
---
## 🚀 Try it in Google Colab
Click the link below to run this program interactively:

[Open in Google Colab](https://colab.research.google.com/drive/1yY9FROfjzKzr5pWEGVpRZVXeLFqFGb5L?usp=sharing)

---
Happy Coding! 🚀

