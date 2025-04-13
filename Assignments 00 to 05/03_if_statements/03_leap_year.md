# 🗓️ Leap Year Checker - Python Program

This Python program determines whether a given year is a leap year or not based on the rules of the Gregorian calendar.

## 📄 Problem Statement
A leap year (also known as an intercalary year) is a year with an extra day added to keep the calendar year synchronized with the astronomical or seasonal year. In the Gregorian calendar, a leap year contains 366 days.

## 🚀 How the Program Works
1. Prompts the user to input a year.
2. Uses conditional logic to check leap year criteria.
3. Displays the result.
---
## 💻 Python Code
```python
def main():
    # Ask the user for a year
    year = int(input("Enter a year: "))

    # Check for leap year based on Gregorian calendar rules
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                print("That's a leap year!")
            else:
                print("That's not a leap year.")
        else:
            print("That's a leap year!")
    else:
        print("That's not a leap year.")


if __name__ == '__main__':
    main()
```
---
### 📅 Sample Output
```
Enter a year: 2024
That's a leap year!

Enter a year: 1900
That's not a leap year.
```

## 📂 Google Colab Notebook
Click below to run this program in Google Colab:

📍 [Open in Google Colab](https://colab.research.google.com/drive/1sLCIjtzztkiu3LkFOYw3aWVVletsIT3v?usp=sharing)

---
**Happy Coding**
