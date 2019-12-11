import Map
class Engine(object):
    def __init__(self, start_room):
        self.start_room = start_room

    def play(self):
        current_room = self.start_room.openner()
        last_room = Map.Map.scenes.get("ending")
        while current_room != last_room:
            next_scene = current_room.describe()
            current_room = self.start_room.get_scene(next_scene)
        current_room.describe()
m = Map.Map("bridge")
e = Engine(m)
e.play()
