run_experiment:
	@python src/main.py

test: 
	@pytest -vvs tests/test_grid.py