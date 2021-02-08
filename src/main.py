from grid import Grid, Experiment

if __name__ == "__main__":
    g = Grid()
    # g.initialize_grid("/Users/kellischeuble/Desktop/interviews/abett_technical_challenge/abett-cell-cultures-challenge/data/cell-cultures.txt")
    g.initialize_grid(
        "/Users/kellischeuble/Desktop/interviews/abett_technical_challenge/abett-cell-cultures-challenge/tests/data/cell_culture.txt"
    )

    e = Experiment(g)
    e.run_experiment()
    e.answer_experiment_questions()
