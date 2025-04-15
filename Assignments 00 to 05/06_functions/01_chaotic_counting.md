
# Chaotic Counting Project 🧮

## Description 📜
This is a Python project that counts numbers from 1 to 10, but with a twist! The program uses a `done()` function to randomly decide when to stop counting, printing "I'm done." once the counting is complete.

## Features 🌟
- Counts numbers from 1 to 10, but can stop earlier based on a random likelihood.
- Prints "I'm done." once the counting ends.
- Demonstrates control flow with randomness and return statements.
---
## Code Implementation
```python
import random

DONE_LIKELIHOOD = 0.3  # You can adjust this to see different results

def done():
    return random.random() < DONE_LIKELIHOOD

def chaotic_counting():
    for i in range(1, 11):
        if done():
            return
        print(i, end=' ')

def main():
    print("I'm going to count until 10 or until I feel like stopping, whichever comes first.")
    chaotic_counting()
    print("\nI'm done.")

if __name__ == '__main__':
    main()


```
---
## Example Output 🎬
```
I'm going to count until 10 or until I feel like stopping, whichever comes first.
1 2 3 
I'm done.
```
---

## Google Colab Notebook Link. 📚

Click[here](https://colab.research.google.com/drive/1g8zB2mjiaeakL9Q6KlJNxETlKMQEXMob?usp=sharing)
---
Happy Coding
