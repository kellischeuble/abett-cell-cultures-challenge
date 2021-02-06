from src.grid import Grid

grid_to_test = Grid()
grid_to_test.initialize_grid("tests/test-data.txt")

def test_initialize_grid():
    assert len(grid_to_test.grid) == 10
    assert len(grid_to_test.grid[0]) == 10
    # assert grid_to_test.grid == [["L",".","L","L",".","L","L",".","L","L"],
    #                             ["L","L","L","L","L","L","L",".","L","L"],
    #                             ["L",".","L",".","L",".",".","L",".","."],
    #                             ["L","L","L","L",".","L","L",".","L","L"],
    #                             ["L",".","L","L",".","L","L",".","L","L"],
    #                             ["L",".","L","L","L","L","L",'.','L',"L"],
    #                             [".",".","L",".","L",".",".",".",".","."],
    #                             ["L","L","L","L","L","L","L","L","L","L"],
    #                             ["L",".","L","L","L","L","L","L",".","L"],
    #                             ["L",".","L","L","L","L","L",".","L","L"]]

def test_count_occupied_cells():
    assert grid_to_test.count_occupied_cells() == 0

def test_apply_rules():
    pass