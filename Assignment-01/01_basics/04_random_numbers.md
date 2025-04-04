# 🎲 Random Number Generator - Python Program

This program prints **10 random numbers** in the range **1 to 100**.
- Each number is randomly generated.
- Every time you run the program, you get a different set of numbers.

---

## 🛠️ How It Works
1. The program uses the **random.randint()** function to generate random numbers.
2. It generates **10 random numbers** and stores them in a list.
3. Finally, the numbers are printed on a single line, separated by spaces.

---

## 🖥️ Code Implementation
```python
import random

N_NUMBERS: int = 10  # Number of random numbers to generate
MIN_VALUE: int = 1  # Minimum value in range
MAX_VALUE: int = 100  # Maximum value in range

def main():
    random_numbers = [random.randint(MIN_VALUE, MAX_VALUE) for _ in range(N_NUMBERS)]
    print(" ".join(map(str, random_numbers)))

# Required for execution
if __name__ == '__main__':
    main()
```

---

## 📌 Example Output
```
45 79 61 47 52 10 16 83 19 12
```
```
81 76 70 1 27 63 96 100 32 92
```

Each time you run the program, the output will be different! 🎲

---

## 🔗 Google Colab Notebook
[Open in Google Colab](https://colab.research.google.com/drive/14pMX9A2TBdAYr-o3FqaGkIGChf54o2yB?usp=sharing)

---

🚀 **Enjoy generating random numbers!** 😃

