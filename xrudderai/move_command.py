from xrudderai.command import Command

class MoveCommand(Command):
    def __init__(self, x1, y1, x2, y2):
        self.source_x = self.LETTER_MAPPING[x1]
        self.source_y = int(y1) - 1
        self.target_x = self.LETTER_MAPPING[x2]
        self.target_y = int(y2) - 1
