class Event:
    def __init__(self, time, delay, name):
        self.time = time
        self.when = time + delay
        self.delay = delay
        self.name = name

