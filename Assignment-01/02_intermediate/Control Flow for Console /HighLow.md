# 🎲 High-Low Game - Python Program


The **High-Low Game** is a fun number guessing game where:
- Two random numbers (from **1 to 100**) are generated—one for the **player** and one for the **computer**.
- The player **can see their number** but **not the computer’s**.
- The player guesses whether their number is **higher** or **lower** than the computer’s.
- If the guess is **correct**, they earn a **point**.
- The game continues for multiple rounds.
- The final score is displayed with a **performance message** based on the player’s success.

---

## 🛠️ How It Works
1. The game generates two random numbers—**one for the player** and **one for the computer**.
2. The player inputs **"higher"** or **"lower"**.
3. The program checks if the guess is correct:
   - If correct, **player gains a point**.
   - If incorrect, **no points awarded**.
4. The game repeats for a fixed number of rounds.
5. After all rounds, the player receives a **final score** and a **performance message**.

---

## 🖥️ Code Implementation
```python
import random

NUM_ROUNDS = 5  # Number of rounds in the game

def main():
    print("Welcome to the High-Low Game!")
    print("--------------------------------")
    score = 0  # Player's score
    
    for round_number in range(1, NUM_ROUNDS + 1):
        print(f"Round {round_number}")
        player_number = random.randint(1, 100)
        computer_number = random.randint(1, 100)
        
        print(f"Your number is {player_number}")
        
        guess = input("Do you think your number is higher or lower than the computer's? (higher/lower): ").strip().lower()
        
        while guess not in ["higher", "lower"]:
            guess = input("Invalid input. Please enter either 'higher' or 'lower': ").strip().lower()
        
        if (guess == "higher" and player_number > computer_number) or (guess == "lower" and player_number < computer_number):
            print("You were right!", end=" ")
            score += 1
        else:
            print("Aww, that's incorrect.", end=" ")
        
        print(f"The computer's number was {computer_number}")
        print(f"Your score is now {score}\n")
    
    # Final Score Message
    print("Thanks for playing!")
    print("Your final score is:", score)
    
    if score == NUM_ROUNDS:
        print("Wow! You played perfectly!")
    elif score >= NUM_ROUNDS // 2:
        print("Good job, you played really well!")
    else:
        print("Better luck next time!")

# Run the game
if __name__ == '__main__':
    main()
```

---

## 📌 Example Output
```
Welcome to the High-Low Game!
--------------------------------
Round 1
Your number is 42
Do you think your number is higher or lower than the computer's? higher
Aww, that's incorrect. The computer's number was 67
Your score is now 0

Round 2
Your number is 89
Do you think your number is higher or lower than the computer's? higher
You were right! The computer's number was 75
Your score is now 1

... (more rounds are played)

Thanks for playing!
Your final score is: 3
Good job, you played really well!
```

---

## 🔗 Google Colab Notebook
[Open in Google Colab](https://colab.research.google.com/drive/11a78rb9-_IlXupc40vcXKM-Y_1eR4_O3?usp=sharing)

---

🎮 **Enjoy the game and test your luck!** 🚀

