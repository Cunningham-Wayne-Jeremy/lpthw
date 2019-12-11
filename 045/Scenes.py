from random import randint
from textwrap import dedent
from time import time
class Scene(object):

    def describe(self):
        print("Enter a description here")

class Death(Scene):
    quips=["Oops, you died",
           "Dont get frustrated, keep on going!",
           "How do you like the timed responses?",
           "Try again",
           "Game Over",
           "YOU DIED"
          ]
    def describe(self):
        print(self.quips[(randint(0,(len(self.quips)-1)))])
        exit(0)

class Bridge(Scene):
    def describe(self):
        print(dedent("""
                    Before you lies the castle of the dragon, said to hold the most beautiful
                    princess Daphne, legend tells of her eternal youth and beauty. She awaits
                    a fine knight to save her from the clutches of the dragon within.

                    You are Dirk a fine knight of Duetchland, equiped with your sword and armor
                    you have come to rescue the princess and in so doing become king.

                    As you begin your march on the castle you see it tower before you, with a broken
                    bridge leading to the main gate. You reach the bridge and begin to cross the wide
                    expanse of the swap that it encroaches.
                    """))
        input("Press ENTER to continue")
        print(dedent("""
                    As you cross the bridge a rotten board gives way beneath you, you grab hold of
                    the edge of the bridge. But as you attempt to climp up, something grabs your leg
                    out of the water.

                    You look down to see a large mass of tentacles with an eye at each ones tip.
                    One of the eyed tentacles is wrapped around your left leg with a vice grip, its
                    eye looks up at you hungrily.
                    """))

        input("Press ENTER to continue")
        start_time = time()
        stop_time = start_time + 6
        while start_time < stop_time:
            userinput = input("What do you do? ")
            start_time = time()
            if start_time > stop_time:
                print(dedent("""
                            You dont react fast enough and the beast warps another eye tentacle
                            around your other leg and it pulls you into its toothy maw becoming its
                            next meal.
                            """))
                return "death"
            elif "sword" in userinput or "attack" in userinput:
                print(dedent("""
                            In a panic, you draw your sword from your scabbard and cut the tentacle
                            clean off from the beast, freeing your leg. Ignoring the beasts roar of
                            pain, you hastily climb up to safety. As you rush to the door you hear
                            the roar of  water coming behind you, and you can feel the tentacled
                            beast inches away from your neck. Without looking back, you reach the
                            door and bar the exit for good measure.
                            """))
                return "feiry_pit"

class Feiry_Pit(Scene):
    def describe(self):
        print(dedent("""
                    Leaning against the door you let out a sigh of relief then turn to face your
                    surroundings. Your sigh of relief turns to one of despair as you realize you now
                    stand on a ledge with a lake of fire below you. The ledge of which you stand is
                    the only surviving peice of the floor that once rested here.

                    Three chandeliers hang low in front of you but the heat from the lake has lit
                    them on fire. They sway with a slight beeze and you wonder if you can use them
                    to make it across. Just as you think this you hear a click
                """))
        input("Press ENTER to continue")
        print(dedent("""
                    The ledge on which you stand begins to slide inward, it appears you have
                    triggered a trap!
                """))
        input("Press ENTER to continue")
        start_time = time()
        stop_time = start_time + 8
        while start_time < stop_time:
            userinput = input("What do you do? ")
            start_time = time()
            if start_time > stop_time:
                jumps = ["You jump to soon and fall into the lake of fire and brimstone below.",
                         "You jump too late and fall into the lake of fire and brimstone below",
                         "The ledge slips undeneath the wall pushing you into the lake of fire",
                         "Leaping onto a chandelier you ignite in its flames falling to your death",
                         "You jump THREE times onto the last chandelier but it falls into the fire"
                         ]
                print(jumps[(randint(0,4))])
                return "death"
            elif "jump jump jump jump" in userinput or "grab grab grab grab" in userinput:
                print(dedent("""
                            You deftly leap and jump and hop from one chandelier to another safely
                            arriving on the other side. You open the next door and see a staircase,
                            hastily you go up the stairs to the next level of the dragons castle.
                            """))
                return "magical_horse"


