class Level:
    def __init__(self, levelNumber) -> None:
        self.mapSize = 15,15
        self.tileSize = 40
        self.grid = []

        fileName = 'lvl' + str(levelNumber) + '.txt'
        print(f"File name will be {fileName}")

        pass


