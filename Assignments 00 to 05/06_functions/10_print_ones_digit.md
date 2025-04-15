
# Print Ones Digit 🧮

## Problem Statement
Write a function called `print_ones_digit(num)`, which takes an integer `num` as a parameter and prints its ones digit. The modulo (remainder) operator `%` will be helpful in finding the ones digit.

The program asks the user for an integer and then calls the `print_ones_digit()` function to display the ones digit of the number.

---

## How It Works 🤖
- The program prompts the user to input an integer.
- The function calculates the ones digit using the modulo operator (`%`), which returns the remainder when dividing the number by 10.
- The result (ones digit) is then printed on the screen.

---

## Python Code 📝
```python
def print_ones_digit(num):
    ones_digit = num % 10
    print(f"The ones digit is {ones_digit}")

def main():
    num = int(input("Enter a number: "))
    print_ones_digit(num)

if __name__ == '__main__':
    main()
```

---

### Example Output 💻
```
Enter a number: 42
The ones digit is 2
```

---

## Try It on Google Colab ✨
Click below to open and run the notebook in Google Colab:

[Open in Google Colab 🚀](https://colab.research.google.com/drive/1dZ9HGnL9Kqz5i6rXppqf2hlxtUscgznS?usp=sharing)

---

Happy Coding! 🎉
