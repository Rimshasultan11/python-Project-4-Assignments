# 🤖 Joke Bot - Python Program

## 📌 Problem Statement
This program acts as a simple **Joke Bot** that responds only to a specific request:
- The bot prompts the user with: **"What do you want?"**
- If the user enters **"Joke"**, the bot prints a **random joke**.
- If the user enters anything else, the bot responds with **"Sorry, I only tell jokes".**

The program uses three constants:
- **PROMPT** - The message asking the user what they want.
- **JOKES** - A list of random jokes.
- **SORRY** - The message displayed when the user requests something else.

---

## 🛠️ How It Works
1⃣ The program asks the user for input: *"What do you want?"*
2⃣ If the input is **"Joke"**, the program prints a **randomly selected joke**.
3⃣ If the input is anything else, the program prints a polite rejection.

---

## 🖥️ Code Implementation
```python
import random

# Define constants
PROMPT = "What do you want? "
JOKES = [
    "Why don't scientists trust atoms? Because they make up everything!",
    "Parallel lines have so much in common. It’s a shame they’ll never meet.",
    "Why do programmers prefer dark mode? Because light attracts bugs!",
    "How does a computer get drunk? It takes screenshots.",
    "What’s a programmer’s favorite hangout place? The Foo Bar!"
]
SORRY = "Sorry, I only tell jokes"

def main():
    # Get user input
    user_input = input(PROMPT)
    
    # Check response and print appropriate message
    if user_input == "joke":
        print("Here is a joke for you!", random.choice(JOKES))
    else:
        print(SORRY)


if __name__ == '__main__':
    main()
```

---


## 📌 Example Output
```
What do you want? joke
Here is a joke for you! Why don't scientists trust atoms? Because they make up everything!
```
```
What do you want? Fun Fact
Sorry, I only tell jokes
```

---

## 🔗 Google Colab Notebook
[Open in Google Colab](https://colab.research.google.com/drive/1GAmCd-yIXiSgi_R99umOsN-8ImQ80EGN?usp=sharing)

---

🚀 **Enjoy the jokes!** 😄

