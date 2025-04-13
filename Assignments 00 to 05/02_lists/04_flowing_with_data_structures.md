# 📋 Mutability in Python - List Modification Without Return

## 🚀 Objective
Write a function `add_three_copies(...)` that takes a list and a piece of data, then adds **three copies** of the data to the list **without returning** anything. This demonstrates how mutable objects like lists retain changes made within functions.

---

## 🔍 What You Will Learn
- ✅ The difference between **mutable** and **immutable** data types
- ✅ How functions can modify mutable data types **without returning them**
- ✅ Practical use of `append()` and loops to manipulate lists

---

## 🖥️ Code
```python
# Function that modifies a list (mutable) without returning it
def add_three_copies(my_list, data):
    for _ in range(3):
        my_list.append(data)

# Main function
def main():
    message = input("Enter a message to copy: ")
    messages = []  # Empty list

    print("\nList before:", messages)

    add_three_copies(messages, message)  # Modify list

    print("List after:", messages)

if __name__ == '__main__':
    main()
```

---

## 📌 Example Output
```
Enter a message to copy: Hello world!

List before: []
List after: ['Hello world!', 'Hello world!', 'Hello world!']
```

---

## 🔗 Try it on Google Colab
[Open in Google Colab](https://colab.research.google.com/drive/13ClGo3YoU_cqs29b-7wdGveDUuaF2dCg?usp=sharing)

---

Enjoy exploring Python mutability! 🐍✨

