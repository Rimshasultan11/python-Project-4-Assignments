# 📏 Feet to Inches Converter

## 📝 Overview
This Python program converts a given length from **feet to inches**. It prompts the user to enter a value in feet, performs the conversion, and then displays the result.

---

## 🔧 How It Works
1️⃣ The user is asked to enter a **length in feet**.  
2️⃣ The input is read and converted into a **floating-point number**.  
3️⃣ The conversion formula is applied:
   
   ```
   inches = feet * 12
   ```
   
4️⃣ The result is displayed in inches.

---

## 🖥️ Code Implementation
```python
# Define the main function
def main():
    INCHES_IN_FOOT: int = 12
    # Ask user for length in feet
    feet = float(input("Enter length in feet: "))

    # Convert feet to inches
    inches = feet * INCHES_IN_FOOT

    # Print the result
    print(f"{feet} feet is equal to {inches} inches.")


if __name__ == '__main__':
    main()
```

---

## 📌 Example Output
```
Enter length in feet: 5
5.0 feet is equal to 60.0 inches.
```

---

## 🔗 Google Colab Notebook
[Open in Google Colab](https://colab.research.google.com/drive/1-Fhd4za1CCfUAzEne2OWEgG0AY-lNsbA?usp=sharing)

---

🚀 **Happy Coding!** 😊

