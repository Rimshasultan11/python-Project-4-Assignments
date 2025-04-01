# ⏳ Python Program: Calculate Seconds in a Year

## 📝 Overview
This Python program calculates the total number of seconds in a year based on the standard time units.

---

## 🔧 How It Works
1️⃣ The program defines constants for:
   - **Days in a year** = 365
   - **Hours in a day** = 24
   - **Minutes in an hour** = 60
   - **Seconds in a minute** = 60  

2️⃣ The total number of seconds is calculated using:
   ```python
   seconds_in_year = 365 * 24 * 60 * 60
   ```

3️⃣ The result is printed with a user-friendly message.

---

## 🖥️ Code Implementation
```python
# Define constants

def main():
    # Define constants
    DAYS_IN_YEAR = 365
    HOURS_IN_DAY = 24
    MINUTES_IN_HOUR = 60
    SECONDS_IN_MINUTE = 60

    # Calculate total seconds in a year
    seconds_in_year = DAYS_IN_YEAR * HOURS_IN_DAY * MINUTES_IN_HOUR * SECONDS_IN_MINUTE

    # Print the result
    print(f"There are {seconds_in_year} seconds in a year!")


if __name__ == '__main__':
    main()
```

---

## 📌 Example Output
```
There are 31536000 seconds in a year!
```

---

## 🔗 Google Colab Notebook
[Open in Google Colab](https://colab.research.google.com/drive/1ulxfqKtw6tZTwm1oXIx53RP1faf2e4vw?usp=sharing)

---

🚀 **Enjoy Coding!** 😊
