# 📌 Get Last Element from a List - Python

## 📝 Problem Statement
Fill out the function `get_last_element(lst)` which takes in a list `lst` as a parameter and prints the **last element** in the list. The list is guaranteed to be non-empty, but there are no guarantees on its length.

---

## 💡 How It Works
1. The program prompts the user to enter list elements one by one.
2. An empty input (`Enter`) stops the input process.
3. The list is passed to a function that prints the **last element**.

---

## 🖥️ Code Implementation
```python
# Function to print the last element of a list
def get_last_element(lst):
    print(lst[-1])

# Function to create a list from user input
def get_lst():
    lst = []
    elem = input("Please enter an element of the list or press enter to stop. ")
    while elem != "":
        lst.append(elem)
        elem = input("Please enter an element of the list or press enter to stop. ")
    return lst

# Main function
def main():
    lst = get_lst()
    get_last_element(lst)

if __name__ == '__main__':
    main()
```

---

## 🔍 Example Output
```
Please enter an element of the list or press enter to stop. Apple
Please enter an element of the list or press enter to stop. Banana
Please enter an element of the list or press enter to stop. Cherry
Please enter an element of the list or press enter to stop.
Cherry
```

---

## 🔗 Google Colab Link
[👉 Open in Google Colab](https://colab.research.google.com/drive/1V1M9_xDn2jJPJDgY74sX8UhJ1UqLMKna?usp=sharing)

---

✨ Happy Coding!

