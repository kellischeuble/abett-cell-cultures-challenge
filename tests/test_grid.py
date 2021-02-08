from src.grid import Grid
from tests.data.cultures import (
    initial,
    sprouted,
    hour_two,
    hour_three,
    hour_four,
    hour_five,
)

grid_to_test = Grid()
grid_to_test.initialize_grid("tests/data/cell_culture.txt")

initialized_grid = grid_to_test.get_2d_matrix()
initial_count_cells = grid_to_test.count_occupied_cells()

grid_to_test.sprout_culture()
sprouted_grid = grid_to_test.get_2d_matrix()

grid_to_test.apply_rules()
hour_two_grid = grid_to_test.get_2d_matrix()

grid_to_test.apply_rules()
hour_three_grid = grid_to_test.get_2d_matrix()

grid_to_test.apply_rules()
hour_four_grid = grid_to_test.get_2d_matrix()

grid_to_test.apply_rules()
hour_five_grid = grid_to_test.get_2d_matrix()


def test_initialize_grid():
    assert len(grid_to_test.grid) == 10
    assert len(grid_to_test.grid[0]) == 10
    assert initialized_grid == initial


def test_count_occupied_cells():
    assert initial_count_cells[0] == 0


def test_sprout_culture():
    assert sprouted_grid == sprouted


def test_apply_rules():
    assert hour_two_grid == hour_two
    assert hour_three_grid == hour_three
    assert hour_four_grid == hour_four
    assert hour_five_grid == hour_five
