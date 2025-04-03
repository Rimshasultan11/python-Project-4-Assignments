# 🎯 Guess My Number - Python Program

This program implements a **Guess My Number** game where:
- The program randomly selects a number between **0 and 99**.
- The user must guess the number.
- The program provides feedback:
  - "Too high" if the guess is greater than the number.
  - "Too low" if the guess is lower than the number.
  - "Congrats!" when the correct number is guessed.

---

## 🛠️ How It Works
1. The program selects a **random number** between **0 and 99**.
2. It continuously asks the user for a **guess**.
3. If the guess is incorrect, the program provides a hint ("Too high" or "Too low").
4. The process repeats until the user correctly guesses the number.

---

## 🖥️ Code Implementation
```python
import random

def main():
    # Generate a random number between 0 and 99
    secret_number = random.randint(0, 99)
    print("I am thinking of a number between 0 and 99...")
    
    while True:
        # Get user input
        guess = int(input("Enter a guess: "))
        
        # Compare guess with secret number
        if guess > secret_number:
            print("Your guess is too high")
        elif guess < secret_number:
            print("Your guess is too low")
        else:
            print(f"Congrats! The number was: {secret_number}")
            break  # Exit loop when guessed correctly


if __name__ == '__main__':
    main()
```

---

## 📌 Example Output
```
I am thinking of a number between 0 and 99...
Enter a guess: 50
Your guess is too high

Enter a new number: 25
Your guess is too low

Enter a new number: 40
Your guess is too low

Enter a new number: 45
Your guess is too low

Enter a new number: 48
Congrats! The number was: 48
```

---

## 🔗 Google Colab Notebook
[Open in Google Colab](https://colab.research.google.com/drive/1-jCniNc3oYvacPAherVvPRxowCYrsxdc?usp=sharing)

---

🎉 **Enjoy the game and happy guessing!** 😃

