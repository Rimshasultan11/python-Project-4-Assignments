# 🔢 Number Squaring Program - Python

## 📝 Overview
This Python program prompts the user to enter a number and calculates its **square** (the product of the number multiplied by itself). The output displays both the input number and its squared value.

---

## 🔧 How It Works
1️⃣ The user is asked to input a **number**.  
2️⃣ The input is converted into a **floating-point number** for accurate calculations.  
3️⃣ The square of the number is calculated using:
   
   ```
   square = number * number
   ```
   
4️⃣ The program prints the **squared value** of the entered number.

---

## 🖥️ Code Implementation
```python
# Define the main function
def main():
    # Prompt the user for a number
    number = float(input("Type a number to see its square: "))
    
    # Calculate the square of the number
    square = number * number
    
    # Print the result
    print(f"\n{number} squared is {square}\n")
    # ASCII representation of a square 
    print(" __________________ ")
    print("|                  |")
    print("|                  |")
    print("|                  |")
    print("|                  |")
    print("|                  |")
    print("|                  |")
    print("|                  |")
    print("|__________________|")

if __name__ == '__main__':
    main()
```

---


## 📌 Example Output
```
Type a number to see its square: 4

4.0 squared is 16.0
 __________________ 
|                  |
|                  |
|                  |
|                  |
|                  |
|                  |
|                  |
|__________________|
```

---

## 🔗 Google Colab Notebook
[Open in Google Colab](https://colab.research.google.com/drive/1hcauUUe6vNMYNrqooimjXM4AnpeB28Um?usp=sharing)

---

🚀 **Happy Coding!** 😊
