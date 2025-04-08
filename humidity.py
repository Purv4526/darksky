class Humidity:
    def __init__(self, percentage):
        self.percentage = percentage

    def is_humid(self):
        return self.percentage > 60

    def is_dry(self):
        return self.percentage < 30

    def increase(self, amount):
        self.percentage = min(100, self.percentage + amount)

    def decrease(self, amount):
        self.percentage = max(0, self.percentage - amount)

    def set_humidity(self, value):
        self.percentage = max(0, min(100, value))

    def get_humidity(self):
        return self.percentage

    def is_optimal(self):
        return 30 <= self.percentage <= 60

    def humidity_level(self):
        if self.is_humid():
            return "High"
        elif self.is_dry():
            return "Low"
        return "Moderate"

    def humidity_warning(self):
        return self.percentage > 80

    def compare(self, other_humidity):
        return self.percentage - other_humidity