# 🛍️ Fruit Shop Total Cost Calculator

## 📜 Problem Statement
You like buying fruits from a local shop and want to keep track of the total cost before going. This Python program prompts you for the quantity of each available fruit, then calculates and displays the total price.

## 💡 Features
- Uses a Python dictionary to store fruit prices.
- Accepts user input for quantity.
- Calculates total using a simple loop.
---
## ✍️ code Implementation

```python
 def main():
    # Dictionary of fruits and their prices
    fruit_prices = {
        "apple": 10.0,
        "durian": 15.0,
        "jackfruit": 25.0,
        "kiwi": 20.0,
        "rambutan": 8.5,
        "mango": 7.0
    }

    total_cost = 0

    for fruit, price in fruit_prices.items():
        quantity = input(f"How many ({fruit}) do you want?: ")
        if quantity.isdigit():
            total_cost += int(quantity) * price

    print(f"\nYour total is ${total_cost}")


if __name__ == '__main__':
    main()

```
## 🧠 Example Output 
```
How many (apple) do you want?: 2
How many (durian) do you want?: 0
How many (jackfruit) do you want?: 1
How many (kiwi) do you want?: 0
How many (rambutan) do you want?: 1
How many (mango) do you want?: 3

Your total is $99.5
```

## 🔗 Google Colab Link
Click the link below to run this program in Google Colab:

[▶️ Open in Colab](https://colab.research.google.com/drive/19KVOhxUyc3UaVFlFcRtZQ6V8hWgJha0D?usp=sharing)

---

👨‍💻 Happy Coding!

