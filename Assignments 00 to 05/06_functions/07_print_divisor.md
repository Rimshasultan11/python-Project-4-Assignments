
# Print Divisors of a Number ➗

## Problem Statement
Write a helper function `print_divisors(num)` that takes in a number and prints all of its divisors — numbers from 1 to `num` that divide it with no remainder.

---

## How It Works 🤖
- The user is prompted to input a number.
- The program loops through numbers from 1 to `num`.
- It prints each number that divides `num` exactly (no remainder).

---

## Python Code 📝
```python
def print_divisors(num):
    print(f"Here are the divisors of {num}")
    for i in range(1, num + 1):
        if num % i == 0:
            print(i, end=" ")

def main():
    num = int(input("Enter a number: "))
    print_divisors(num)

if __name__ == '__main__':
    main()
```

---

### Example Output 💻
```
Enter a number: 12
Here are the divisors of 12
1 2 3 4 6 12
```

---

## Try It on Google Colab ✨
Click below to open and run the notebook in Google Colab:

[Open in Google Colab 🚀](https://colab.research.google.com/drive/1O_cSEv_Ssx1ajYdFZaZnM5SMhVXdG3rF?usp=sharing)

---

Happy Coding! 💡
