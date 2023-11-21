class Room:
  def __init__(self, name):
    self.name = name
    self.north = None
    self.south = None
    self.east = None
    self.west = None

forest = Room("Forest")
west_of_house = Room("West of House")
dragons_lair = Room("Dragon's Lair")

forest.north = west_of_house
forest.east = dragons_lair

west_of_house.east = dragons_lair
west_of_house.sount = forest

