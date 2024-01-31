class Controller:
    def __init__(self):
        self.top = 100
    
    def update(self):
        # if user hits up key
        self.top += 10

        # if user hits down key
        self.top -= 10