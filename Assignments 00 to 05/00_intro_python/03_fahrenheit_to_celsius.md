# 🌡️ Python Program: Fahrenheit to Celsius Converter

## 📝 Overview
This Python program converts a temperature from Fahrenheit to Celsius. It prompts the user to enter a temperature in Fahrenheit, performs the conversion using a standard formula, and then displays the result.

---

## 🔧 How It Works
1️⃣ The user is prompted to enter a **temperature in Fahrenheit**.  
2️⃣ The input is read and converted into a **floating-point number**.  
3️⃣ The conversion formula is applied:
   
   ```
   degrees_celsius = (degrees_fahrenheit - 32) * 5.0 / 9.0
   ```
   
4️⃣ The result is displayed with an appropriate message.

---

## 🖥️ Code Implementation
```python
# Define the main function
def main():
    # Ask user for temperature in Fahrenheit
    fahrenheit = float(input("Enter temperature in Fahrenheit: "))

    # Convert Fahrenheit to Celsius
    celsius = (fahrenheit - 32) * 5.0 / 9.0

    # Print the result
    print(f"Temperature: {fahrenheit}F = {celsius}C")

if __name__ == '__main__':
    main()
```

---

## 📌 Example Output
```
Enter temperature in Fahrenheit: 79
Temperature: 79.0F = 26.11111111111111C
```

---

## 🔗 Google Colab Notebook
[Open in Google Colab](https://colab.research.google.com/drive/1nWZ7Z5LQkQJplPY3GsBSZoTb84aw26I9?usp=sharing)

---

🚀 **Enjoy Coding!** 😊
