# 📘 Fibonacci Sequence Generator

This program prints the terms in the Fibonacci sequence up to a specified maximum value using Python. It starts from `Fib(0)` and continues generating terms until the value exceeds 10,000.

---

## 💻code implementation
```python
def main():
    MAX_VALUE = 10000  # Constant for maximum value
    a, b = 0, 1  # Starting values for Fib(0) and Fib(1)

    while a < MAX_VALUE:
        print(a, end=' ')
        a, b = b, a + b  # Next term is sum of previous two

if __name__ == '__main__':
    main()

```

### ✅ Sample Output
```
0 1 1 2 3 5 8 13 21 34 55 89 144 233 377 610 987 1597 2584 4181 6765
```

## 🔗 Google Colab Notebook
You can run and test this code directly in your browser using Google Colab.:

[📎 Open in Google Colab](https://colab.research.google.com/drive/1-qkcH1rFwIsXhkS39_Cp99kQI2ShnHOS?usp=sharing)

---
Happy Coding! 💻✨
