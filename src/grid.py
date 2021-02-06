class Grid:

    def __init__(self):
        self.grid = list()

    def count_occupied_cells(self):
        cells_occupied = 0
        for row in self.grid:
            for cell in row:
                if cell == "#":
                    cells_occupied += 1
        return cells_occupied 
    
    def initialize_grid(self, file_name:str):
        self.grid = list() # Make sure empty grid
        with open(file_name) as f:
            for line in f:
                # exclude newline char
                self.grid.append([character for character in line[:-1]])

    def sprout_culture(self):
        for row in self.grid:
            for cell in row:
                if cell == "L":
                    cell = "#"

    def apply_rules(self):
        """
        Returns another grid for the next hour's growth
        """
        
        def count_adj_cultures(i, j):

            adj_cultures = 0
            
            # TODO: Make this more reusable and not so repetitive 

            top = (i == 0)
            left_edge = (j == 0)
            right_edge = (j == (len(self.grid[0]) -1))
            bottom = (i == (len(self.grid) -1))

            if not top:
                if self.grid[i-1][j] == "#":
                    adj_cultures += 1
                if not right_edge:
                    if self.grid[i-1][j+1] == "#":
                        adj_cultures += 1
                if not left_edge:
                    if self.grid[i-1][j-1] == "#":
                        adj_cultures += 1
            if not bottom:
                if self.grid[i+1][j] == "#":
                    adj_cultures += 1
                if not right_edge:
                    if self.grid[i+1][j+1] == "#":
                        adj_cultures += 1
                if not left_edge:
                    if self.grid[i+1][j-1] == "#":
                        adj_cultures += 1
            if not left_edge:
                if self.grid[i][j-1] == "#":
                    adj_cultures += 1
            if not right_edge:
                if self.grid[i][j+1] == "#":
                    adj_cultures += 1
            
            return adj_cultures
    

        def determine_new_char(cell, i, j):
            if cell == "#" and count_adj_cultures(i, j) >= 4:
                return "L"
            if cell == "L" and count_adj_cultures(i, j) == 0:
                return "#"
            return cell
    
        next_hour_grid = list()

        print(self.grid)

        for i, row in enumerate(self.grid):
            current_row = list()
            for j, cell in enumerate(row):
                current_row.append(determine_new_char(cell, i, j))
            next_hour_grid.append(current_row)
 
        self.grid = next_hour_grid   
    
    def get_2d_matrix(self):
        return [[cell for cell in row] for row in self.grid]

    def __repr__(self):
        return f"{[[cell for cell in row] for row in self.grid]}"


class Experiment:

    def __init__(self, initial_grid):
        self.previous_grid = initial_grid
        self.grid = initial_grid
        self.is_stable = False
        self.hour = 0

    def run_experiment(self):

        self.grid.sprout_culture()
        self.hour += 1

        while not self.is_stable:
            print("PREVIOUS GRID", self.previous_grid)
            print("CURRENT GRID", self.grid)
            self.hour += 1
            self.previous_grid = self.grid.get_2d_matrix()
            self.grid.apply_rules()
            print("NEW GRID", self.grid)
            if self.grid.get_2d_matrix() == self.previous_grid:
                self.is_stable = True

    def answer_experiment_questions(self):
        return self.hour, self.grid.count_occupied_cells()
        # Unclear on 3rd 

        

g = Grid()
# # g.initialize_grid("/Users/kellischeuble/Desktop/interviews/abett_technical_challenge/abett-cell-cultures-challenge/data/cell-cultures.txt")
g.initialize_grid("/Users/kellischeuble/Desktop/interviews/abett_technical_challenge/abett-cell-cultures-challenge/tests/test-data.txt")
e = Experiment(g)
e.run_experiment()
print("HOURS", e.hour)
# print("INITIALIZED GRID", g.grid)
# g.sprout_culture()
# print("SPROUTED", g.grid)
# print("APPLIED RULES", g.apply_rules())


# tested = [["L",".","L","L",".","L","L",".","L","L"],
#             ["L","L","L","L","L","L","L",".","L","L"],
#                 ["L",".","L",".","L",".",".","L",".","."],
#                 ["L","L","L","L",".","L","L",".","L","L"],
#                 ["L",".","L","L",".","L","L",".","L","L"],
#                 ["L",".","L","L","L","L","L",'.','L',"L"],
#                 [".",".","L",".","L",".",".",".",".","."],
#                 ["L","L","L","L","L","L","L","L","L","L"],
#                 ["L",".","L","L","L","L","L","L",".","L"],
#                 ["L",".","L","L","L","L","L",".","L","L"]]


# for i, row in enumerate(g.grid):
#     print("g.grid row", row)
#     print()
#     print("tested row", tested[i])
#     if row == tested[i]:
#         print("true")

# print(g.grid)