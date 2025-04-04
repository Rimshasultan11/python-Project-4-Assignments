# 🧠 List Practice and 🎮 Index Game - Python Project

## 📘 Overview
This project consists of two fun and interactive parts:

1. 🍎 **List Practice**
2. 🧩 **Index Game**

These exercises help users build a strong understanding of list operations such as:
- Adding elements
- Measuring length
- Accessing elements by index
- Modifying elements
- Slicing lists

---

## 🍓 Problem #1: List Practice
This part demonstrates basic list manipulation in Python.

### ✅ Features:
- A list called `fruit_list` is created with a few fruits.
- The program prints the length of the list using `len()`.
- A new fruit, `'mango'`, is added using `.append()`.
- The updated list is displayed.

### 🧾 Code:
```python
def main():
    # Problem #1: List Practice

    # Create a list called `fruit_list` that contains the following fruits:
    fruit_list = ['apple', 'banana', 'orange', 'grape', 'pineapple']

    # Print the length of the list.
    print("Length of fruit_list:", len(fruit_list))

    # Add 'mango' at the end of the list.
    fruit_list.append('mango')

    # Print the updated list.
    print("Updated fruit_list:", fruit_list)
```

---

## 🎲 Problem #2: Index Game
This is an interactive text-based game where users practice index-based operations on a list.

### 🧩 Features:
- A sample list `[10, 20, 30, 40, 50]` is used.
- Users can choose from the following options:
  1. 🔍 **Access an element** by index.
  2. ✏️ **Modify an element** at a given index with a new value.
  3. ✂️ **Slice the list** using a start and end index.
  4. 🚪 **Exit the game**.

### 🧾 Code:
```python
def access_element(lst, index):
    try:
        return f"Element at index {index}: {lst[index]}"
    except IndexError:
        return "Index out of range."

def modify_element(lst, index, new_value):
    try:
        lst[index] = new_value
        return f"Element at index {index} modified successfully."
    except IndexError:
        return "Index out of range."

def slice_list(lst, start, end):
    try:
        return lst[start:end]
    except:
        return "Error slicing the list."

def main():
    sample_list = [10, 20, 30, 40, 50]

    while True:
        print("\nSample list:", sample_list)
        print("Choose an operation:")
        print("1. Access element")
        print("2. Modify element")
        print("3. Slice list")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            index = int(input("Enter index to access: "))
            print(access_element(sample_list, index))

        elif choice == '2':
            index = int(input("Enter index to modify: "))
            new_value = input("Enter new value: ")
            result = modify_element(sample_list, index, new_value)
            print(result)
            print("Updated list:", sample_list)

        elif choice == '3':
            start = int(input("Enter start index: "))
            end = int(input("Enter end index: "))
            sliced = slice_list(sample_list, start, end)
            print("Sliced list:", sliced)

        elif choice == '4':
            print("Thanks for playing!")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == '__main__':
    main()
```

---


## 🔗 Google Colab
[📎 Click here to open in Google Colab](https://colab.research.google.com/drive/11ZihN3z77Wog-CauBYfpXQRtdYJBGliw?usp=sharing)
---


🎉 **Happy Coding and Keep Practicing!** 🚀

