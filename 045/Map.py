import Scenes
class Map(object):

    scenes = {
        "death" : Scenes.Death(),
        "bridge" : Scenes.Bridge(),
        "feiry_pit" : Scenes.Feiry_Pit(),
        "magical_horse" : Scenes.Magical_Horse(),
        "dragon" : Scenes.Dragon(),
        "ending" : Scenes.Finished()
        }
    def __init__(self, opening_scene):
        self.opening_scene = opening_scene

    def  openner(self):
        return self.scenes.get(self.opening_scene)

    def get_scene(self,next_scene_name):
        self.next_scene_name = next_scene_name
        return self.scenes.get(self.next_scene_name)

#a = Map("bridge")

#a.get_scene()

#Map.scenes.get("death")


