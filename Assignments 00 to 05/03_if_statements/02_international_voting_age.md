# Voting Eligibility Program

## Problem Statement

This Python program checks a user's eligibility to vote in three fictional countries based on their age. Each country has a different minimum voting age:

- **Peturksbouipo**: Voting age is **16**
- **Stanlau**: Voting age is **25**
- **Mayengua**: Voting age is **48**

The user is prompted to input their age, and the program displays whether they are eligible to vote in each of the countries.

---
## Final Code
```python
def main():
    age = int(input("How old are you? "))

    if age >= 16:
        print("You can vote in Peturksbouipo where the voting age is 16.")
    else:
        print("You cannot vote in Peturksbouipo where the voting age is 16.")

    if age >= 25:
        print("You can vote in Stanlau where the voting age is 25.")
    else:
        print("You cannot vote in Stanlau where the voting age is 25.")

    if age >= 48:
        print("You can vote in Mayengua where the voting age is 48.")
    else:
        print("You cannot vote in Mayengua where the voting age is 48.")

if __name__ == '__main__':
    main()
```
---
## Sample Output
```
How old are you? 20
You can vote in Peturksbouipo where the voting age is 16.
You cannot vote in Stanlau where the voting age is 25.
You cannot vote in Mayengua where the voting age is 48.
```

## Google Colab Notebook Link
[Open in Google Colab](https://colab.research.google.com/drive/1VqeTuZ-_bBl0vHQ-6MxdBQSZl2qIjQYd?usp=sharing)

---
**Happy coding**

