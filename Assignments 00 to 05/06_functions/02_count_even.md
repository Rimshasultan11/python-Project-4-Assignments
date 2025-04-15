# 📊 Count Even Numbers Program

## 🔢 Problem Statement

This program prompts the user to enter integers one by one, building a list from the inputs. The user can stop inputting numbers by pressing `Enter` without typing a number. After all entries are collected, the program counts and prints how many of those numbers are even.


## 📝 How It Works
1. The program uses a loop to repeatedly ask the user for input.
2. Each valid integer is added to a list.
3. The input ends when the user presses `Enter` on an empty prompt.
4. A separate function `count_even(lst)` is called to count and display the number of even integers in the list.
---
## Code Implementation
```python
def count_even(lst):
    # Count the even numbers in the list
    even_count = sum(1 for num in lst if num % 2 == 0)
    print(f"The number of even numbers in the list is: {even_count}")

def main():
    lst = []
    
    while True:
        user_input = input("Enter an integer or press enter to stop: ")
        
        # Check if the user pressed Enter without typing anything
        if user_input == "":
            break
        else:
            try:
                # Try converting the input to an integer
                num = int(user_input)
                lst.append(num)
            except ValueError:
                print("That's not a valid integer. Please try again.")
    
    # Call count_even function to count and display even numbers
    count_even(lst)

if __name__ == '__main__':
    main()

```
---
## ⚖️  Example Output
```
Enter an integer or press enter to stop: 5
Enter an integer or press enter to stop: 4
Enter an integer or press enter to stop: 8
Enter an integer or press enter to stop:
The number of even numbers in the list is: 2
```

## 🔗 Google Colab Link
Click below to run this program on Google Colab Notebook:

[Run on Google Colab Notebook ✨](https://colab.research.google.com/drive/1fSF9dyynma2TaLQrmKADeCeg6BYdA6Pk?usp=sharing/)

---

Happy Coding ❤️ 

