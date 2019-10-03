class MoveCommand:

    source_x = ""
    source_y = ""
    target_x = ""
    target_y = ""

    def __init__(self, x1, y1, x2, y2):
        self.source_x = x1
        self.source_y = y2
        self.target_x = x2
        self.target_y = y2

    def __str__(self):
        return "Move token from "+self.source_x+str(self.source_y)+" to "+self.target_x+str(self.target_y)
