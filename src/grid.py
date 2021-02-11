class Grid:

    def __init__(self):
        self.grid = list()

    def count_occupied_cells(self):
        culture = 0
        livable = 0
        for row in self.grid:
            for cell in row:
                if cell == "#":
                    culture += 1
                if cell == "L":
                    livable += 1
        return culture, livable

    def initialize_grid(self, file_name: str):
        self.grid = list()  # Make sure empty grid
        with open(file_name) as f:
            for line in f:
                # exclude newline char
                self.grid.append([character for character in line[:-1]])

    def sprout_culture(self):
        # TODO: CHANGE THIS TO DO IN PLACE
        # I have tried iterating over with i & j
        # and changing value directly in self.grid
        next_hour_grid = list()

        for row in self.grid:
            current_row = list()
            for cell in row:
                if cell == "L":
                    current_row.append("#")
                if cell == ".":
                    current_row.append(".")
            next_hour_grid.append(current_row)

        self.grid = next_hour_grid

    def apply_rules(self):
        """
        Returns another grid for the next hour's growth
        """

        def count_adj_cultures(x, y):

            adj_cultures = 0

            if 0 < x < len(self.grid) - 1:
                xi = (0, -1, 1)
            elif x > 0:
                xi = (0, -1)
            else:
                xi = (0, 1)

            if 0 < y < len(self.grid[0]) - 1:
                yi = (0, -1, 1)
            elif y > 0:
                yi = (0, -1)
            else:
                yi = (0, 1)

            for a in xi:
                for b in yi:
                    if a == b == 0:
                        continue
                    if self.grid[x + a][y + b] == "#":
                        adj_cultures += 1

            return adj_cultures

        def determine_new_char(cell: str, i: int, j: int) -> str:

            if cell == "#" and count_adj_cultures(i, j) >= 4:
                return "L"
            if cell == "L" and count_adj_cultures(i, j) == 0:
                return "#"
            return cell

        next_hour_grid = list()

        for i, row in enumerate(self.grid):
            current_row = list()
            for j, cell in enumerate(row):
                current_row.append(determine_new_char(cell, i, j))
            next_hour_grid.append(current_row)

        self.grid = next_hour_grid

    def get_2d_matrix(self):
        """
        Returns:
            List: List of all of the rows in the table
        """
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

        while not self.is_stable:
            self.hour += 1
            self.previous_grid = self.grid.get_2d_matrix()
            self.grid.apply_rules()
            self.is_stable = self.grid.get_2d_matrix() == self.previous_grid

    def answer_experiment_questions(self):
        print("Hours it takes the culture to stabilize:", self.hour)
        culture, livable = self.grid.count_occupied_cells()
        print("No. of cells occupied with culture after stabilization:", culture)
        print(
            f"Ratio of culture/livable spaces as percentage: {round((culture/livable)*100, 2)}%"
        )
