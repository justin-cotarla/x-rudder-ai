from xrudderai.command import Command

class MoveCommand(Command):
    def __init__(self, x1, y1, x2, y2):
        self.source_x = x1
        self.source_y = y1
        self.target_x = x2
        self.target_y = y2
