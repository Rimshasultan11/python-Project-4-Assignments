# 📏 Pythagorean Theorem Calculator

## 📝 Overview
This Python program calculates the hypotenuse of a right triangle using the **Pythagorean theorem**. The user provides the lengths of the two perpendicular sides, and the program computes and displays the hypotenuse.

---

## 🔧 How It Works
1️⃣ The user enters the lengths of **AB** and **AC** (two perpendicular sides of the triangle).  
2️⃣ The program applies the Pythagorean theorem formula:
   
   ```
   BC = sqrt(AB^2 + AC^2)
   ```
   
3️⃣ The result is displayed with an appropriate message.

---

## 🖥️ Code Implementation
```python
import math

def main():
    # Prompt the user for the lengths of the two perpendicular sides
    ab = float(input("Enter the length of AB: "))
    ac = float(input("Enter the length of AC: "))

    # Calculate the length of the hypotenuse (BC)
    bc = math.sqrt(ab ** 2 + ac ** 2)

    # Print the result
    print(f"The length of BC (the hypotenuse) is: {bc}")

if __name__ == '__main__':
    main()
```

---

## 📌 Example Output
```
Enter the length of AB: 3
Enter the length of AC: 4
The length of BC (the hypotenuse) is: 5.0
```

---

## 🔗 Google Colab Notebook
[Open in Google Colab](https://colab.research.google.com/drive/1eCxlSaNvmOlqy79-rPIkAfJvYZkSanpW?usp=sharing)

---

🚀 **Happy Coding!** 😊
