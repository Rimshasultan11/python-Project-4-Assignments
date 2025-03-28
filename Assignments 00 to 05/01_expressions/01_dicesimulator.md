# 🎲 Simulating Rolling Two Dice - Python

## 📝 Overview
This Python program simulates rolling **two dice three times** and prints the results of each die roll. It demonstrates how **variable scope** works by ensuring that each roll is generated within a function scope.

---

## 🔧 How It Works
1️⃣ The program uses the **random** module to generate random numbers between `1` and `6` for each die.  
2️⃣ A function `roll_dice()` simulates rolling **two dice** and returns their values.  
3️⃣ The main function calls `roll_dice()` **three times** and prints the results.  

---

## 🖥️ Code Implementation
```python
import random

# Function to roll two dice
def roll_dice():
    die1 = random.randint(1, 6)  # First die roll
    die2 = random.randint(1, 6)  # Second die roll
    return die1, die2

# Define the main function
def main():
    print("\nRolling two dice three times:\n")
    
    for i in range(1, 4):
        die1, die2 = roll_dice()
        print(f"Roll {i}: Die 1 = {die1}, Die 2 = {die2}")
    
if __name__ == '__main__':
    main()
```

---

## 📌 Example Output
```
Rolling two dice three times:

Roll 1: Die 1 = 3, Die 2 = 5
Roll 2: Die 1 = 1, Die 2 = 6
Roll 3: Die 1 = 4, Die 2 = 2
```

---

## 🔗 Google Colab Notebook
[Open in Google Colab](https://colab.research.google.com/drive/12RWMpyvi5WXlYbq7yBH5rlWn8CMa7eWn?usp=sharing)

---

🎲 **Enjoy Simulating Dice Rolls!** 😊
