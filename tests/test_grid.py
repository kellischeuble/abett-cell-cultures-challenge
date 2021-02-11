from src.grid import Grid
from tests.data.cultures import (
    initial,
    sprouted,
    hour_two,
    hour_three,
    hour_four,
    hour_five,
)


def create_grid(file):
    grid = Grid()
    grid.initialize_grid(file)
    return grid


def test_initialize_grid():
    grid = create_grid("tests/data/cell_culture.txt")
    initialized_grid = grid.get_2d_matrix()

    assert len(grid.grid) == 10
    assert len(grid.grid[0]) == 10
    assert initialized_grid == initial


def test_count_occupied_cells():
    grid = create_grid("tests/data/cell_culture.txt")
    initial_count_cells = grid.count_occupied_cells()

    assert initial_count_cells[0] == 0


def test_sprout_culture():
    grid = create_grid("tests/data/cell_culture.txt")
    grid.sprout_culture()
    sprouted_grid = grid.get_2d_matrix()

    assert sprouted_grid == sprouted


def test_grow_one_hour():
    grid = create_grid("tests/data/cell_culture.txt")
    grid.sprout_culture()

    grid.grow_one_hour()
    hour_two_grid = grid.get_2d_matrix()

    grid.grow_one_hour()
    hour_three_grid = grid.get_2d_matrix()

    grid.grow_one_hour()
    hour_four_grid = grid.get_2d_matrix()

    grid.grow_one_hour()
    hour_five_grid = grid.get_2d_matrix()

    assert hour_two_grid == hour_two
    assert hour_three_grid == hour_three
    assert hour_four_grid == hour_four
    assert hour_five_grid == hour_five
