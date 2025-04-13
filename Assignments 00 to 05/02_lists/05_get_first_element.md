# 📋 Get First Element of a List - Python

## 🧠 Problem Statement
Fill out the function `get_first_element(lst)` which takes in a list `lst` as a parameter and **prints the first element** in the list. The list is **guaranteed to be non-empty**. The user will input the list elements one at a time.

---

## 🚀 Objective
- ✅ Learn how to access elements in a list
- ✅ Practice handling user input and looping
- ✅ Understand the importance of indexing in lists

---

## 🖥️ Code
```python
# Function to get and print the first element of a list
def get_first_element(lst):
    """
    Prints the first element of a provided list.
    """
    print(lst[0])

# Helper function to build the list from user input
def get_lst():
    """
    Prompts the user to enter one element of the list at a time and returns the resulting list.
    """
    lst = []
    elem = input("Please enter an element of the list or press enter to stop. ")
    while elem != "":
        lst.append(elem)
        elem = input("Please enter an element of the list or press enter to stop. ")
    return lst

# Main function
def main():
    lst = get_lst()
    get_first_element(lst)

if __name__ == '__main__':
    main()
```

---

## 📌 Example Output
```
Please enter an element of the list or press enter to stop. 🐍
Please enter an element of the list or press enter to stop. Python
Please enter an element of the list or press enter to stop. Code
Please enter an element of the list or press enter to stop. 
🐍
```

---

## 🔗 Try it on Google Colab
[Open in Google Colab](https://colab.research.google.com/drive/1kZBHWr1HgLsS4nZlzgciqccE7E_nN4qy?usp=sharing)

---
Have fun coding with lists! 🎉

