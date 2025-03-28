#  Python Program: Age Riddle Solver

## 📝 Overview
This Python program calculates and prints the ages of five friends—Anton, Beth, Chen, Drew, and Ethan—based on given age relationships.

---

## 🔧 How It Works
1️⃣ **Anton** is given as **21 years old**.  
2️⃣ **Beth** is **6 years older** than Anton.  
3️⃣ **Chen** is **20 years older** than Beth.  
4️⃣ **Drew**'s age is the **sum of Chen's and Anton's age**.  
5️⃣ **Ethan** is the **same age as Chen**.  
6️⃣ The program calculates and prints each person's name with their correct age.

---

## 🖥️ Code Implementation
```python
# Define the main function
def main():
    # Assigning ages based on given conditions
    Anton = 21
    Beth = Anton + 6
    Chen = Beth + 20
    Drew = Chen + Anton
    Ethan = Chen

    # Printing results
    print(f"Anton is {Anton}")
    print(f"Beth is {Beth}")
    print(f"Chen is {Chen}")
    print(f"Drew is {Drew}")
    print(f"Ethan is {Ethan}")

if __name__ == '__main__':
    main()
```

---

## 📌 Example Output
```
Anton is 21
Beth is 27
Chen is 47
Drew is 68
Ethan is 47
```

---

## 🔗 Google Colab Notebook
[Open in Google Colab](https://colab.research.google.com/drive/1SIZE5Q0AEMM2Hsy9Jl3y_UvGfwUzzlow?usp=sharing)

