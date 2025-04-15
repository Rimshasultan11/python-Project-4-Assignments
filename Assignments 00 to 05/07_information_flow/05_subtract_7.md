# Subtract Seven – Python Program 

## 📌 Problem Statement
You need to complete the `subtract_seven(num)` helper function which subtracts 7 from the given number `num`, and return the result. Then, write code in the `main()` function to:
- Take a number from the user
- Call `subtract_seven()` using that number
- Print the result

This is a simple example of using helper functions and function calls in Python.

---

## ✅ Features
- Accepts user input as an integer
- Subtracts 7 from the input
- Displays the result

---


## 📌 Code
```python
def subtract_seven(num):
    return num - 7

def main():
    number = int(input("Enter a number: "))
    result = subtract_seven(number)
    print("Result after subtracting 7:", result)

if __name__ == '__main__':
    main()
```
---
## ▶️ Example Output 

```
Enter a number: 20  
Result after subtracting 7: 13
```

---

## 🔗 Google Colab

You can try this program directly in Google Colab:  
👉 [Open in Google Colab](https://colab.research.google.com/drive/1J8L5Dn-kW-53lqKMvcwbAbgsmZR2ONPV?usp=sharing)

---

Happy Coding❤️..
