class Temperature:
    def __init__(self, celsius):
        self.celsius = celsius

    def to_fahrenheit(self):
        return (self.celsius * 9/5) + 32

    def to_kelvin(self):
        return self.celsius + 273.15

    def is_below_freezing(self):
        return self.celsius < 0

    def is_above_boiling(self):
        return self.celsius > 100

    def describe(self):
        if self.celsius < 0:
            return "Freezing"
        elif self.celsius < 15:
            return "Cold"
        elif self.celsius < 25:
            return "Warm"
        else:
            return "Hot"

    def increase(self, amount):
        self.celsius += amount

    def decrease(self, amount):
        self.celsius -= amount

    def set_temperature(self, new_temp):
        self.celsius = new_temp

    def get_temperature(self):
        return self.celsius

    def difference(self, other_temp):
        return abs(self.celsius - other_temp)