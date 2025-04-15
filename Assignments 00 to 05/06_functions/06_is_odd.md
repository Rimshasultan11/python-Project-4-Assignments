
# Even or Odd from 10 to 19 🔢

## Problem Statement
Write a program that prints whether each number from 10 to 19 is even or odd.

---

## How It Works 🤖
- Loop through numbers from 10 to 19.
- For each number:
  - If the number is divisible by 2, it's even.
  - Otherwise, it's odd.
- Print the number followed by "even" or "odd" on the same line.

---

## Python Code 📝
```python
def main():
    for i in range(10, 20):
        if i % 2 == 0:
            print(i, "even", end=" ")
        else:
            print(i, "odd", end=" ")

if __name__ == '__main__':
    main()
```

---

### Example Output 💻
```
10 even 11 odd 12 even 13 odd 14 even 15 odd 16 even 17 odd 18 even 19 odd 
```

---

## Try It on Google Colab ✨
Click below to open and run the notebook in Google Colab:

[Open in Google Colab 🚀](https://colab.research.google.com/drive/1OVpT0E5xSLBrKeGYCIGkrGg7G87Wcygr?usp=sharing)

---

Happy Coding! ✨
