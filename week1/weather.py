import requests


def get_weather(lat, lon):
    try:
        url = (
            "https://api.open-meteo.com/v1/forecast"
            f"?latitude={lat}&longitude={lon}&current=temperature_2m"
        )

        r = requests.get(url, timeout= 5)
        r.raise_for_status()

        data = r.json()
        temp = data["current"]["temperature_2m"]

        return f"It is {temp}°C right now."

    except requests.exceptions.Timeout:
        return "Request timed out. Please try again."

    except requests.exceptions.RequestException:
        return "Weather service is unavailable."

    except (KeyError, TypeError, ValueError):
        return "Invalid weather data received."

CITIES = {
    "delhi": (28.61, 77.21),
    "mumbai": (19.08, 72.88),
    "lucknow": (26.85, 80.95),
    "varanasi": (25.32, 82.97),
    "bengaluru": (12.97, 77.59),
}

def weather_for(city):
    """Show the temperature for a city, e.g. /weather delhi."""
    city = city.lower().strip()      # lowercase it, then strip spaces
    if city in CITIES:
        lat, lon = CITIES[city]
        return get_weather(lat, lon)
    return "I don't know that city. Try: " + ", ".join(CITIES)



if __name__ == "__main__":
    print(weather_for("Delhi"))
    print(weather_for("Unknown"))
    print(weather_for("Mumbai"))
    print(weather_for("Kolkata"))