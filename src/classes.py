class Grid:

    def __init__(self):
        self.grid = list()
        self.cells_occupied = 0

    def count_occupied_cells(self):
        self.cells_occupied = 0
        for row in self.grid:
            for cell in row:
                if cell.status == "occupied":
                    self.cells_occupied += 1
    
    def initialize_grid(self, file_name:str):
        self.grid = list() # Make sure empty grid
        with open(file_name) as f:
            for line in f:
                # exclude newline char
                self.grid.append([Cell(character) for character in line[:-1]])

    def apply_rules(self):
        """
        Returns another grid for the next hour's growth
        """
        
        def count_neighbors(i, j):
            neighbors = 0
            # Make sure this is looking at edge cases (literal edges - should they be counted as unlivable??)
            # Make this more reusable and not so repetitive 
            if self.grid[[i+1][j]].status == "occupied":
                neighbors += 1


        def determine_if_livable(cell, i, j):
            if cell.livable & count_neighbors(i, j) < 4:
                return True
            return False
            
        next_hour_grid = list()

        # iterate through the grid and return a new one.
        for i, row in enumerate(self.grid):
            current_row = list()
            for j, cell in enumerate(row):
                if determine_if_livable(cell, i, j):
                    current_row.append(["X"])
                else:
                    current_row.append(["."])
            next_hour_grid.append(current_row)

    
class Cell:

    def __init__(self, character):

        CHARACTER_MAP = {"X": "occupied", 
                         "L":"livable", 
                         ".": "unlivable"}

        self.character = character
        self.status = CHARACTER_MAP[self.character]

    def __repr__(self):
        return f"{self.character}"
        

class Experiment:

    def __init__(self, initial_grid):
        self.initial_grid = initial_grid
        self.is_stable = False
        self.hour = 0

    def run_experiment(self):

        previous_grid = self.initial_grid
        current_grid = list()

        while not self.is_stable:
            self.hour += 1



g = Grid()
g.initialize_grid("/Users/kellischeuble/Desktop/interviews/abett_technical_challenge/abett-cell-cultures-challenge/data/cell-cultures.txt")
print(g.grid)