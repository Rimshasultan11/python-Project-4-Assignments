# 🎲 Guess My Number - Python Project

## 📖 Problem Statement
This is a simple Python program called **"Guess My Number"**. The program randomly selects a number between 0 and 99, and then asks the user to guess the number. After each guess, the program will give a hint whether the guess is too high or too low, until the user correctly guesses the number.


## 📚 Code:
```python
import random

def main():
    number_to_guess = random.randint(0, 99)
    print("I am thinking of a number between 0 and 99...")

    while True:
        try:
            guess = int(input("Enter a guess: "))

            if guess > number_to_guess:
                print("Your guess is too high\n")
            elif guess < number_to_guess:
                print("Your guess is too low\n")
            else:
                print(f"Congrats! The number was: {number_to_guess}")
                break

        except ValueError:
            print("Please enter a valid integer.")
if __name__ == '__main__':
    main()
```

---

## 📊 Output Example:
```
I am thinking of a number between 0 and 99...
Enter a guess: 70
Your guess is too high

Enter a guess: 20
Your guess is too low

Enter a guess: 45
Congrats! The number was: 45
```

---

## 📄 Google Colab Notebook
Click the link below to run this program in Google Colab:

🔗 [Open in Google Colab](https://colab.research.google.com/drive/1_aHnrLGW4iYsF3iA3APagWyyzlRYMCbk?usp=sharing)


---



Happy coding! 🚀

