
# Print Multiple Messages 📝

## Problem Statement
Fill out the `print_multiple(message, repeats)` function, which takes two parameters: a string `message` and an integer `repeats` representing the number of times to print the message.

The program prompts the user for a message and the number of repeats and prints the message the specified number of times.

---

## How It Works 🤖
- The user is prompted to enter a message and the number of times to repeat it.
- The program then prints the message the specified number of times.

---

## Python Code 📝
```python
def print_multiple(message, repeats):
    for _ in range(repeats):
        print(message)

def main():
    message = input("Please type a message: ")
    repeats = int(input("Enter a number of times to repeat your message: "))
    print_multiple(message, repeats)

if __name__ == '__main__':
    main()
```

---

### Example Output 💻
```
Please type a message: Hello!
Enter a number of times to repeat your message: 6
Hello!
Hello!
Hello!
Hello!
Hello!
Hello!
```

---

## Try It on Google Colab ✨
Click below to open and run the notebook in Google Colab:

[Open in Google Colab 🚀](https://colab.research.google.com/drive/1Etuixls7Up4a5Ok3sTRNm8vA0-YRUiv9?usp=sharing)

---

Happy Coding! 🎉
