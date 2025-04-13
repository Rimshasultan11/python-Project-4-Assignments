# 📋 Continuous List Input Program - Python

## 📝 Overview
This Python program continuously prompts the user to enter values which are added one by one into a list. The input ends when the user presses **Enter** without typing anything. After that, the complete list is displayed.

---

## 🚀 How It Works
1. An empty list is created to store the user inputs.
2. The user is prompted to enter values in a loop.
3. If the user presses **Enter** without entering any value, the loop ends.
4. The final list is printed to the console.

---

## 💻 Code Implementation
```python
# Program to continuously add user input to a list until enter is pressed

def main():
    user_list = []  # Initialize an empty list

    while True:
        value = input("Enter a value: ")
        
        if value == "":  # If input is empty, exit the loop
            break
        
        user_list.append(value)  # Add the entered value to the list

    print("Here's the list:", user_list)  # Print the final list

if __name__ == '__main__':
    main()

```

---

## 🖥️ Sample Output
```
Enter a value: 1
Enter a value: 2
Enter a value: 3
Enter a value:
Here's the list: ['1', '2', '3']
```

---

# 🔗 Google Colab Notebook

[Open in Google Colab](https://colab.research.google.com/drive/1z8VGU-0jqtDXKEGFD_7aI-2VqxwGB4UL?usp=sharing)

Happy coding! 🎉

