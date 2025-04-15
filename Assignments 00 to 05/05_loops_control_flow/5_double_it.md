# 🚀 Double Until 100 - Python Program

This is a simple Python program that repeatedly doubles a number entered by the user until the result is 100 or greater.

## 📌 Problem Statement
Prompt the user to enter a number. Then double that number and print the result. Continue doubling and printing the result until the value reaches or exceeds 100.
---
## Code Implementation🚀
```python
def main():
    curr_value = int(input("Enter a number: "))
    while curr_value < 100:
        curr_value = curr_value * 2
        print(curr_value)

if __name__ == '__main__':
    main()

```
---
### Example Run:
```
Enter a number: 2
4
8
16
32
64
128
```


## 🔗 Google Colab Notebook 
You can try this code directly in Google Colab Notebook:
👉 [Open in Colab](https://colab.research.google.com/drive/1NoVdKthUjlKj54R2NeEVtxg8PF7NTUn7?usp=sharing)

---

Happy coding ❤️ 

