# 📘 First 20 Even Numbers - Python

## 📝 Problem Statement
Write a Python program that prints the **first 20 even numbers**. You must use a **loop** to generate the output instead of writing twenty `print` statements manually.

🔹 The first even number is `0`, and the sequence increases by 2 each time.

**Expected Output:**
```
0 2 4 6 8 10 12 14 16 18 20 22 24 26 28 30 32 34 36 38
```

---

## 🖥️ Code implementation 
```python
# Prints the first 20 even numbers using a loop

def main():
    count = 0
    even = 0
    print("The first 20 even numbers are:")
    while count < 20:
        print(even, end=" ")
        even += 2
        count += 1
 
if __name__ == '__main__':
    main()
```
---
# output of code

```
The first 20 even numbers are:
0 2 4 6 8 10 12 14 16 18 20 22 24 26 28 30 32 34 36 38
```
---

## 🔗 Google Colab Notebook
[Open in Google Colab](https://colab.research.google.com/drive/1XA3om7ORl9EgEmL8-TufJgWSFuzTSvJg?usp=sharing)

---

🎉 **Happy Coding!**
