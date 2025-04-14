# 📊 Number Frequency Counter - Python Program

## 📝 Problem Statement
This Python program counts the number of times each number appears in a list. The program repeatedly asks the user to input numbers. When the user stops entering numbers, the program prints how many times each number was entered.

### 🧠 How it Works
- The program uses a Python dictionary to store each unique number and its frequency.
- The user is continuously prompted to enter numbers.
- When the user hits "Enter" without typing a number, input stops.
- The program then prints how many times each number appeared.

---

## 💻 Code Implementation 
```python
def main():
    number_counts = {}  # Dictionary to store occurrences

    while True:
        number = input("Enter a number: ")
        if number == "":  # Stop if input is empty
            break
        if number in number_counts:
            number_counts[number] += 1
        else:
            number_counts[number] = 1

    for number, count in number_counts.items():
        print(f"{number} appears {count} times.")


if __name__ == '__main__':
    main()

```

---
## ▶️ Example Output 
```
Enter a number: 3
Enter a number: 4
Enter a number: 3
Enter a number: 6
Enter a number: 4
Enter a number: 3
Enter a number: 12
Enter a number: 
3 appears 3 times.
4 appears 2 times.
6 appears 1 times.
12 appears 1 times.
```

---
## 🔗 Google Colab Notebook
You can run the code in Google Colab here: [Open in Colab](https://colab.research.google.com/drive/1tjTY8qk_iEo9eO8RZ3HDQnYwHIRpH_dw?usp=sharing)

---


Enjoy coding! 🚀
