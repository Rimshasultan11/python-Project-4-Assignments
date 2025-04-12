# 🌦️ Weather Forecast - Python Project

## 📌 Problem Statement
Knowing the current weather conditions is essential for daily planning. Manually searching weather for each city is inconvenient. This **Python project** provides a solution by allowing users to check real-time weather for any city using a weather API.

---

## 🎯 Features
- Get live weather for any city.
- Displays:
  - City Name
  - Temperature
  - Weather Description
  - Humidity
  - Wind Speed
- Uses external API to fetch real-time data.
- Command-line based and beginner-friendly.

---

## 🛠️ How It Works
1. The user enters a **city name**.
2. The program calls the weather API using the city name.
3. It parses the returned JSON data.
4. Displays the weather details in a clean format.
5. Handles invalid city names and API errors gracefully.

---
🖥️ Code Implementation
```python
 import requests
def get_weather(city):
    api_key = "d37624457bd43bcba25e927cee25509c"  # Replace with your actual API key from OpenWeatherMap
    base_url = "https://api.openweathermap.org/data/2.5/weather?appid={}".format(api_key)
    params = {"q": city, "appid": api_key, "units": "metric"}

    try:
        response = requests.get(base_url, params=params)
        data = response.json()

        if response.status_code == 200:
            weather = {
                "City": data["name"],
                "Temperature (°C)": data["main"]["temp"],
                "Weather": data["weather"][0]["description"],
                "Humidity (%)": data["main"]["humidity"],
                "Wind Speed (m/s)": data["wind"]["speed"]
            }
            return weather
        else:
            return {"Error": data.get("message", "Failed to retrieve data")}
    except requests.RequestException as e:
        return {"Error": str(e)}

# Run the program
print("🌤️ Welcome to the Weather App!")
city = input("Enter city name: ")
weather_info = get_weather(city)

for key, value in weather_info.items():
    print(f"{key}: {value}")
```

---
# 🧪 Example Output
```
🌤️ Welcome to the Weather App!
Enter city name: karachi

📍 City: Karachi
🌡️ Temperature: 32.1°C
🌥️ Description: clear sky
💧 Humidity: 44%
💨 Wind Speed: 4.6 m/s
```
---
# 🔐 Important Notes

- You need an API key from OpenWeatherMap.

- Replace your_api_key_here with your real API key.

- API key can be obtained for free at: https://openweathermap.org/api 
---
 # 🔗 Google Colab Notebook

Run it online using Google Colab:
[👉 Open in Google Colab](https://colab.research.google.com/drive/1wfRn2KniUy0UkR3Hb5KlzKoEgoR658_8?usp=sharing)

*Happy coding*😊


