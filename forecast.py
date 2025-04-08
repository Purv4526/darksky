class Forecast:
    def __init__(self, temp, humidity, wind_speed, chance_of_rain):
        self.temp = temp
        self.humidity = humidity
        self.wind_speed = wind_speed
        self.chance_of_rain = chance_of_rain

    def is_storm_likely(self):
        return self.wind_speed > 50 and self.chance_of_rain > 70

    def is_rain_expected(self):
        return self.chance_of_rain > 50

    def is_sunny(self):
        return self.chance_of_rain < 20 and self.humidity < 50

    def comfort_index(self):
        return 100 - abs(22 - self.temp) * 2 - abs(50 - self.humidity)

    def update_temperature(self, new_temp):
        self.temp = new_temp

    def update_humidity(self, new_humidity):
        self.humidity = new_humidity

    def update_wind_speed(self, new_speed):
        self.wind_speed = new_speed

    def update_rain_chance(self, new_chance):
        self.chance_of_rain = new_chance

    def get_forecast_summary(self):
        return f"Temp: {self.temp}°C, Humidity: {self.humidity}%, Wind: {self.wind_speed} km/h, Rain: {self.chance_of_rain}%"

    def is_extreme_weather(self):
        return self.temp > 40 or self.temp < -10 or self.wind_speed > 70

    def feels_like(self):
        return self.temp - ((100 - self.humidity) / 5)