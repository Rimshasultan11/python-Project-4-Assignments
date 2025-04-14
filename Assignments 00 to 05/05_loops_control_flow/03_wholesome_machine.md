# Affirmation Repetition Program

This Python program repeatedly prompts the user to type a specific affirmation until it is entered correctly. The affirmation is meant to boost motivation and positivity. The user will be gently reminded to try again until they input the affirmation exactly as required.

---

## Program Code
```python
def main():
    affirmation = "I am capable of doing anything I put my mind to."
    print(f"Please type the following affirmation: {affirmation}")
    
    while True:
        user_input = input()
        if user_input == affirmation:
            print("That's right! :)")
            break
        else:
            print("Hmmm That was not the affirmation. Please try again:")


if __name__ == '__main__':
    main()


 
```
---

### Sample Run:
```
Please type the following affirmation: I am capable of doing anything I put my mind to.
> I am capable
Hmmm That was not the affirmation.
Please type the following affirmation: I am capable of doing anything I put my mind to.
> I am capable of doing anything I put my mind to.
That's right! :)
```

## Google Colab Link
You can try this program on Google Colab by clicking the link below.:

👉 [Open in Google Colab](https://colab.research.google.com/drive/15Qacem5DMIW61BkALBgblwStSku6g-d0?usp=sharing)


---

**Stay positive and keep learning! 💪**

