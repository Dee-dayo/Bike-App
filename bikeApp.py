class Bike:
    def __init__(self):
        self.is_on = False
        self.speedometer = 0
        self.gear = 0

    def check_status(self):
        return self.is_on

    def start(self):
        self.is_on = True

    def stop(self):
        self.is_on = False

    def check_speedometer(self):
        return self.speedometer

    def accelerate(self):
        if self.is_on:
            if 0 <= self.check_speedometer() <= 20:
                self.speedometer += 1
                self.gear = 1
            elif 21 <= self.check_speedometer() <= 30:
                self.speedometer += 2
                self.gear = 2
            elif 31 <= self.check_speedometer() <= 40:
                self.speedometer += 3
                self.gear = 3
            elif 41 <= self.check_speedometer():
                self.speedometer += 4
                self.gear = 4

    def check_gear(self):
        return self.gear

    def brake(self):
        if self.is_on:
            if 0 <= self.check_speedometer() <= 20:
                self.speedometer -= 1
                self.gear = 1
            elif 21 <= self.check_speedometer() <= 30:
                self.speedometer -= 2
                self.gear = 2
            elif 31 <= self.check_speedometer() <= 40:
                self.speedometer -= 3
                self.gear = 3
            elif 41 <= self.check_speedometer():
                self.speedometer -= 4
                self.gear = 4