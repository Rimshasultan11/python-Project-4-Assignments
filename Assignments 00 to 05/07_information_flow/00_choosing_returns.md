
# Is Adult? 🎉

## Problem Statement
The goal of this program is to determine if a person is an adult based on their age. The program checks if the given age is greater than or equal to the legal age of adulthood. If the age is above or equal to the adult age, the program returns `True`; otherwise, it returns `False`.

The legal adult age is defined by the `ADULT_AGE` variable (in this case, 18).

---

## How It Works 🤖
- The program prompts the user to input a person's age.
- It then calls the `is_adult()` function which checks if the inputted age is greater than or equal to the legal adult age (`ADULT_AGE`).
- The result (`True` or `False`) is printed on the screen.

---

## Python Code 📝
```python
# The legal adult age in the United States
ADULT_AGE = 18

def is_adult(age):
    if age >= ADULT_AGE:
        return True
    else:
        return False

def main():
    age = int(input("How old is this person?: "))
    print(is_adult(age))

if __name__ == '__main__':
    main()
```

---

### Example Output 💻
1. **For an adult age:**
```
How old is this person?: 25
True
```

2. **For a non-adult age:**
```
How old is this person?: 12
False
```

---

## Try It on Google Colab ✨
Click below to open and run the notebook in Google Colab:

[Open in Google Colab 🚀](https://colab.research.google.com/drive/1RZRtkoy4zcCwbSNB8lA74P9FvW74lbsG?usp=sharing)

---

Happy Coding! 🎉
