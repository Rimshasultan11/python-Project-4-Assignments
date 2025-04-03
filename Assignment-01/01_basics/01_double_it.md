# 🔢 Doubling Number Program

This program takes an integer input from the user and continuously doubles it, printing each result. The process continues until the value reaches **100 or greater**.

### Example:
#### Input:
```
Enter a number: 2
```
#### Output:
```
4
8
16
32
64
128
```

The program starts with the user's number, **doubles it**, and prints the result in each iteration until the value exceeds **100**.

---

## 🛠️ How It Works
1️⃣ The program asks the user to enter a **starting number**.
2️⃣ The entered number is stored in `curr_value`.
3️⃣ A `while` loop continuously **doubles the value** while it's **less than 100**.
4️⃣ The updated value is printed each time.

---

## 🖥️ Code Implementation
```python
# Function to double the number until it reaches or exceeds 100
def main():
    curr_value = int(input("Enter a number: "))  # Get user input
    
    while curr_value < 100:
        curr_value *= 2  # Double the value
        print(curr_value)  # Print the result

if __name__ == '__main__':
    main()
```

---

## 📌 Example Output
```
Enter a number: 3
6
12
24
48
96
192
```

---

## 🔗 Google Colab Notebook
[Open in Google Colab](https://colab.research.google.com/drive/1vZnAFjpFa-X7gq91ylzuNOrDFqb9kmNW?usp=sharing)

---

🚀 **Have fun doubling numbers!** 🎉

