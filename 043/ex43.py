from sys import exit
from random import randint
from textwrap import dedent
# How do I start the game?
# is it just a bunch of conditional statements?
# no its done by return statements somehow
#

# Coding this like I am someone else is the problem for sure.... but we need arrays for and to
# randomly choose from that array.
# The success path is linear so it should return the next path when finished

# This was dificult to code as he made a crappy outline and I dont think like him so that was a
# mistake. The outline threw me and I didnt understand how one object linked to the other which is by
# a dictionary.... A dictionary was the missing link. There was nothing complicated about it I just
# was stuck and he had literally no hints that were helpful. It feels rushed and it shouldnt be a
# rushed thing
class Scene(object):
    def enter(self):
        print("Not sure what I am doing here")
        print("read up on exit and rand and dedent with 3 qoutes")
        exit(1)

class Engine(object):
# this is the game engine.
    def __init__(self, scene_map):
        self.scene_map = scene_map

    def play(self):
        current_scene = self.scene_map.opening_scene()
        last_scene = self.scene_map.next_scene('finished')

        while current_scene != last_scene:
            #print("beginning of the while loop, the current_scene is: ", current_scene)
            next_scene_name = current_scene.enter()
            #print("The next_scene_name is: ", next_scene_name)
            current_scene = self.scene_map.next_scene(next_scene_name)
            #print("End of while loop")
        # be sure to print out the last scene
        current_scene.enter()
#a_map = Map('central_corridor')
#a_game = Engine(a_map)
#a_game.play()
class Death(Scene):

    quips = [
        "You died. Keep trying!",
        "I know this game is stupid",
        "Zed is awesome in real life",
        "I hate this game as much as I hated coding it",
        "Objects are complex!",
        "I blame others when I dont succeed"
]
    def enter(self):
        print(Death.quips[randint(0, len(self.quips)-1)])
        exit(1)

class CentralCorridor(Scene):

    def enter(self):
        # Ok so the enter scene is the description of the scene itself
        print(dedent("""
            The Gothons of Planet Percal #25 have invaded your ship and
            destroyed your entire crew. You are the last surviving
            member and your last mission is to get the neutron destruct
            bomb from the Weapons Armory, put it in the bridge, and
            blow the ship up after getting into an escape pod.

            You're running down the central corridor to the Weapons
            Armory when a Gothon jumps out, red scaly skin, dark grimy
            teeth, and evil clown costume flowing around his hate
            filled body. He's blocking the door to the Armory and
            about to pull a weapon to blast you.
            """))

            # get some user input
            # "Games" like these server no purpose, guessing only to read what happens requires
            # zero skill just annoying patience.
        action = input("{shoot, dodge, joke} ")

        if action == "shoot":
            print(dedent("""
                Quick on the draw you yank out your blaster and fire
                it at the Gothon. His clown costume is flowing and
                moving around his body, which throws off your aim.
                Your laser hits his costume but misses him entirely.
                This completely ruins his brand new costume his mother
                bought him, which makes him fly into an insane rage
                blast you repeatedly in the face until you are
                dead. Then he eats you.
                """))
            return 'death'

        elif action == "dodge":
            print(dedent("""
                Like a world class boxer you dodgee, weave, slip and
                slide right as the Gorthon's blaster cranks a laser
                past your head. In the middle of your artful dodge
                your foot slips and you bang your head on the metal
                wall and pass out. You wake shortly after only to
                die as the Gothon stomps on your head and eats you.
                """))
            return 'death'

        elif action == 'joke':
            print(dedent("""
                Lucky for you they made you learn Gothon insults in
                the academy. You tell the one Gothon joke you know:
                Lbhe zbgure vf fb sng, jura fur fvgf nebhaq gur ubhfr,
                fur fvgf nebhaq gur ubhfr. The Gothon stops, tries
                not to laugh, then busts out laughing and can't move.
                While he's laughing you run up and shoot him square in
                the head putting him down, then jump through the
                Weapon Armory door.
                """))

            return 'laser_weapon_armory'

        else:
            print("DOES NOT COMPUTE!")
            return 'central_corridor'

