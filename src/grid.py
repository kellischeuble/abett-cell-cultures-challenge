class Grid:

    def __init__(self):
        self.grid = list()

    def count_occupied_cells(self) -> tuple:
        """
        Counts number of cells where culture is growing
        (marked with a "#")
        Counts number of livable cells
        (marked with an "L")

        Returns:
            tuple: contains two integers with number of cultures
                    at index 0, and number of livable cells at
                    index 1
        """
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
        """
        Takes txt file representing the grid of cell culture medium
        This file should only "."s and "L"s

        Reads in file and initializes the 2d matrix represeting the grid

        Args:
            file_name (str): path to file
        """
        self.grid = list()  # Make sure empty grid
        with open(file_name) as f:
            for line in f:
                # exclude newline char
                self.grid.append([character for character in line[:-1]])

    def sprout_culture(self):
        """
        Once the grid is initialized, the culture then needs to sprout.
        
        All "L"s turn into "#"s - representing that the culture has
        sprouted
        """
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

    def grow_one_hour(self):
        """
        Returns another grid for the next hour's growth
        by applying rules:

        1. If a livable area ("L") is empty and there are no adjacent
            cell cultures ("#"), the cell will begin to grow -> ("#")
        2. If a cell culture ("#") has four or more adjacent locations 
            that are also growing cultures, it dies back -> ("L")
        3. All other cells stay the same
        """

        def count_adj_cultures(x:int, y:int) -> int:
            """
            Returns number of adjacent growing cultures

            Args:
                x (int): row of cell
                y (int): column of cell

            Returns:
                int: number of adjacent cultures growing
            """

            adj_cultures = 0

            # checks to see if the cell is on the top or 
            # bottom of the grid
            if 0 < x < len(self.grid) - 1:
                xi = (0, -1, 1)
            elif x > 0:
                xi = (0, -1)
            else:
                xi = (0, 1)

            # checks to see if the cell is on the side
            # of the grid
            if 0 < y < len(self.grid[0]) - 1:
                yi = (0, -1, 1)
            elif y > 0:
                yi = (0, -1)
            else:
                yi = (0, 1)

            for a in xi:
                for b in yi:
                    if a == b == 0: # the cell whose neighbors we are counting
                        continue
                    if self.grid[x + a][y + b] == "#":
                        adj_cultures += 1

            return adj_cultures

        def determine_new_state(cell_state: str, x: int, y: int) -> str:
            """
            Returns the new state of the cell by looking at the
            current state and the number of neighboring cultures

            Args:
                cell_state (str): cell state - either "#", "L", or "."
                x (int): row of cell
                y (int): column of cell

            Returns:
                str: the new state of the cell - either "#", "L", or "."
            """

            if cell_state == "#" and count_adj_cultures(x, y) >= 4:
                return "L"
            if cell_state == "L" and count_adj_cultures(x, y) == 0:
                return "#"
            return cell_state

        next_hour_grid = list()


        for i, row in enumerate(self.grid):
            current_row = list()
            for j, cell in enumerate(row):
                current_row.append(determine_new_state(cell, i, j))
            next_hour_grid.append(current_row)

        self.grid = next_hour_grid

    def get_2d_matrix(self):
        """
        Returns 2D list of grid for testing purposes
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
        """
        Runs entire experiment until the cells have all 
        stabilized 
        """

        self.grid.sprout_culture()

        while not self.is_stable:
            self.hour += 1
            self.previous_grid = self.grid.get_2d_matrix()
            self.grid.grow_one_hour()
            self.is_stable = self.grid.get_2d_matrix() == self.previous_grid

    def answer_experiment_questions(self):
        print("Hours it takes the culture to stabilize:", self.hour)
        culture, livable = self.grid.count_occupied_cells()
        print("No. of cells occupied with culture after stabilization:", culture)
        print(
            f"Ratio of culture/livable spaces as percentage: {round((culture/livable)*100, 2)}%"
        )
