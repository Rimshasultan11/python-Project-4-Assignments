# In Range Checker 🔍

## Problem Statement 📘
Implement a function that takes in three integers: `n`, `low`, and `high`, and checks whether `n` lies within the range `[low, high]` (inclusive).

---

## How It Works ⚙️
- The function `in_range(n, low, high)` returns `True` if `n` is greater than or equal to `low` and less than or equal to `high`.
- It returns `False` otherwise.
- The `main()` function takes input from the user and prints the result.

---

## Python Code 🐍
```python
def in_range(n, low, high):
    """
    Returns True if n is between low and high, inclusive.
    high is guaranteed to be greater than low.
    """
    return low <= n <= high

def main():
    n = int(input("Enter the number to check: "))
    low = int(input("Enter the lower bound: "))
    high = int(input("Enter the upper bound: "))

    result = in_range(n, low, high)
    print("Result:", result)

if __name__ == '__main__':
    main()
```

---

## Sample Run 🎯
```
Enter the number to check: 5
Enter the lower bound: 1
Enter the upper bound: 10
Result: True
```

---

## Run it on Google Colab 🚀
[Open in Google Colab](https://colab.research.google.com/drive/1UMwNXGlO6FHC2LSaOOL5PACkuSJLD--q?usp=sharing)

---

Happy Coding! 💻✨

