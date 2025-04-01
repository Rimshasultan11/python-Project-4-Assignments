### **📌 Sum of Numbers Program**

## **📝 Problem Statement**
Write a function that takes a list of numbers and returns the sum of those numbers.

---

## **✅ Solution**
```python
# Function to calculate the sum of numbers in a list
def add_many_numbers(numbers)-> int:
    """
    Takes in a list of numbers and returns the sum of those numbers.
    """

    total_so_far: int = 0
    for number in numbers:
        total_so_far += number

    return total_so_far


def main():
    numbers: list[int] = [1, 2, 3, 4, 5]  # Make a list of numbers
    sum_of_numbers: int = add_many_numbers(numbers)  # Find the sum of the list
    print(sum_of_numbers)  # Print out the sum above
    

if __name__ == '__main__':
    main()
```

---

## **🖥️ How It Works**
1️⃣ The function `add_many_numbers(numbers)` takes a **list of integers** as input.  
2️⃣ It iterates through the list, adding each number to `total_so_far`.  
3️⃣ The final sum is returned and printed.  

---

## **▶️ Example Output**
```
The sum of the numbers is: 15
```
---

## **🔗 Google Colab Notebook**
[Open in Google Colab](https://colab.research.google.com/drive/1NE4-UmwZv_1T8hXTTk4dHU6UZ0EXu-Vp?usp=sharing)
 
🚀 **Happy Coding! 😊**

