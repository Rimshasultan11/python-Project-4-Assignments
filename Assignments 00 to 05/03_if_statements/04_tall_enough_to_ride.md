# 🎢 Height Requirement Checker - Python Program

## 📘 Problem Statement
This Python program asks the user how tall they are and prints whether or not they're taller than a pre-specified minimum height. In amusement parks, rollercoasters frequently have minimum height requirements for safety reasons.

The program assumes a **minimum height of 50** units (you can assume centimeters, inches, etc.).
---

## 💡 Code Implementation 
```python
def main():
    height = input("How tall are you? ")
    if height:
        height = int(height)
        if height >= 50:
            print("You're tall enough to ride!")
        else:
            print("You're not tall enough to ride, but maybe next year!")

if __name__ == '__main__':
    main()
```

---

## ✅ Sample Runs:
```bash
How tall are you? 100
You're tall enough to ride!

How tall are you? 10
You're not tall enough to ride, but maybe next year!
```
---

## 📎 Google Colab Notebook
Click the link below to open and run this code in Google Colab:

👉 [Open in Google Colab](https://colab.research.google.com/drive/1G6sbjsipP8Klh3iP9pKFfezer42GSzjf?usp=sharing)

---

### Happy Coding 