class Magical_Horse(Scene):
    def describe(self):
        print(dedent("""
                    At the top of the stairs you see a scarcely lit gigantic room. The room's size
                    is much wider than should be possible given the castles exterior. Most of the
                    "room" is actually a chasm with giant columns whose head nor tail you see due to
                    the dim light. You stand on a small oulook of cobblestone overlooking the chasm
                    and its crowded columns. The room is empty except for a suit of gilded horse
                    armor.

                    With naught to do you sit on the only available furniture, to think how to
                    proceed further within the castle. The dragon must have flown past these columns
                    but you lack wings and know not how to continue. As you think this the horse
                    armor beneath you glows and suddenly takes flight through the chasm of columns!
                    """))
        input("Press ENTER to continue")
        print(dedent("""
                    You hang on tightly taking the reigns to steer as the steed you fly on speeds
                    towards one of the large columns!"""))

        start_time = time()
        stop_time = start_time + 26
        dodge_pillar = start_time + 6
        dodge_fire = start_time + 12
        dodge_snake = start_time + 19
        count = 1

        while start_time < stop_time:
            userinput = input("What do you do? ")
            start_time = time()
            if "left" in userinput or "right" in userinput and count == 1 and start_time < dodge_pillar:
                print(dedent("""
                            You dodge the giant pillar but now face a new problem, you are racing
                            towards a wall of fire suspended between two pillars!
                            """))
                count += 1
                start_time = time()
            elif "left" in userinput or "right" in userinput and start_time < dodge_fire and count == 2:
                print(dedent("""
                            Dodging the fire you pass between two large columns when suddenly a large
                            python wrapped around one of the pillars attemps to bite you from above!
                            """))
                count +=1
                start_time = time()
            elif "down" in userinput and start_time < dodge_snake and count == 3:
                print(dedent("""
                            The snake misses you, crashing into another pillar and before you know it
                            the pillars are crashing into each other and the ceiling begins to collapse.
                            You dart for the only exit which is soon to be blocked by falling pillars. A
                            tiny hole remains open but your horse is too big to get through it!
                            """))
                count +=1
                start_time = time()
            elif "jump" in userinput or "off" in userinput and count == 4:
                print(dedent("""
                            Valiantly you leap off the magical horse and through the tiny hallway. You
                            hear behind you the thunder of pillars falling, the castle shakes and you
                            wait for the whole castle to come down upon you but it still stands.

                            Gingerly you open the door at the end of the hallway and proceed further into
                            the castle.
                            """))

                return "dragon"
            elif start_time > dodge_pillar and count == 1:
                print(dedent("""
                            You crash into the pillar, knocking you off the magical horse falling to
                            your death.
                            """))
                return "death"

            elif start_time > dodge_fire and count == 2:
                print(dedent("""
                            The flame is the last thing you see as you are turned to ash.
                            """))
                return "death"
            elif start_time > dodge_snake and count ==3:
                print(dedent("""
                            The snake devours you whole, you suffocate and are digested in its belly.
                            """))
                return "death"
            elif start_time > stop_time and count ==4:
                print(dedent("""
                            Your horse gets stuck between the falling pillars and you are crushed between them.
                            """))
                return "death"
            elif start_time > stop_time:
                print(dedent("""
                            Your horse becomes to quick to control and it jettisons off into the darkness.
                            """))
                return "death"

