class Bike:
    def __init__(self):
        self.is_on = False

    def check_status(self):
        return self.is_on

    def start(self):
        self.is_on = True