class LaserWeaponArmory(Scene):

    def enter(self):
        print(dedent("""
            You do a dive roll into the Weapon Armory, crouch and scan the room
            for mor Gothons that might be hiding. It's dead quiet, too quiet.
            You stand up and run to the far side of the room and find the
            neutron bomb in its container. There's a keypad lock on the box
            and you need the code to get the bomb out. If you get the code
            wrong ten times then the lock closes forever and you can't
            get the bomb. The code is 3 digits.
            """))
        action = input("its 0132> ")

        count = 0

        while count < 10:
            count += 1
            if count > 10:
                print(dedent("""
                    The keypad locks with a resounding click. Standing you make for
                    The door when suddenly the chamber door slams shut sealing you
                    within it. It looks like the keypad was bobby trapped. You starve
                    to death with only the keypads menacing "ERROR" message to
                    comfort you.
                    """))
                return 'death'

            elif  action == "0132" and count <= 10:
                print(dedent("""
                    The container clicks open and the seal breaks, letting gas out.
                    You grab the neutron bomb and run as fast as you can to the
                    bridge where you must place it in the right spot.
                    """))
                return 'the_bridge'

            elif  count < 10:
                action = input("its 0132>")

class TheBridge(Scene):

    def enter(self):
        print(dedent("""
            You burst onto the Bridge with the netron destruct bomb
            under your arm and surprise 5 Gothons who are trying to
            take control of the ship.  Each of them has an even uglier
            clown costume than the last.  They haven't pulled their
            weapons out yet, as they see the active bomb under your
            arm and don't want to set it off.
            """))

        action = input("{slowly place bomb, throw bomb}")
        if action == "slowly place bomb":
            print("")
            return 'escape_pod'
        else:
            print("")
            return 'death'
class EscapePod(Scene):

    def enter(self):
        print(dedent("""
            You point your blaster at the bomb under your arm
            and the Gothons put their hands up and start to sweat.
            You inch backward to the door, open it, and then carefully
            place the bomb on the floor, pointing your blaster at it.
            You then jump back through the door, punch the close button
            and blast the lock so the Gothons can't get out.
            Now that the bomb is placed you run to the escape pod to
            get off this tin can.

            You rush through the ship desperately trying to make it to
            the escape pod before the whole ship explodes.  It seems like
            hardly any Gothons are on the ship, so your run is clear of
            interference.  You get to the chamber with the escape pods, and
            now need to pick one to take.  Some of them could be damaged
            but you don't have time to look.  There's 5 pods,
             """))
        action = input(">")
        if action == "2":
            print(dedent("""
                You jump into pod 2 and hit the eject button.
                The pod easily slides out into space heading to
                the planet below.  As it flies to the planet, you look
                back and see your ship implode then explode like a
                bright star, taking out the Gothon ship at the same
                time.
                """))
            return 'finished'
        else:
            return 'death'
class Finished(Scene):
    def enter(self):
        print("You won! Good Job.")
        return 'finished'


class Map(object):
    # Dictionary
    scenes = {
        'central_corridor': CentralCorridor(),
        'laser_weapon_armory': LaserWeaponArmory(),
        'the_bridge': TheBridge(),
        'escape_pod': EscapePod(),
        'death': Death(),
        'finished': Finished(),
    }
# Lets break down Map/Engine magic
# When the map oject is called it needs a parameter called start scene. You see this an example of
# this with a_map = Map('central_corridor')
# Then the engine function takes the dict value of central_corridor and inputs into map opening scene
# Then the scene loads and the engine while loop controls it.
    def __init__(self, start_scene):
        self.start_scene = start_scene

    def next_scene(self, scene_name):
        val = Map.scenes.get(scene_name)
        return val
    def opening_scene(self):
        return self.next_scene(self.start_scene)

a_map = Map('central_corridor')
a_game = Engine(a_map)
a_game.play()
