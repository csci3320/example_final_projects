class Airport: # The nodes in our non-linear data structure
  def __init__(self, name):
    self.name = name
    self.edges = []
  def __str__(self):
    return self.name
  def __repr__(self):
    return self.__str__()

class FlightTime: # The edges in our non-linear data structure
  def __init__(self, time, destination):
    self.time = time
    self.destination = destination
  def __str__(self):
    return self.destination + "->" + str(self.time)
  def __repr__(self):
    return self.__str__()

oma = Airport("OMA")
atl = Airport("ATL")
sfo = Airport("SFO")
lax = Airport("LAX")

oma.edges.append(FlightTime(4, atl))
atl.edges.append(FlightTime(4, oma))

oma.edges.append(FlightTime(5, sfo))
sfo.edges.append(FlightTime(5, oma))

oma.edges.append(FlightTime(10, lax))
lax.edges.append(FlightTime(10, oma))

sfo.edges.append(FlightTime(1, lax))
lax.edges.append(FlightTime(1, sfo))

atl.edges.append(FlightTime(6, lax))
lax.edges.append(FlightTime(6, atl))

# Now do something fun, 
# like find the shortest time to get 
# from oma to lax



    



