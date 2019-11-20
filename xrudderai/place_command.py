from xrudderai.command import Command

class PlaceCommand(Command):
    def __init__(self, x, y):
        self.target_x = x
        self.target_y = y

    def __str__(self):
        return "Place {}{}".format(
            Command.REVERSE_LETTER_MAPPING[self.target_x],
            self.target_y,
        )        