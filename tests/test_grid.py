from src.grid import Grid

grid_to_test = Grid()

def test_initialize_grid():
    grid_to_test.initialize_grid("tests/test-data.txt")
    assert len(grid_to_test.grid) == 10
    assert len(grid_to_test.grid[0]) == 10
    assert grid_to_test.grid == [["L",".","L","L",".","L","L",".","L","L"],
                                ["L","L","L","L","L","L","L",".","L","L"],
                                ["L",".","L",".","L",".",".","L",".","."],
                                ["L","L","L","L",".","L","L",".","L","L"],
                                ["L",".","L","L",".","L","L",".","L","L"],
                                ["L",".","L","L","L","L","L",'.','L',"L"],
                                [".",".","L",".","L",".",".",".",".","."],
                                ["L","L","L","L","L","L","L","L","L","L"],
                                ["L",".","L","L","L","L","L","L",".","L"],
                                ["L",".","L","L","L","L","L",".","L","L"]]

def test_count_occupied_cells():
    pass

def test_apply_rules():
    pass