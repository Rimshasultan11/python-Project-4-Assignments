# Sophia's Fruit Stock Checker 🍎🍌

## Problem Statement
Sophia has a fruit store. She has written a function `num_in_stock(fruit)` that returns how many of that fruit are currently in inventory. Your job is to write code in `main()` that will:

1. Prompt the user to enter a fruit name:  
   `Enter a fruit:`
2. Call the `num_in_stock(fruit)` function to check the availability.
3. Print the number in stock **if** Sophia has more than 0 of that fruit.
4. Print `"This fruit is not in stock."` if Sophia has none of that fruit in inventory.

---

## How It Works 🧠
- A fruit name is input by the user.
- The `num_in_stock()` function checks its inventory.
- Based on the result:
  - If stock > 0: it prints the available quantity.
  - If stock == 0: it prints a message saying the fruit is not in stock.

---

## Python Code 📝
```python
def num_in_stock(fruit):
    inventory = {
        'apple': 500,
        'banana': 300,
        'pear': 1000,
        'grape': 250,
        'orange': 200
    }
    return inventory.get(fruit.lower(), 0)

def main():
    fruit = input("Enter a fruit: ")
    count = num_in_stock(fruit)
    if count > 0:
        print("This fruit is in stock! Here is how many:")
        print(count)
    else:
        print("This fruit is not in stock.")

if __name__ == '__main__':
    main()
```

---

### Sample Runs 📊
#### Run 1:
```
Enter a fruit: pear
This fruit is in stock! Here is how many:
1000
```

#### Run 2:
```
Enter a fruit: lychee
This fruit is not in stock.
```

---

## Try It on Google Colab ✨
Click below to open and run the notebook in Google Colab:

[Open in Google Colab 🚀](https://colab.research.google.com/drive/1buauezZ6HHenupDDixOumyvxwAtejN6E?usp=sharing)

---

Happy Coding! ❤️

