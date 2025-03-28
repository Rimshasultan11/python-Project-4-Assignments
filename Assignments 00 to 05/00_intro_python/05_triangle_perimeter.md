# 🔺 Triangle Perimeter Calculator - Python Program

## 📝 Overview
This Python program prompts the user to enter the lengths of the three sides of a triangle and then calculates and displays the **perimeter** of the triangle. The output also includes an ASCII representation of a triangle.

---

## 🔧 How It Works
1️⃣ The user is asked to input the lengths of **three sides of a triangle**.  
2️⃣ The inputs are converted into **floating-point numbers** for accurate calculations.  
3️⃣ The perimeter is calculated using the formula:
   
   ```
   perimeter = side1 + side2 + side3
   ```

4️⃣ The program prints the **perimeter** of the triangle along with a visual ASCII representation of a triangle.

---

## 🖥️ Code Implementation
```python
# Define the main function
def main():
    # Prompting the user for three side lengths
    side1 = float(input("What is the length of side 1? "))
    side2 = float(input("What is the length of side 2? "))
    side3 = float(input("What is the length of side 3? "))

    # Calculating the perimeter
    perimeter = side1 + side2 + side3

    # Printing the result
    print(f"\nThe perimeter of the triangle is {perimeter}\n")
    
    # ASCII representation of a triangle
    print("    /\ ")
    print("   /  \ ")
    print("  /____\ ")


if __name__ == '__main__':
    main()
```

---

## 📌 Example Output
```
What is the length of side 1? 3  
What is the length of side 2? 4  
What is the length of side 3? 5.5  

The perimeter of the triangle is 12.5

    /\
   /  \ 
  /____\

```

---

## 🔗 Google Colab Notebook
[Open in Google Colab](https://colab.research.google.com/drive/1ctMjW3U5WyVOD3OsdNmaB1VHqWJU9DCI?usp=sharing)

---

🚀 **Happy Coding!** 😊
