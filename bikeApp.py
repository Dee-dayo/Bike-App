class Bike:
    def __init__(self):
        self.is_on = False
        self.speedometer = 0

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
            self.speedometer += 1



