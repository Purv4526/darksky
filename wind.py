class Wind:
    def __init__(self, speed, direction):
        self.speed = speed
        self.direction = direction

    def is_strong(self):
        return self.speed > 30

    def is_light(self):
        return self.speed < 10

    def increase_speed(self, value):
        self.speed += value

    def decrease_speed(self, value):
        self.speed = max(0, self.speed - value)

    def set_speed(self, speed):
        self.speed = speed

    def set_direction(self, direction):
        self.direction = direction

    def get_speed(self):
        return self.speed

    def get_direction(self):
        return self.direction

    def wind_category(self):
        if self.is_light():
            return "Light breeze"
        elif self.speed <= 30:
            return "Moderate wind"
        return "Strong wind"

    def wind_alert(self):
        return self.speed > 50