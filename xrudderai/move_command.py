from xrudderai.command import Command

class MoveCommand(Command):
    def __init__(self, x1, y1, x2, y2):
        self.source_x = x1
        self.source_y = y1
        self.target_x = x2
        self.target_y = y2

    
    def __str__(self):
        return "Move {}{} to {}{}".format(
            Command.REVERSE_LETTER_MAPPING[self.source_x],
            self.source_y,
            Command.REVERSE_LETTER_MAPPING[self.target_x],
            self.target_y
        )
