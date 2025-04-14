# Random Numbers Generator 🌟

## Problem Statement
Write a program that prints **10 random numbers** in the range **1 to 100**.

Each time you run the program, it should produce a **different set of random numbers**.

### Example Output
```
45 79 61 47 52 10 16 83 19 12
```
The program uses the Python `random` module. Specifically, `random.randint(a, b)` generates a random integer between `a` and `b` (both inclusive).

---

## How It Works 🪡
- Import the `random` module.
- Loop 10 times.
- In each iteration, generate and print a random number between 1 and 100.

---

## Python Code 💻
```python
import random

def main():
    for _ in range(10):
        number = random.randint(1, 100)
        print(number, end=" ")

if __name__ == '__main__':
    main()
```

---

## Output Example 📊
```
32 65 12 98 45 67 23 88 9 100
```

---

## Google Colab Notebook 📔 

🔗 **[Open in Colab](https://colab.research.google.com/drive/1zPtwpqLfJZ4dW1YjbgmxQzDgSyXAPky_?usp=sharing/)**
---

Enjoy generating randomness! 🌀