class Dragon(Scene):
    def describe(self):
        print(dedent("""
                    You open the door to the next room and there before lies the dragon! He sleeps on the biggest
                    pile of gold you have ever seen! And next to him is princess Daphne protected from harm and
                    given eternal life in a sphere of magical power.

                    Silently you move through a maze of expensive vases all stacked on top of each other. Deftly
                    you manuvuer between them but accidentally bump into a tower of vases! Its about to fall!
                    """))
        input("Press ENTER to continue:")
        start_time = time()
        stop_time = start_time + 41
        save_ceramic = start_time + 7
        dodge_tail = start_time + 14
        dodge_fire = start_time + 21
        grab_sword = start_time + 28
        attack = start_time + 35
        count = 1

        while start_time < stop_time:
            userinput = input("What do you do? ")
            start_time = time()
            if "stop" in userinput or "grab" in userinput and count == 1 and start_time < save_ceramic:
                print(dedent("""
                            Quickly you grab the stack of urns and try to stabalize the stack but a gold piece
                            falls from the mouth of an urn clinking on the ground then you hear the dragon begin
                            to sniff around.

                            You cower behind a pillar and as if sensing your fear the dragon whips its tail aiming
                            at your pillar!
                            """))
                count += 1
                start_time = time()
            elif "roll" in userinput or "jump" in userinput and start_time < dodge_tail and count == 2:
                print(dedent("""
                            You roll away from the pillar just in time as the dragons tail reduces the pillar
                            to stones. Drawing your sword you run at the beast to slay it. Just then the dragon
                            rears back his head, mouth agape full of flame.
                            """))
                count +=1
                start_time = time()
            elif "pillar" in userinput and start_time < dodge_fire and count == 3:
                print(dedent("""
                            The pillar you take cover behind heats up and sizzles as the front of it melts. Over
                            the roar of the fire through some sort of magical communciation you hear the angelic
                            voice of princess Daphne. "The sword, get the magical blade! The dragon is immune to
                            non magical weaponry!" Looking behind you see the blade.
                            """))
                count +=1
                start_time = time()
            elif "take" in userinput or "sword" in userinput or "blade" in userinput and start_time < grab_sword and count == 4:
                print(dedent("""
                            Laying on a pile of gold is the magical sword, you snatch it up as the dragon continues
                            his feiry assault on the pillar. When he takes a breath you jump out from behind the
                            pillar and face the beast, its nostrils still smoking from the intense flames.

                            With the swiftness of a serpent it snaps at your face.
                            """))
                count +=1
                start_time = time()
            elif "dodge" in userinput and start_time < attack and count == 5:
                print(dedent("""
                            You side step out of the way of the dragons deadly attack. Its giant neck is outstreched
                            before you.
                            """))
                count +=1
                start_time = time()
            elif "attack" in userinput or "chop" in userinput and start_time < attack and count == 6:
                print(dedent("""
                            With a heavy blow you chop the dragons head off rendering its head from its neck. The beast
                            falls with a crash as a sickly gurgle emanating from its throat echos over the castles halls.
                            """))
                count +=1
                start_time = time()
                return "ending"

            elif start_time > save_ceramic and count == 1:
                print(dedent("""
                            The cearmic crashes to the floor and without the element of surprise the dragon quickly eats you.
                            """))
                return "death"

            elif start_time > dodge_tail and count == 2:
                print(dedent("""
                            The dragon smashes the pillar and you along with it.
                            """))
                return "death"
            elif start_time > dodge_fire and count ==3:
                print(dedent("""
                            You hesitate before the dragons fearful gaze and are turned to ash beneath its flames.
                            """))
                return "death"
            elif start_time > grab_sword and count ==4:
                print(dedent("""
                            The Dragons flames overcome the pillar and you are reduced to ashes.
                            """))
                return "death"
            elif start_time > attack and count == 5:
                print(dedent("""
                            The dragon swallows you whole.
                            """))
                return "death"
            elif start_time > stop_time and count == 6:
                print(dedent("""
                            You hesitate before taking the killing blow and the dragon feeling thankful squeeze you
                            to death in gratitude.
                            """))
                return "death"


class Finished(Scene):

    def describe(self):
        print(dedent("""
                With the foul dragon slain the princess is free from her confinement. Grateful she falls in your arms.

                THE END
                """))

