class Planet:

    def __init__(self, name, position):
        self.name = name
        self.position = position
        self.size = 0
        self.temp = 0
        self.humanity = False


class Mercury(Planet):
    def __init__(self, position, name='Mercury'):
        super().__init__(name, position)
