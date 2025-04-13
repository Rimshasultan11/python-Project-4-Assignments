# ✂️ Shorten a List in Python

## 📝 Problem Statement

Fill out the function `shorten(lst)` which removes elements **from the end** of the list `lst` **until it is exactly `MAX_LENGTH` items long**.

- Each removed item should be printed.
- If the list is already shorter than `MAX_LENGTH`, leave it unchanged.

✅ This demonstrates **list mutability** and how to manipulate list lengths safely.


---

## ✅ code implementation 

```python
MAX_LENGTH = 3

def shorten(lst):
    """
    Removes items from the end of the list until its length is MAX_LENGTH.
    Prints each item removed.
    """
    while len(lst) > MAX_LENGTH:
        removed = lst.pop()
        print("Removed:", removed)

def get_list():
    """
    Prompts the user to input list elements until an empty input is given.
    Returns the list.
    """
    lst = []
    elem = input("Enter a value (or press Enter to stop): ")
    while elem != "":
        lst.append(elem)
        elem = input("Enter a value (or press Enter to stop): ")
    return lst

def main():
    lst = get_list()
    print("\nOriginal list:", lst)
    shorten(lst)
    print("Final list:", lst)

if __name__ == '__main__':
    main()
```

---

## 💡 Example Output

```
Enter a value (or press Enter to stop): apple
Enter a value (or press Enter to stop): banana
Enter a value (or press Enter to stop): cherry
Enter a value (or press Enter to stop): dragonfruit
Enter a value (or press Enter to stop):

Original list: ['apple', 'banana', 'cherry', 'dragonfruit']
Removed: dragonfruit
Final list: ['apple', 'banana', 'cherry']
```

---

## 🔗 Google Colab Notebook

[👉 Open in Google Colab](https://colab.research.google.com/drive/1kT5q73cSqxzsgt3xbz6YugxbWUJMS8Bs?usp=sharing)  


---
*Happy Coding*
