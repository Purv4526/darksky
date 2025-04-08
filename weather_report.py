class WeatherReport:
    def __init__(self, forecast):
        self.forecast = forecast

    def print_summary(self):
        print(self.forecast.get_forecast_summary())

    def alert_if_needed(self):
        if self.forecast.is_extreme_weather():
            print("⚠️ Extreme weather alert!")

    def recommend_outfit(self):
        temp = self.forecast.temp
        if temp < 10:
            return "Wear a coat."
        elif temp < 20:
            return "Wear a jacket."
        else:
            return "T-shirt weather!"

    def is_good_for_outdoor(self):
        return self.forecast.is_sunny() and not self.forecast.is_storm_likely()

    def suggest_activity(self):
        if self.is_good_for_outdoor():
            return "Go for a hike!"
        return "Stay indoors and read a book."

    def show_comfort_index(self):
        return self.forecast.comfort_index()

    def show_feels_like(self):
        return self.forecast.feels_like()

    def show_rain_status(self):
        return "Rain expected." if self.forecast.is_rain_expected() else "No rain expected."

    def wind_status(self):
        return f"Wind: {self.forecast.wind_speed} km/h"

    def humidity_status(self):
        return f"Humidity: {self.forecast.humidity}%"

    def temperature_status(self):
        return f"Temperature: {self.forecast.temp}°C"