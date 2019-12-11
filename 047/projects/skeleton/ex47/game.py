class Room(object):

    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.paths = {}

    def go(self, direction):
        return self.paths.get(direction, None)

    def add_paths(self, paths):
        # this uses the update attribute method in python dict to modify or in this case add values
        # the dictionary called paths
        self.paths.update(paths)
