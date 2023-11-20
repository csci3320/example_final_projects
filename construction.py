class Task: # Our node class
  def __init__(self, name):
    self.name = name
    self.next = [] # Unweighted edges

dig_foundation = Task("Dig Foundation")
pour_foundation = Task("Pour Foundation")
framing = Task("Framing")
exterior = Task("Exterior")
plumbing = Task("Plumbing")
hvac = Task("HVAC")
electrical = Task("Electrical")
dry_wall = Task("Dry Wall")

dig_foundation.next.append(pour_foundation)
pour_foundation.next.append(framing)
framing.next.append(exterior)
framing.next.append(plumbing)
framing.next.append(hvac)
framing.next.append(electrical)
plumbing.next.append(dry_wall)
hvac.next.append(dry_wall)
electrical.next.append(dry_wall)

# Now do something fun, like what has to be done
# before electrical?