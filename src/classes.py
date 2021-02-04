class Grid:

    def __init__(self):
        self.grid = list()
        self.cells_occupied = 0

    def count_occupied_cells(self):
        self.cells_occupied = 0
        for row in self.grid:
            for cell in row:
                if cell.livable:
                    self.cells_occupied += 1
    
    def initialize_grid(self, file_name):
        self.grid = list() # Make sure empty grid
        with open(file_name) as f:
            for line in f:
                # exclude newline char
                self.grid.append([Cell(character) for character in line[:-1]])

    def apply_rules(self):
        

    
class Cell:

    def __init__(self, character):
        self.character = character
        if character == "L" or character == "#":
            self.livable = True
        else:
            self.livable = False

    def __repr__(self):
        return f"{self.character}"
        

class Experiment:

    def __init__(self, initial_grid):
        self.initial_grid = initial_grid
        # what's best practice to do with this when
        # we don't necessarily need it when we initialize it?
        self.previous_grid = list()
        self.current_grid = list()
        self.is_stable = False
        self.hour = 0

    def run_experiment(self):

        while not self.is_stable:
            self.hour += 1



g = Grid()
g.initialize_grid("/Users/kellischeuble/Desktop/interviews/abett_technical_challenge/abett-cell-cultures-challenge/data/cell-cultures.txt")
print(g.grid)