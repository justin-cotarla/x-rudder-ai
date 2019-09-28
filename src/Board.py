class Board:

    grid = []

    def __init__(self):
        self.grid = [[None]*12 for n in range(10)]
        print(self.grid)
