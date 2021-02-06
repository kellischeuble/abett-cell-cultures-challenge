class Cell:

    def __init__(self, character):

        CHARACTER_MAP = {"X": "occupied", 
                         "L":"livable", 
                         ".": "unlivable"}

        self.character = character
        self.status = CHARACTER_MAP[self.character]

    def __repr__(self):
        return f"{self.character}"