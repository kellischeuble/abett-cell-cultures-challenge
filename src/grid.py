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

        def count_adj_cultures(i, j):

            adj_cultures = 0

            # TODO: Make this more reusable and not so repetitive

            top = i == 0
            left_edge = j == 0
            right_edge = j == (len(self.grid[0]) - 1)
            bottom = i == (len(self.grid) - 1)

            if not top:
                if self.grid[i - 1][j] == "#":
                    adj_cultures += 1
                if not right_edge:
                    if self.grid[i - 1][j + 1] == "#":
                        adj_cultures += 1
                if not left_edge:
                    if self.grid[i - 1][j - 1] == "#":
                        adj_cultures += 1
            if not bottom:
                if self.grid[i + 1][j] == "#":
                    adj_cultures += 1
                if not right_edge:
                    if self.grid[i + 1][j + 1] == "#":
                        adj_cultures += 1
                if not left_edge:
                    if self.grid[i + 1][j - 1] == "#":
                        adj_cultures += 1
            if not left_edge:
                if self.grid[i][j - 1] == "#":
                    adj_cultures += 1
            if not right_edge:
                if self.grid[i][j + 1] == "#":
                    adj_cultures += 1

            return adj_cultures

        def determine_new_char(cell, i, j):
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
            if self.grid.get_2d_matrix() == self.previous_grid:
                self.is_stable = True

    def answer_experiment_questions(self):
        print("Hours it takes the culture to stabilize:", self.hour)
        culture, livable = self.grid.count_occupied_cells()
        print("No. of cells occupied with culture after stabilization:", culture)
        print(
            f"Ratio of culture/livable spaces as percentage: {round((culture/livable)*100, 2)}%"
        )
