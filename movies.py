class Movie: # Node class
  def __init__(self, name):
    self.name = name
    self.share_actors_with = [] #Unweighted because our edges don't have weights


avengers =  Movie("The Avengers")
captain_america = Movie("Captian America")
iron_man = Movie("Iron Man")
thor = Movie("Thor")
knives_out = Movie("Knives Out")

avengers.share_actors_with.append(captain_america)
captain_america.share_actors_with.append(avengers)

avengers.share_actors_with.append(iron_man)
iron_man.share_actors_with.append(avengers)

avengers.share_actors_with.append(thor)
thor.share_actors_with.append(avengers)

captain_america.share_actors_with.append(knives_out)
knives_out.share_actors_with.append(captain_america)

# Now do something fun
# How can you go from Iron Man to Knives out?