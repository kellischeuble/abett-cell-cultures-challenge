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