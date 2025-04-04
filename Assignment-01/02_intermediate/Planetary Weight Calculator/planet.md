# 🌍 Planetary Weight Calculator - Python Program

This program calculates a person's weight on different planets based on their weight on Earth.
- **Milestone #1:** Convert Earth weight to Mars weight.
- **Milestone #2:** Allow calculations for all planets in our solar system.
- The output is rounded to **two decimal places**.

---

## 🛠️ How It Works
1. The program prompts the user to enter their **weight on Earth**.
2. The user selects a **planet** from the available options.
3. The program calculates and displays the **equivalent weight** on the selected planet.

### 🌎 Planetary Gravity Multipliers
| Planet   | Gravity Multiplier |
|----------|-------------------|
| Mercury  | 0.376             |
| Venus    | 0.889             |
| Mars     | 0.378             |
| Jupiter  | 2.36              |
| Saturn   | 1.081             |
| Uranus   | 0.815             |
| Neptune  | 1.14              |

---

## 🖥️ Code Implementation
```python
# Planetary Weight Calculator
def calculate_weight(earth_weight, planet):
    gravity_multipliers = {
        "Mercury": 0.376,
        "Venus": 0.889,
        "Mars": 0.378,
        "Jupiter": 2.36,
        "Saturn": 1.081,
        "Uranus": 0.815,
        "Neptune": 1.14
    }
    
    if planet in gravity_multipliers:
        return round(earth_weight * gravity_multipliers[planet], 2)
    else:
        return None

# Main function
def main():
    earth_weight = float(input("Enter a weight on Earth: "))
    planet = input("Enter a planet: ")
    
    weight_on_planet = calculate_weight(earth_weight, planet)
    
    if weight_on_planet is not None:
        print(f"The equivalent weight on {planet}: {weight_on_planet}")
    else:
        print("Invalid planet name. Please try again.")

if __name__ == "__main__":
    main()
```

---

## 📌 Example Output
```
Enter a weight on Earth: 120
Enter a planet: Mars
The equivalent weight on Mars: 45.36
```
```
Enter a weight on Earth: 150
Enter a planet: Jupiter
The equivalent weight on Jupiter: 354.0
```

---

## 🔗 Google Colab Notebook
[Open in Google Colab](https://colab.research.google.com/drive/1707IjZBtWgHRBnj6I-moVBtME7L6Xfme?usp=sharing)

---

🌌 **Explore the universe with science!** 🚀

