# 🚀 Spaceship Countdown - Python Program

This program prints out the countdown for a spaceship that is about to launch.
- The countdown starts from **10** and goes down to **1**.
- After reaching 1, the program prints **"Liftoff!"**.
- Each number is printed on a new line for a clear countdown effect.
- A **1-second delay** is added between each countdown number for a dramatic effect.

---

## 🛠️ How It Works
1. The program uses a **for loop** to iterate from 10 down to 1.
2. Each number is printed on a **new line** with a **1-second delay**.
3. After the loop ends, the program prints **"Liftoff!"** to signal launch.

---

## 🖥️ Code Implementation
```python
import time  # Import time module for delay

def main():
    # Countdown from 10 to 1
    for i in range(10, 0, -1):
        print(i)  # Print each number on a new line
        time.sleep(1)  # Wait for 1 second before printing the next number
    
    # Print Liftoff after countdown ends
    print("Liftoff!")

# Required for execution
if __name__ == '__main__':
    main()
```

---

## 📌 Example Output
```
10
9
8
7
6
5
4
3
2
1
Liftoff!
```

---

## 🔗 Google Colab Notebook
[Open in Google Colab](https://colab.research.google.com/drive/13xzz5-0n6HJQBtzV_xAlogJ4Jg8o_5Ks?usp=sharing)

---

🚀 **Happy coding!** 😃

