from grid import Grid, Experiment

if __name__ == "__main__":
    g = Grid()
    g.initialize_grid("./data/cell-cultures.txt")
    e = Experiment(g)
    e.run_experiment()
    e.answer_experiment_questions()
