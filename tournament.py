class Team:
  def __init__(self, name):
    self.name = name

class Game:
  def __init__(self, team_one, team_two):
    self.team_one, team_two = team_one, team_two
    self.winner = None

alice = Team("alice")
bob = Team("Bob")
carlos = Team("Carlos")
dean = Team("Dean")

first_round_one = Game(alice, bob)
first_round_one.winner = alice

first_round_two = Game(carlos, dean)
first_round_two.winner = carlos

second_round = Game(first_round_one.winner, first_round_two.winner)
