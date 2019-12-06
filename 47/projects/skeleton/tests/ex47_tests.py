from nose.tools import *
from ex47.game import Room
# Take the Room class and try and break it with this unit test.
def test_room():
    gold = Room("GoldRoom",
                """This room has gold in it you can grab. There's a
                door to the north.""")
    # The first tests ensures that the name of the instance of the class is GoldRoom (pretty silly as
    # That is obvious by just reading the code. The next one checks that paths is empty
    assert_equal(gold.name, 'GoldRoom')
    assert_equal(gold.paths, {})

def test_room_paths():
    center = Room("Center", "Test room in the center.")
    north = Room("North", "Test room in the north.")
    south = Room("South", "Test room in the south.")

    center.add_paths({"north": north, "south": south})
    assert_equal(center.go('north'), north)
    assert_equal(center.go('south') , south)

def test_map():
    start = Room("Start", "You can go west and down a hole.")
    west = Room("Trees" , "There are trees here, you can go east.")
    down = Room("Dungeon", "It's dark down here, you can go up.")

    # These are all instances of the Room class and each one with have a different dict
    start.add_paths({'west': west, 'down': down})
    west.add_paths({'east': start})
    down.add_paths({'up': start})

    assert_equal(start.go('west'), west)
    assert_equal(start.go('west').go('east'), start)
    assert_equal(start.go('down').go('up'), start)
