
class Event:
    def __init__(self, time, delay, name):
        self.when = time + delay
        self.delay = delay
        self.name = name
