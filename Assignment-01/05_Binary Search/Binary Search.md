
# 🔍 Binary Search - Python Project

## 📌 Problem Statement
This Python project demonstrates how **Binary Search** works in a sorted list of numbers. The program simulates a simple search game where the user provides a number and the program searches for it using the Binary Search algorithm.

---

## 🛠️ How It Works
1️⃣ The program starts by showing the user a **sorted list of numbers**.  
2️⃣ The user is prompted to **enter a number** to search.  
3️⃣ The program performs **binary search** to locate the number.  
4️⃣ If found, it displays the index of the number. Otherwise, it shows a **"not found"** message.

---

## 🖥️ Code Implementation
```python
def binary_search(arr, target):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid  # Target found
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return -1  # Target not found


# Sorted list of numbers
numbers = [3, 7, 15, 18, 24, 31, 42, 56, 67, 72, 88, 95]

print("🔍 Welcome to the Binary Search Game!")
print(f"Here's a sorted list:\n{numbers}")

# User input
try:
    user_input = int(input("Enter a number to search: "))
    result = binary_search(numbers, user_input)

    if result != -1:
        print(f"✅ Number found at index {result}.")
    else:
        print("❌ Number not found in the list.")
except ValueError:
    print("⚠️ Please enter a valid number.")
```

---

## 💡 Sample Output
```
🔍 Welcome to the Binary Search Game!
Here's a sorted list:
[3, 7, 15, 18, 24, 31, 42, 56, 67, 72, 88, 95]
Enter a number to search: 42
✅ Number found at index 6.
```

```
Enter a number to search: 100
❌ Number not found in the list.
```

---

## 🔗 Google Colab Notebook
[Open in Google Colab](https://colab.research.google.com/drive/1GZVw7kzp63izbwXuQ9mZE2OYhjrRC9-9?usp=sharing)

---

🚀 **Explore the power of efficient searching!**
