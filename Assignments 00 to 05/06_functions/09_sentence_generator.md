
# Make Sentence 📝

## Problem Statement
Implement the helper function `make_sentence(word, part_of_speech)` that takes two parameters:
- `word`: a string (the word to be placed in the sentence)
- `part_of_speech`: an integer (0 for noun, 1 for verb, 2 for adjective)

Based on the value of `part_of_speech`, the function will print the word in one of the following sentence templates:
- If `part_of_speech` is 0, the template is: 
  "I am excited to add this ____ to my vast collection of them!"
- If `part_of_speech` is 1, the template is: 
  "It's so nice outside today it makes me want to ____!"
- If `part_of_speech` is 2, the template is: 
  "Looking out my window, the sky is big and ____!"

The program asks the user for a word and the type of part of speech, then prints the sentence.

---

## How It Works 🤖
- The user is prompted to input a word (noun, verb, or adjective).
- Then the user is asked to specify the type of part of speech: 0 for noun, 1 for verb, or 2 for adjective.
- Based on the part of speech, the word is inserted into one of the templates and printed.

---

## Python Code 📝
```python
def make_sentence(word, part_of_speech):
    if part_of_speech == 0:
        print(f"I am excited to add this {word} to my vast collection of them!")
    elif part_of_speech == 1:
        print(f"It's so nice outside today it makes me want to {word}!")
    elif part_of_speech == 2:
        print(f"Looking out my window, the sky is big and {word}!")

def main():
    word = input("Please type a noun, verb, or adjective: ")
    part_of_speech = int(input("Is this a noun, verb, or adjective? Type 0 for noun, 1 for verb, 2 for adjective: "))
    make_sentence(word, part_of_speech)

if __name__ == '__main__':
    main()
```

---

### Example Output 💻
```
Please type a noun, verb, or adjective: groovy
Is this a noun, verb, or adjective? Type 0 for noun, 1 for verb, 2 for adjective: 2
Looking out my window, the sky is big and groovy!
```

---

## Try It on Google Colab ✨
Click below to open and run the notebook in Google Colab:

[Open in Google Colab 🚀](https://colab.research.google.com/drive/1uw0LkgSnvGQCkehfyEHC3RoUklf3s4cJ?usp=sharing)

---

Happy Coding! 🎉
