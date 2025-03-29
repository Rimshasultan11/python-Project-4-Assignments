## 🔢 Python Program: Division with Remainder

### 📝 Overview
This Python program asks the user for two integers and performs division, displaying both the quotient and the remainder.

---

### 🔧 How It Works
1️⃣ The user is prompted to enter two integers: 
   - The first number (dividend).
   - The second number (divisor).
2️⃣ The program performs **integer division** (`//`) to compute the quotient.
3️⃣ It calculates the **remainder** (`%`).
4️⃣ The result is displayed in a formatted output.

---

### 🖥️ Code Implementation
```python
def main():
    # Ask user for the first number
    num1 = int(input("Please enter an integer to be divided: "))

    # Ask user for the second number
    num2 = int(input("Please enter an integer to divide by: "))

    # Perform division and find remainder
    quotient = num1 // num2
    remainder = num1 % num2

    # Display result
    print(f"The result of this division is {quotient} with a remainder of {remainder}")


if __name__ == '__main__':
    main()
```

---

### 📌 Example Output
```
Please enter an integer to be divided: 5
Please enter an integer to divide by: 3
The result of this division is 1 with a remainder of 2
```
## 🔗 Google Colab Notebook
[Open in Google Colab](https://colab.research.google.com/drive/1Ujth855MzTFJBKp3uiKg4nwL_M3Iz1UY?usp=sharing)
---

🚀 **Enjoy Coding!** 😊
