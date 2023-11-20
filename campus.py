class Place: # Node in our non-linear data structure
  def __init__(self, name):
    self.name = name
    self.walking_time_to = []

class WalkingTimeTo: # Weighted Edg
  def __init__(self, time, destination):
    self.time = time
    self.destination = destination

pki = Place("PKI")
walmart = Place("Walmart")
mammel_hall = Place("Mammel Hall")
brb = Place("Biomechanics Research Building")
library = Place("Criss Library")
milo_bail = Place("Milo Bail Student Center")

pki.walking_time_to.append(WalkingTimeTo(5, mammel_hall))
mammel_hall.walking_time_to.append(WalkingTimeTo(5, pki))

mammel_hall.walking_time_to.append(WalkingTimeTo(10, walmart))
walmart.walking_time_to.append(WalkingTimeTo(10, mammel_hall))

brb.walking_time_to.append(WalkingTimeTo(15, pki))
pki.walking_time_to.append(WalkingTimeTo(15, brb))

library.walking_time_to.append(WalkingTimeTo(10, brb))
brb.walking_time_to.append(WalkingTimeTo(10, library))

library.walking_time_to.append(WalkingTimeTo(5, milo_bail))
milo_bail.walking_time_to.append(WalkingTimeTo(5, library))

milo_bail.walking_time_to.append(WalkingTimeTo(5, brb))
brb.walking_time_to.append(WalkingTimeTo(5, milo_bail))


# Now do something fun
# What is the fastest way to walk from Milo Bail
# to PKI?