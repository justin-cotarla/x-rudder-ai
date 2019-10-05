from xrudderai.command import Command

class PlaceCommand(Command):
    def __init__(self, x, y):
        self.target_x = self.LETTER_MAPPING[x]
        self.target_y = int(y) - 1
        