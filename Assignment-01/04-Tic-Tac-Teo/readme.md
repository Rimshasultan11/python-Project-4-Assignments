
# 🎮 Tic-Tac-Toe - Console Python Game

## 📌 Project Description
This is  the classic Tic-Tac-Toe game using Python. It allows **two players** to take turns and play the game in the terminal.

---

## 🛠️ Features
- Two-player mode: Player **X** and Player **O**
- Checks for:
  - Winning conditions (rows, columns, diagonals)
  - Draw (when no more moves left)
  - Invalid inputs (non-numeric or out-of-range)
  - Already taken cells
- Clean board display and status updates after each turn

---

## 💡 How It Works

1. A **3x3 grid** is created using a 2D list.
2. Players take turns by entering **row and column numbers** (from 0 to 2).
3. The game continues until:
   - A player **wins**, or
   - It's a **draw**, or
   - The input is invalid or already taken.

---
## implement code

```bash
# Function to display the board
def display_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

# Function to check for a win
def check_winner(board, player):
    # Check rows, columns, and diagonals
    for row in board:
        if all(cell == player for cell in row):
            return True

    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True

    if all(board[i][i] == player for i in range(3)):
        return True

    if all(board[i][2 - i] == player for i in range(3)):
        return True

    return False

# Function to check for a draw
def check_draw(board):
    return all(cell != " " for row in board for cell in row)

# Function to play the game
def play_game():
    board = [[" " for _ in range(3)] for _ in range(3)]
    current_player = "X"

    while True:
        display_board(board)
        print(f"Player {current_player}'s turn")

        try:
            row = int(input("Enter row (0-2): "))
            col = int(input("Enter column (0-2): "))

            if board[row][col] != " ":
                print("❌ Cell already taken. Try again.")
                continue

            board[row][col] = current_player

            if check_winner(board, current_player):
                display_board(board)
                print(f"🎉 Player {current_player} wins!")
                break

            if check_draw(board):
                display_board(board)
                print("🤝 It's a draw!")
                break

            # Switch players
            current_player = "O" if current_player == "X" else "X"

        except (ValueError, IndexError):
            print("⚠️ Invalid input. Please enter numbers between 0 and 2.")

# Start the game
play_game()

```
---

## 📌 Example Game Output

```
 |   |  
---------
 |   |  
---------
 |   |  
Player X's turn  
Enter row (0-2): 0  
Enter column (0-2): 0  

X |   |  
---------
 |   |  
---------
 |   |  
Player O's turn  
...
🎉 Player X wins!
```

---


## 🔗 Google Colab Notebook Link

[Open in Google Colab](https://colab.research.google.com/drive/1cAqZo2BsKzZjYQY831bgXIwNWxg3_YAP?usp=sharing)  

---


🚀 **Let the battle of Xs and Os begin!** 😄
