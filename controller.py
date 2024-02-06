import keyboard

class Controller:
    def __init__(self):
        self.top = 100
        self.count = 0
    
    def update(self):

        if keyboard.is_pressed('w'):
            print("UP")
            self.top += 10
        
        elif keyboard.is_pressed('s'):
            print("DOWN")
            self.top -= 10

        print(keyboard)
        self.count += 1
        print(self.count)