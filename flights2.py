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

start = oma
end = lax
all_airports = [oma, lax, atl, sfo]

shortest_distances = {}
visited = [oma]
unvisited = [x for x in all_airports if x not in visited]


UNVISITED = 10000

for airport in all_airports:
  if airport is start:
    shortest_distances[airport] = 0
  else:
    shortest_distances[airport] = UNVISITED


while len(unvisited) > 0:
  candidates = {}
  for visited_airport in visited:
    shortest_distance = shortest_distances[visited_airport]
    for edge in visited_airport.edges:
      new_distance = edge.time + shortest_distance
      new_airport = edge.destination
      if new_airport in visited:
        continue
      if new_airport in candidates:
        if candidates[new_airport] > new_distance:
          candidates[new_airport] = new_distance
      else:
        candidates[new_airport] = new_distance
  # Now find the closest candidate
  closest_candidate = min(candidates, key=candidates.get )
  closest_candidate_distance = candidates[closest_candidate]
  visited.append(closest_candidate)
  unvisited.remove(closest_candidate)
  shortest_distances[closest_candidate] = closest_candidate_distance
  
print("The shortest path to " + str(end) + " is " + str(shortest_distances[end]))


# for airport in visited:
#   airport_object = airport[0]
#   flight_time = airport[1]

#   for destination in airport_object.edges:
#     matches = filter(lambda a: a[0], possible)
#     if destination in matches:


    



