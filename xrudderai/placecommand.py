class PlaceCommand:

    target_x = ""
    target_y = ""

    def __init__(self, x, y):
        self.target_x = x
        self.target_y = y

    def __str__(self):
        return "Place token at "+self.target_x+str(self.target_y)