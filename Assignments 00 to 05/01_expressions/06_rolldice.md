# 🎲 Dice Rolling Simulation

## 📝 Problem Statement
This program simulates rolling two dice and prints the results of each roll along with the total sum of the two dice.

---

## 🔧 How It Works
1️⃣ The program generates two random numbers, each representing a six-sided die roll.  
2️⃣ The results of both dice are displayed.  
3️⃣ The program calculates and prints the total sum of the two dice rolls.

---

## 🖥️ Code Implementation
```python
import random

def main():
    # Roll two dice
    die1 = random.randint(1, 6)
    die2 = random.randint(1, 6)
    
    # Calculate total
    total = die1 + die2
    
    # Print results
    print(f"Die 1: {die1}")
    print(f"Die 2: {die2}")
    print(f"Total: {total}")

if __name__ == '__main__':
    main()
```

---
## 📌 Example Output
```
Die 1: 4
Die 2: 2
Total: 6
```

---

## 🔗 Google Colab Notebook
[Open in Google Colab](https://colab.research.google.com/drive/1GYk_BpZ-AbW1yWp6wV8ctUKqMfxIfdNL?usp=sharing)

---

🎲 **Happy Rolling!** 😊
